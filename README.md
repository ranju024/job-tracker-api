

# Job Tracker API

A production-oriented REST API for managing job applications, interviews, application status history, and job search analytics.

Built with Django REST Framework and PostgreSQL.

## Features

- JWT authentication
- User registration and login
- Job application CRUD
- User-specific data isolation
- Application status tracking
- Application status history
- Interview management
- Search and filtering
- Pagination
- Sorting and ordering
- Dashboard analytics
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

Swagger UI:

`/api/docs/`

OpenAPI schema:

`/api/schema/`

ReDoc:

`/api/redoc/`

## Main Endpoints

### Authentication

```text
POST /api/accounts/register/
POST /api/token/
POST /api/token/refresh/
POST /api/accounts/logout/
```



### Job Applications

<pre class="overflow-visible! px-0!" data-start="2279" data-end="2395"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex h-full min-h-0 max-w-full"><div id="d59a034d-48d4-4c4f-969e-57eb68ce8727:8:editor" dir="ltr" class="Rx43rG_codemirror z-10 flex h-full min-h-0 w-full flex-col items-stretch"><div class="cm-editor ͼ1 ͼ2 ͼd ͼr"><div class="cm-announced" aria-live="polite"></div><div tabindex="-1" class="cm-scroller"><div spellcheck="false" autocorrect="off" autocapitalize="off" writingsuggestions="false" translate="no" contenteditable="false" class="cm-content" role="textbox" aria-multiline="true" aria-readonly="true" aria-label="Edit code"><div class="cm-line">GET    /api/jobs/</div><div class="cm-line">POST   /api/jobs/</div><div class="cm-line">GET    /api/jobs/{id}/</div><div class="cm-line">PATCH  /api/jobs/{id}/</div><div class="cm-line">DELETE /api/jobs/{id}/</div></div></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

### Interviews

<pre class="overflow-visible! px-0!" data-start="2413" data-end="2559"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex h-full min-h-0 max-w-full"><div id="d59a034d-48d4-4c4f-969e-57eb68ce8727:9:editor" dir="ltr" class="Rx43rG_codemirror z-10 flex h-full min-h-0 w-full flex-col items-stretch"><div class="cm-editor ͼ1 ͼ2 ͼd ͼr"><div class="cm-announced" aria-live="polite"></div><div tabindex="-1" class="cm-scroller"><div spellcheck="false" autocorrect="off" autocapitalize="off" writingsuggestions="false" translate="no" contenteditable="false" class="cm-content" role="textbox" aria-multiline="true" aria-readonly="true" aria-label="Edit code"><div class="cm-line">GET    /api/interviews/</div><div class="cm-line">POST   /api/interviews/</div><div class="cm-line">GET    /api/interviews/{id}/</div><div class="cm-line">PATCH  /api/interviews/{id}/</div><div class="cm-line">DELETE /api/interviews/{id}/</div></div></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

### Dashboard

<pre class="overflow-visible! px-0!" data-start="2576" data-end="2607"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex h-full min-h-0 max-w-full"><div id="d59a034d-48d4-4c4f-969e-57eb68ce8727:10:editor" dir="ltr" class="Rx43rG_codemirror z-10 flex h-full min-h-0 w-full flex-col items-stretch"><div class="cm-editor ͼ1 ͼ2 ͼd ͼr"><div class="cm-announced" aria-live="polite"></div><div tabindex="-1" class="cm-scroller"><div spellcheck="false" autocorrect="off" autocapitalize="off" writingsuggestions="false" translate="no" contenteditable="false" class="cm-content" role="textbox" aria-multiline="true" aria-readonly="true" aria-label="Edit code"><div class="cm-line">GET /api/dashboard/</div></div></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

### Status History

<pre class="overflow-visible! px-0!" data-start="2629" data-end="2695"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex h-full min-h-0 max-w-full"><div id="d59a034d-48d4-4c4f-969e-57eb68ce8727:11:editor" dir="ltr" class="Rx43rG_codemirror z-10 flex h-full min-h-0 w-full flex-col items-stretch"><div class="cm-editor ͼ1 ͼ2 ͼd ͼr"><div class="cm-announced" aria-live="polite"></div><div tabindex="-1" class="cm-scroller"><div spellcheck="false" autocorrect="off" autocapitalize="off" writingsuggestions="false" translate="no" contenteditable="false" class="cm-content" role="textbox" aria-multiline="true" aria-readonly="true" aria-label="Edit code"><div class="cm-line">GET /api/status-history/</div><div class="cm-line">GET /api/status-history/{id}/</div></div></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

## Filtering

Applications can be filtered and searched using query parameters.

