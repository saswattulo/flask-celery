# Flask-RESTful API with SQLite and Gunicorn

This is a production-ready REST API built using **Flask**, **Flask-RESTful**, **Flask-SQLAlchemy**, and **Flask-Migrate**. The API provides CRUD operations for user management and uses **SQLite** as the database.

## 🚀 Features
- CRUD operations for users
- Flask Blueprints for modular API structure
- Database migrations using Flask-Migrate
- Production-ready with **Gunicorn**
- Uses **SQLite** as the database

## 📂 Project Structure
```
Flask-Celery/
│── app/
│   ├── __init__.py       # Application factory (create_app)
│   ├── config.py         # Database configuration
│   ├── models.py         # SQLAlchemy models (User model)
│   ├── extensions.py     # Extensions like db, migrate
│   ├── api/
│   │   ├── __init__.py   # Blueprint & API instance
│   │   ├── user.py       # User resource (CRUD operations)
│   ├── migrations/       # Flask-Migrate migrations
│   ├── routes.py         # Route registration
│── .venv/                # Virtual environment (excluded from Git)
│── database.db           # SQLite database file
│── requirements.txt      # Python dependencies
│── README.md             # Project documentation
│── run.py                # Entry point (alternative to Gunicorn)
│── wsgi.py               # WSGI entry point for Gunicorn
```

## 🛠️ Setup & Installation
### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-repo/flask-crud-api.git
cd flask-crud-api
```

### 2️⃣ Create a virtual environment & install dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate  # (On Windows, use `.venv\Scripts\activate`)
pip install -r requirements.txt
```

### 3️⃣ Initialize and Migrate the Database
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 4️⃣ Run the Application
#### Development Mode
```bash
flask run --debug
```

#### Production Mode (Using Gunicorn)
```bash
gunicorn -w 4 -b 0.0.0.0:5000 "app:create_app()"
```

## 📌 API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET    | `/api/users` | Get all users |
| POST   | `/api/users` | Create a new user |
| GET    | `/api/users/<user_id>` | Get a user by ID |
| PUT    | `/api/users/<user_id>` | Update a user by ID |
| DELETE | `/api/users/<user_id>` | Delete a user by ID |

## 🛠️ Example Requests (cURL)
### Get all users
```bash
curl -X GET http://127.0.0.1:5000/api/users
```

### Create a new user
```bash
curl -X POST http://127.0.0.1:5000/api/users \
     -H "Content-Type: application/json" \
     -d '{"name": "John Doe", "email": "john@example.com"}'
```

### Update a user
```bash
curl -X PUT http://127.0.0.1:5000/api/users/1 \
     -H "Content-Type: application/json" \
     -d '{"name": "John Updated", "email": "john.new@example.com"}'
```

### Delete a user
```bash
curl -X DELETE http://127.0.0.1:5000/api/users/1
```

## 🎯 License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

---
### 🚀 Happy Coding! Let me know if you need further improvements! 🔥

