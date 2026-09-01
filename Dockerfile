# ① 用官方的 Python 3.12 當基底環境(等於「一台裝好 Python 的乾淨電腦」)
FROM python:3.12-slim

# ② 在容器裡設一個工作資料夾
WORKDIR /app

# ③ 先把套件清單複製進去,然後安裝(先裝套件有個好處,之後解釋)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ④ 把你的 code 複製進容器
COPY . .

# ⑤ 開放 8000 這個 port(你的 API 跑在這)
EXPOSE 8000

# ⑥ 容器啟動時,執行這個指令跑起你的 API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]