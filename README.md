# Habit Tracker

A full-stack habit tracking app with daily check-ins and streak calculation. Built with FastAPI (backend) and Vue (frontend).

## Features

- Create, view, update, and delete habits (full CRUD)
- Daily check-ins with duplicate prevention
- Automatic streak calculation (consecutive check-in days)
- Cascade delete (removes a habit's check-ins along with it)
- Vue frontend to manage habits in the browser

## Tech Stack

**Backend**
- FastAPI – web framework
- SQLModel – ORM (SQLAlchemy + Pydantic)
- SQLite – database

**Frontend**
- Vue 3 (via CDN)

## Getting Started

### Prerequisites
- Python 3.10+

### Backend setup

```bash
cd habit-tracker
python -m venv venv
venv\Scripts\activate      # Windows
pip install fastapi uvicorn sqlmodel
uvicorn main:app --reload
```

Backend runs at http://localhost:8000 (API docs at /docs).

### Frontend setup

In a separate terminal:

```bash
cd frontend
python -m http.server 5500
```

Open http://localhost:5500 in your browser.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/habits` | Create a habit |
| GET | `/habits` | List all habits |
| GET | `/habits/{id}` | Get a single habit |
| PUT | `/habits/{id}` | Update a habit |
| DELETE | `/habits/{id}` | Delete a habit (and its check-ins) |
| POST | `/habits/{id}/checkin` | Check in for today |
| GET | `/habits/{id}/streak` | Get current streak |

## Roadmap

- Display streaks in the frontend
- Styling improvements
- Check-in history view