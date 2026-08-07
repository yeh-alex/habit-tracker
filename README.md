# Habit Tracker API

A backend API for tracking daily habits and check-in streaks, built with FastAPI and SQLModel.

## Features

- Create and manage habits
- Daily check-ins with duplicate prevention
- Automatic streak calculation (consecutive check-in days)
- Input validation (rejects check-ins for non-existent habits)

## Tech Stack

- **FastAPI** – web framework
- **SQLModel** – ORM (built on SQLAlchemy + Pydantic)
- **SQLite** – database

## Getting Started

### Prerequisites
- Python 3.10+

### Installation

```bash
# Clone the repository
git clone https://github.com/yeh-alex/habit-tracker.git
cd habit-tracker

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate # macOS/Linux

# Install dependencies
pip install fastapi uvicorn sqlmodel
```

### Running the app

```bash
uvicorn main:app --reload
```

Then open http://localhost:8000/docs to explore the API via Swagger UI.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/habits` | Create a new habit |
| GET | `/habits` | List all habits |
| POST | `/habits/{habit_id}/checkin` | Check in for a habit today |
| GET | `/habits/{habit_id}/streak` | Get current streak for a habit |

## Roadmap

- Get / update / delete individual habits
- Check-in history endpoint
- Frontend (Vue / React)