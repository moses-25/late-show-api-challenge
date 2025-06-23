# 🌙 Late Show API

A RESTful Flask API for managing a Late Night TV Show system — complete with guests, episodes, appearances, and authentication.

## 📁 Project Structure

late-show-api-challenge/
├── server/
│ ├── app.py
│ ├── config.py
│ ├── seed.py
│ ├── models/
│ │ ├── init.py
│ │ ├── user.py
│ │ ├── guest.py
│ │ ├── episode.py
│ │ └── appearance.py
│ ├── controllers/
│ │ ├── init.py
│ │ ├── auth_controller.py
│ │ ├── guest_controller.py
│ │ ├── episode_controller.py
│ │ └── appearance_controller.py
├── migrations/
├── challenge-4-lateshow.postman_collection.json
├── README.md

## 🚀 Features

- MVC architecture
- PostgreSQL database
- JWT token-based authentication
- Full CRUD for episodes, guests, and appearances
- Token-protected routes for secure data handling

---

## 🛠 Setup Instructions

### 1. Clone & Navigate

```bash
git clone https://github.com/<your-username>/late-show-api-challenge.git
cd late-show-api-challenge

###Install Dependencies

pipenv install
pipenv shell

##Or with venv:
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

## Create PostgreSQL DB
CREATE DATABASE late_show_db;

##Set Up Configuration
       ##Inside server/config.py:
class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:<your_password>@localhost:5432/late_show_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "your_secret_key"

#📦 Database Setup
export FLASK_APP=server.app:create_app
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python server/seed.py