<pre class="overflow-visible! px-0!" data-start="2778" data-end="2990"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex h-full min-h-0 max-w-full"><div id="d59a034d-48d4-4c4f-969e-57eb68ce8727:12:editor" dir="ltr" class="Rx43rG_codemirror z-10 flex h-full min-h-0 w-full flex-col items-stretch"><div class="cm-editor ͼ1 ͼ2 ͼd ͼr"><div class="cm-announced" aria-live="polite"></div><div tabindex="-1" class="cm-scroller"><div spellcheck="false" autocorrect="off" autocapitalize="off" writingsuggestions="false" translate="no" contenteditable="false" class="cm-content" role="textbox" aria-multiline="true" aria-readonly="true" aria-label="Edit code"><div class="cm-line">GET /api/jobs/?status=interviewing</div><div class="cm-line">GET /api/jobs/?company=Google</div><div class="cm-line">GET /api/jobs/?location=Kathmandu</div><div class="cm-line">GET /api/jobs/?work_type=remote</div><div class="cm-line">GET /api/jobs/?search=developer</div><div class="cm-line">GET /api/jobs/?ordering=-date_applied</div></div></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

## Pagination

<pre class="overflow-visible! px-0!" data-start="3007" data-end="3068"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex h-full min-h-0 max-w-full"><div id="d59a034d-48d4-4c4f-969e-57eb68ce8727:13:editor" dir="ltr" class="Rx43rG_codemirror z-10 flex h-full min-h-0 w-full flex-col items-stretch"><div class="cm-editor ͼ1 ͼ2 ͼd ͼr"><div class="cm-announced" aria-live="polite"></div><div tabindex="-1" class="cm-scroller"><div spellcheck="false" autocorrect="off" autocapitalize="off" writingsuggestions="false" translate="no" contenteditable="false" class="cm-content" role="textbox" aria-multiline="true" aria-readonly="true" aria-label="Edit code"><div class="cm-line">GET /api/jobs/?page=2</div><div class="cm-line">GET /api/jobs/?page_size=20</div></div></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

Maximum page size is 50.

## Application Statuses

<pre class="overflow-visible! px-0!" data-start="3121" data-end="3198"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex h-full min-h-0 max-w-full"><div id="d59a034d-48d4-4c4f-969e-57eb68ce8727:14:editor" dir="ltr" class="Rx43rG_codemirror z-10 flex h-full min-h-0 w-full flex-col items-stretch"><div class="cm-editor ͼ1 ͼ2 ͼd ͼr"><div class="cm-announced" aria-live="polite"></div><div tabindex="-1" class="cm-scroller"><div spellcheck="false" autocorrect="off" autocapitalize="off" writingsuggestions="false" translate="no" contenteditable="false" class="cm-content" role="textbox" aria-multiline="true" aria-readonly="true" aria-label="Edit code"><div class="cm-line">Applied</div><div class="cm-line">Screening</div><div class="cm-line">Interviewing</div><div class="cm-line">Offered</div><div class="cm-line">Rejected</div><div class="cm-line">Ghosted</div><div class="cm-line">Withdrawn</div></div></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

## Project Structure

<pre class="overflow-visible! px-0!" data-start="3222" data-end="3565"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex h-full min-h-0 max-w-full"><div id="d59a034d-48d4-4c4f-969e-57eb68ce8727:15:editor" dir="ltr" class="Rx43rG_codemirror z-10 flex h-full min-h-0 w-full flex-col items-stretch"><div class="cm-editor ͼ1 ͼ2 ͼd ͼr"><div class="cm-announced" aria-live="polite"></div><div tabindex="-1" class="cm-scroller"><div spellcheck="false" autocorrect="off" autocapitalize="off" writingsuggestions="false" translate="no" contenteditable="false" class="cm-content" role="textbox" aria-multiline="true" aria-readonly="true" aria-label="Edit code"><div class="cm-line">job-tracker/</div><div class="cm-line">├── accounts/</div><div class="cm-line">│   ├── models.py</div><div class="cm-line">│   ├── serializers.py</div><div class="cm-line">│   ├── views.py</div><div class="cm-line">│   └── urls.py</div><div class="cm-line">│</div><div class="cm-line">├── jobs/</div><div class="cm-line">│   ├── models.py</div><div class="cm-line">│   ├── serializers.py</div><div class="cm-line">│   ├── views.py</div><div class="cm-line">│   ├── pagination.py</div><div class="cm-line">│   ├── urls.py</div><div class="cm-line">│   └── tests/</div><div class="cm-line">│</div><div class="cm-line">├── jobtracker/</div><div class="cm-line">│   ├── settings.py</div><div class="cm-line">│   └── urls.py</div><div class="cm-line">│</div><div class="cm-line">├── manage.py</div><div class="cm-line">├── requirements.txt</div><div class="cm-line">└── .env.example</div></div></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

## Setup

Clone the repository and create a virtual environment:

<pre class="overflow-visible! px-0!" data-start="3633" data-end="3664"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex h-full min-h-0 max-w-full"><div id="d59a034d-48d4-4c4f-969e-57eb68ce8727:16:editor" dir="ltr" class="Rx43rG_codemirror z-10 flex h-full min-h-0 w-full flex-col items-stretch"><div class="cm-editor ͼ1 ͼ2 ͼd ͼr"><div class="cm-announced" aria-live="polite"></div><div tabindex="-1" class="cm-scroller"><div spellcheck="false" autocorrect="off" autocapitalize="off" writingsuggestions="false" translate="no" contenteditable="false" class="cm-content" role="textbox" aria-multiline="true" aria-readonly="true" aria-label="Edit code" data-language="shell"><div class="cm-line">python <span class="ͼn">-m</span> venv venv</div></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></div></div></pre>

