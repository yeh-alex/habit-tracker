# 終端機 A(後端)
cd D:\dev\habit-tracker
venv\Scripts\activate
uvicorn main:app --reload

# 終端機 B(前端,另開一個)
cd D:\dev\habit-tracker\frontend
python -m http.server 5500

# 瀏覽器開 http://localhost:5500

git add .
git commit -m "說明這次做了什麼"
git push