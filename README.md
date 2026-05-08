# Job Tracker API

A REST API for tracking job applications built with Django, DRF, PostgreSQL, and JWT authentication.

## Tech Stack

- Django + Django REST Framework
- PostgreSQL
- JWT Authentication (simplejwt)

## Setup

1. Clone the repo
2. Create a virtual environment and activate it
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and fill in your values
5. Run migrations: `python manage.py migrate`
6. Start the server: `python manage.py runserver`

## API Endpoints

### Auth

- POST `/api/accounts/register/`
- POST `/api/accounts/login/`
- POST `/api/accounts/token/refresh/`

### Job Applications

- GET `/api/jobs/`
- POST `/api/jobs/`
- GET `/api/jobs/{id}/`
- PUT `/api/jobs/{id}/`
- PATCH `/api/jobs/{id}/`
- DELETE `/api/jobs/{id}/`
