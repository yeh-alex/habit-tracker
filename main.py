from datetime import timedelta
from fastapi import FastAPI
from sqlmodel import SQLModel, Field, create_engine
from datetime import date, datetime
from typing import Optional
from sqlmodel import Session
from sqlmodel import select

# --- 定義資料表 ---

class Habit(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # 主鍵,自動編號
    name: str                                                  # 習慣名稱
    created_at: datetime = Field(default_factory=datetime.now) # 建立時間,自動帶入

class CheckIn(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    habit_id: int = Field(foreign_key="habit.id")  # 外鍵,指向它屬於哪個 habit
    check_date: date                               # 打卡的日期(只要日期,不要時分秒)

# --- 建立資料庫連線 ---

engine = create_engine("sqlite:///habits.db")  # 會在資料夾生出一個 habits.db 檔案

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)  # 根據上面的 class 建出實體表格

# --- App ---

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()  # App 一啟動就確保表格存在

@app.get("/")
def read_root():
    return {"message": "it works"}

@app.post("/habits")
def create_habit(habit: Habit):
    with Session(engine) as session:
        session.add(habit)
        session.commit()
        session.refresh(habit)  # 存進 DB 後，把 ID 塞回 habit 物件
        return habit
        
@app.get("/habits")
def get_habits():
    with Session(engine) as session:
        result = session.exec(select(Habit)).all()
    return result

@app.post("/habits/{habit_id}/checkin")
def create_checkin(habit_id: int):
    # 檢查今天是否已經打卡過，防止重複打卡
    with Session(engine) as session:
        habit = session.get(Habit, habit_id)
        if not habit:
            return {"message": "Habit not found"}
        existing_checkin = session.exec(select(CheckIn).where(
            CheckIn.habit_id == habit_id, CheckIn.check_date == date.today())).first()
        if existing_checkin:
            return {"message": "already checked in"}
        checkin = CheckIn(habit_id=habit_id, check_date=date.today())
        session.add(checkin)
        session.commit()
        session.refresh(checkin)
        return checkin
        
@app.get("/habits/{habit_id}/streak")
def get_streak(habit_id: int):
    streak = 0
    current_date = date.today()

    with Session(engine) as session:
        checkins = session.exec(select(CheckIn).where(CheckIn.habit_id == habit_id)).all()
        checkin_dates = {c.check_date for c in checkins}
        if current_date not in checkin_dates:
            return streak
        while current_date in checkin_dates:
            streak += 1
            current_date -= timedelta(days=1)
        return streak
        
            