Activate the environment.

Windows:

<pre class="overflow-visible! px-0!" data-start="3703" data-end="3736"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex h-full min-h-0 max-w-full"><div id="d59a034d-48d4-4c4f-969e-57eb68ce8727:17:editor" dir="ltr" class="Rx43rG_codemirror z-10 flex h-full min-h-0 w-full flex-col items-stretch"><div class="cm-editor ͼ1 ͼ2 ͼd ͼr"><div class="cm-announced" aria-live="polite"></div><div tabindex="-1" class="cm-scroller"><div spellcheck="false" autocorrect="off" autocapitalize="off" writingsuggestions="false" translate="no" contenteditable="false" class="cm-content" role="textbox" aria-multiline="true" aria-readonly="true" aria-label="Edit code" data-language="shell"><div class="cm-line">venv\Scripts\activate</div></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></div></div></pre>

Install dependencies:

<pre class="overflow-visible! px-0!" data-start="3761" data-end="3804"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex h-full min-h-0 max-w-full"><div id="d59a034d-48d4-4c4f-969e-57eb68ce8727:18:editor" dir="ltr" class="Rx43rG_codemirror z-10 flex h-full min-h-0 w-full flex-col items-stretch"><div class="cm-editor ͼ1 ͼ2 ͼd ͼr"><div class="cm-announced" aria-live="polite"></div><div tabindex="-1" class="cm-scroller"><div spellcheck="false" autocorrect="off" autocapitalize="off" writingsuggestions="false" translate="no" contenteditable="false" class="cm-content" role="textbox" aria-multiline="true" aria-readonly="true" aria-label="Edit code" data-language="shell"><div class="cm-line">pip install <span class="ͼn">-r</span> requirements.txt</div></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></div></div></pre>

Create a `.env` file using `.env.example` and configure the PostgreSQL database.

Run migrations:

<pre class="overflow-visible! px-0!" data-start="3905" data-end="3941"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex h-full min-h-0 max-w-full"><div id="d59a034d-48d4-4c4f-969e-57eb68ce8727:19:editor" dir="ltr" class="Rx43rG_codemirror z-10 flex h-full min-h-0 w-full flex-col items-stretch"><div class="cm-editor ͼ1 ͼ2 ͼd ͼr"><div class="cm-announced" aria-live="polite"></div><div tabindex="-1" class="cm-scroller"><div spellcheck="false" autocorrect="off" autocapitalize="off" writingsuggestions="false" translate="no" contenteditable="false" class="cm-content" role="textbox" aria-multiline="true" aria-readonly="true" aria-label="Edit code" data-language="shell"><div class="cm-line">python manage.py migrate</div></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></div></div></pre>

Start the development server:

<pre class="overflow-visible! px-0!" data-start="3974" data-end="4012"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex h-full min-h-0 max-w-full"><div id="d59a034d-48d4-4c4f-969e-57eb68ce8727:20:editor" dir="ltr" class="Rx43rG_codemirror z-10 flex h-full min-h-0 w-full flex-col items-stretch"><div class="cm-editor ͼ1 ͼ2 ͼd ͼr"><div class="cm-announced" aria-live="polite"></div><div tabindex="-1" class="cm-scroller"><div spellcheck="false" autocorrect="off" autocapitalize="off" writingsuggestions="false" translate="no" contenteditable="false" class="cm-content" role="textbox" aria-multiline="true" aria-readonly="true" aria-label="Edit code" data-language="shell"><div class="cm-line">python manage.py runserver</div></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></div></div></pre>

## Testing

Run the complete test suite:

<pre class="overflow-visible! px-0!" data-start="4056" data-end="4089"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="relative h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class=""><div class="relative"><div class=""><div class="relative z-0 flex h-full min-h-0 max-w-full"><div id="d59a034d-48d4-4c4f-969e-57eb68ce8727:21:editor" dir="ltr" class="Rx43rG_codemirror z-10 flex h-full min-h-0 w-full flex-col items-stretch"><div class="cm-editor ͼ1 ͼ2 ͼd ͼr"><div class="cm-announced" aria-live="polite"></div><div tabindex="-1" class="cm-scroller"><div spellcheck="false" autocorrect="off" autocapitalize="off" writingsuggestions="false" translate="no" contenteditable="false" class="cm-content" role="textbox" aria-multiline="true" aria-readonly="true" aria-label="Edit code" data-language="shell"><div class="cm-line">python manage.py test</div></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></div></div></pre>

The test suite covers:

* Authentication requirements
* Job CRUD
* User data isolation
* Status history
* Search and filtering
* Interview creation
* Dashboard statistics

## Security

Authentication uses JWT access and refresh tokens.

Users can only access their own job applications, interviews, and status history.

Environment variables are used for database credentials and secret configuration.

## Future Improvements

* Email reminders for interviews and follow-ups
* Resume and cover letter management
* Application activity timeline
* Celery-based background tasks
* Production deployment
