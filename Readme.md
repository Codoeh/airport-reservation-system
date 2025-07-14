# ✈️ Airport Reservation System

A REST API for managing flights, tickets, orders, and more.  
Built with Django, Django REST Framework, JWT authentication, and Docker.

![Python](https://img.shields.io/badge/python-3.11-blue)
![Django](https://img.shields.io/badge/django-4.2-green)

---

## 🚀 Features

- ✅ JWT authentication (registration & login)
- ✈️ Management of:
  - Airplanes & airplane types
  - Airports & flight routes
  - Flights
  - Crew members
  - Tickets (read-only)
  - Orders (with multiple tickets)
- 🔍 Filtering with `django-filter`
- 🔁 Many-to-many relations (e.g. crew ↔ flights)
- 💡 Query optimization with `select_related` & `prefetch_related`
- 🔢 Pagination at each endpoint
- 📄 Auto-generated Swagger and Redoc API documentation

---

## 📦 Functionality Overview

### ✅ Core Capabilities

- User registration and JWT authentication
- Flight and ticket booking system
- Multiple tickets in a single order
- Dynamic seat availability validation
- Crew assignment to flights
- Flight filtering by date, airplane type, route, crew, etc.

### 🔧 Technical Extras

- Optimized DB queries to prevent N+1 problem
- Atomic transactions for safe order creation
- Separate serializers for different views (List, Detail, Simple)
- Custom filters using `django_filters`
- Full API documentation via Swagger UI and Redoc

---

## ⚙️ Requirements

- Python 3.11

---

## 🛠️ Local Installation

```bash
git clone https://github.com/Codoeh/airport-reservation-system.git
cd airport-reservation-system
python -m venv venv

# On Linux / macOS
source venv/bin/activate
# On Windows (CMD)
venv\Scripts\activate.bat
# On Windows (PowerShell)
venv\Scripts\Activate.ps1
# Installation for production
pip install -r requirements.txt
# Installation for development
pip install -r requirements.txt -r requirements-dev.txt
```

### 🔐 Create a `.env` file

```bash
cp .env.sample .env
```

> 💡 Generate a Django secret key:
> ```bash
> python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
> ```

### 🔄 Migrate and run the project

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 🐳 Running with Docker

```bash
# 🔧 For production (only required packages):
docker-compose build --build-arg INSTALL_DEV=false

# 🧪 For development (adds testing & linting tools):
docker-compose build --build-arg INSTALL_DEV=true
```

Once started, the app will be available at:

- 🏠 Main: [http://localhost:8000](http://localhost:8000)
- 📘 Swagger: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)
- 📙 Redoc: [http://localhost:8000/api/redoc/](http://localhost:8000/api/redoc/)

---

## 🔐 Authentication

- Register: `POST /api/auth/registration/`
- Login (JWT): `POST /api/token/`

## 📚 API Documentation

Auto-generated docs available after running the server:

- Swagger UI: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)
- Redoc: [http://localhost:8000/api/redoc/](http://localhost:8000/api/redoc/)

---

## 🧪 Testing

```bash
pip install pytest pytest-django
```

The following tests are recommended:

- ✅ **Model tests**: e.g. airplane seat calculation
- ✅ **Serializer validation tests**
- ✅ **Endpoint tests**: List, Create, Detail
- ✅ **Integration tests**: Full order with ticket reservation

> Test framework: `pytest`  
> To run: `pytest`
