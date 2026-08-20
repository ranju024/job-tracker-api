# Job Tracker API

A REST API for managing job applications, interviews, application status history, and job search analytics.

Built with Django REST Framework and PostgreSQL.

**Frontend repo:** [job-tracker-client](https://github.com/ranju024/job-tracker-client)

## Features

- JWT authentication (register, login, refresh, logout)
- Job application CRUD, scoped to the authenticated user
- Application status tracking with automatic status history
- Interview scheduling per application (type, date/time, meeting link, location, notes)
- Search and filtering, including a dedicated "active applications" filter and an
  "applications with an upcoming interview" filter
- Pagination, sorting and ordering
- Dashboard analytics (totals, active count, offers, rejected, response rate,
  upcoming interviews, stale applications)
- Salary range tracking
- OpenAPI / Swagger documentation
- Automated API tests
- PostgreSQL database

## Tech Stack

- Python 3.13
- Django 5.2
- Django REST Framework
- PostgreSQL
- SimpleJWT
- drf-spectacular
- Gunicorn
- WhiteNoise

## API Documentation

- Swagger UI: `/api/docs/`
- OpenAPI schema: `/api/schema/`
- ReDoc: `/api/redoc/`

## Main Endpoints

### Authentication

```
POST /api/accounts/register/
POST /api/accounts/login/
POST /api/accounts/token/refresh/
POST /api/accounts/logout/
```

### Job Applications

```
GET    /api/jobs/
POST   /api/jobs/
GET    /api/jobs/{id}/
PATCH  /api/jobs/{id}/
DELETE /api/jobs/{id}/
```

### Interviews

```
GET    /api/interviews/
POST   /api/interviews/
GET    /api/interviews/{id}/
PATCH  /api/interviews/{id}/
DELETE /api/interviews/{id}/
```

### Dashboard

```
GET /api/dashboard/
```

Returns `total_applications`, `active_applications`, `interviews`, `offers`,
`rejected`, `response_rate`, `by_status`, `upcoming_interviews`, and
`stale_applications`.

### Status History

```
GET /api/status-history/
GET /api/status-history/{id}/
```

## Filtering

Applications can be filtered and searched using query parameters:

```
GET /api/jobs/?status=interviewing
GET /api/jobs/?status=active
GET /api/jobs/?upcoming_interview=true
GET /api/jobs/?stale=true
GET /api/jobs/?company=Google
GET /api/jobs/?location=Kathmandu
GET /api/jobs/?work_type=remote
GET /api/jobs/?search=developer
GET /api/jobs/?ordering=-date_applied
```

- `status=active` matches every status except Offered, Rejected, Ghosted, and
  Withdrawn. This is the same definition the dashboard uses for "active applications".
- `upcoming_interview=true` returns only applications that have at least one
  interview scheduled in the future, and excludes applications whose status is
  Rejected, Withdrawn, or Ghosted (a stale interview on a closed-out
  application doesn't count as "upcoming").
- `stale=true` returns applications still in an active status (Applied,
  Screening, or Interviewing) that haven't been updated in 15+ days. This is the
  same "needing attention" list shown on the dashboard.

## Pagination

```
GET /api/jobs/?page=2
GET /api/jobs/?page_size=20
```

Maximum page size is 50.

## Application Statuses

- Applied
- Screening
- Interviewing
- Offered
- Rejected
- Ghosted
- Withdrawn

## Project Structure

```
job-tracker-api/
├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── jobs/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── pagination.py
│   ├── urls.py
│   └── tests/
│
├── jobtracker/
│   ├── settings.py
│   └── urls.py
│
├── manage.py
├── requirements.txt
└── .env.example
```

## Setup

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/ranju024/job-tracker-api.git
cd job-tracker-api
python -m venv venv
```

Activate the environment.

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file using `.env.example` and configure the PostgreSQL
database and secret key.

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

## Testing

Run the complete test suite:

```bash
python manage.py test
```

The test suite covers:

- Authentication requirements
- Job CRUD
- User data isolation
- Status history
- Search and filtering
- Interview creation
- Dashboard statistics

## Security

- Authentication uses JWT access and refresh tokens.
- Users can only access their own job applications, interviews, and status
  history.
- Environment variables are used for database credentials and secret
  configuration.

## Future Improvements

- Email reminders for interviews and follow-ups
- Resume and cover letter management
- Application activity timeline
- Celery-based background tasks
- Production deployment hardening
