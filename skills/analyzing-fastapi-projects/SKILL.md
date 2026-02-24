---
name: analyzing-fastapi-projects
description: Provides a structured approach and domain knowledge for analyzing FastAPI codebases, including request pipelines, architectures, and development workflows.
---

# Analyzing FastAPI Projects

This skill provides the **domain knowledge and best practices** for analyzing an existing FastAPI application. 
Use this skill when you are asked to understand, audit, or review a FastAPI codebase. Unlike a rigid workflow, use this knowledge to flexibly adapt to the specific codebase and the user's questions.

## 🎯 Goal

Understand the **structure, tech stack, execution pipeline, and conventions** of a FastAPI application to accurately answer questions like:

- “How does this FastAPI app work?”
- “Where does a request flow through the system?”
- “What is the overall architecture?”

## 🧠 Domain Knowledge & Analysis Guidelines

When analyzing a FastAPI project, maintain focus on the following key areas:

### 1. Identify the Tech Stack & Dependencies

Look in `pyproject.toml`, `requirements.txt`, etc.

- **Web framework / Server**: FastAPI, Uvicorn, Gunicorn
- **Validation**: Pydantic (v1 vs v2 is a critical distinction)
- **Database / ORM**: SQLAlchemy, asyncpg, psycopg
- **Infra/Background**: Redis, Celery, RQ

### 2. Map the Project Structure

A standard and well-structured FastAPI app usually separates concerns:

- `main.py` / `server.py`: FastAPI app creation & entry point.
- `api/` or `routers/`: Route definitions.
- `core/`: Settings, security, lifespan.
- `db/` or `database/`: Database engine & sessions.
- `models/`: SQLAlchemy models (data layer).
- `schemas/`: Pydantic schemas (validation layer).
- `services/` or `crud/`: Business logic.

*Best Practice Check:* Ensure business logic isn't embedded directly in route handlers!

### 3. Trace the Execution Pipeline

Understand how the app boots:

1. Entry point (`FastAPI()` instantiation)
2. `lifespan` startup events (DB initialization, background workers)
3. Router registration (`app.include_router()`)

### 4. Trace the Request Flow

Understand how a typical HTTP request flows:
`APIRouter` → `Dependency Injection (Depends)` → `Service/Domain Logic` → `Database` → `Response Model`

*Best Practice Check:* Are authentication and DB sessions properly handled via FastAPI Dependencies (`Depends`)?

### 5. Data Layer & Integrations

- Identify database session lifecycles and transaction boundaries.
- Identify where external API calls or message queues are used.

## 📝 Best Practices for Reporting

When asked to generate a report or summary of the FastAPI project, synthesize your findings into a professional overview.
Your report should ideally cover:

1. **Overview & Tech Stack**: What does the service do and what powers it?
2. **Application Pipeline & Request Flow**: How does it start up? How does a request get processed?
3. **Key Directories & Architecture**: Where is everything located?
4. **Actionable Commands**: How to run it locally (`uvicorn`), test it (`pytest`), and migrate the database (`alembic`).
5. **Insights / Red Flags**: Point out any anti-patterns (e.g. sync calls in async routes, fat routers).
