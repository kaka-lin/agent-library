---
name: analyzing-fastapi-projects
description: Provides a structured workflow to analyze FastAPI codebases, understand architecture, pipelines, dependencies, and development workflows. Intended for onboarding, audits, and answering “how does this FastAPI app work?”
---

# Analyzing FastAPI Projects

This document defines a **systematic workflow** for analyzing an existing FastAPI application.
It focuses on understanding **structure, tech stack, execution pipeline, and conventions**, rather than writing new features.

Use this when:

- Onboarding to an unfamiliar FastAPI codebase
- Reviewing or auditing an existing backend
- Answering questions like:
  - “How does this FastAPI app work?”
  - “Where does a request flow through the system?”
  - “What is the overall architecture?”

---

## Project Analysis Checklist

```
- [ ] Step 1: Repository & README overview
- [ ] Step 2: Dependency & tech stack analysis
- [ ] Step 3: Project structure mapping
- [ ] Step 4: Application startup & execution pipeline
- [ ] Step 5: API layer & dependency graph
- [ ] Step 6: Data & external integrations
- [ ] Step 7: Development & deployment workflow
- [ ] Step 8: Generate analysis report
```

---

## Step 1: Repository & README Overview

### Goals

- Understand the project purpose and scope
- Identify entry points and supported workflows

### Actions

```bash
ls -la
cat README.md 2>/dev/null | head -100
```

### Look For

- Project description and high-level architecture
- Local development instructions
- Environment variables and configuration notes
- References to background workers, queues, or schedulers

---

## Step 2: Dependency & Tech Stack Analysis

### Python Dependencies

Inspect one of the following:

- `pyproject.toml`
- `requirements.txt`
- `requirements/*.txt`

```bash
cat requirements.txt
```

### Identify

- **Web framework**: FastAPI, Starlette
- **ASGI server**: Uvicorn, Hypercorn, Gunicorn
- **Validation**: Pydantic (v1 vs v2)
- **Database**: SQLAlchemy, asyncpg, psycopg
- **Auth**: OAuth2, JWT libraries
- **Infra**: Redis, Celery, RQ
- **Testing**: pytest, pytest-asyncio, httpx

### Validation

- Python version requirement
- Async-first vs sync-heavy stack

---

## Step 3: Project Structure Mapping

### Goal

Build a mental map of the codebase.

### Output Format (example)

```
app/
├── main.py            # FastAPI app creation
├── server.py          # ASGI entry / startup logic
├── api/               # Route definitions
│   ├── v1/
│   │   ├── users.py   # User-related endpoints
│   │   └── health.py
├── core/              # Settings, security, lifespan
├── db/                # Database engine & sessions
├── models/            # SQLAlchemy models
├── schemas/           # Pydantic schemas
├── services/          # Business logic
└── tests/
```

### Validation

- Clear separation between API, domain logic, and infrastructure
- No business logic embedded directly in route handlers

---

## Step 4: Application Startup & Execution Pipeline

### Goal

Understand **how the app boots and runs**.

### Trace the Startup Path

Common patterns:

```
server.py
  ↓
create_app() / FastAPI()
  ↓
lifespan startup
  ↓
router registration
  ↓
uvicorn / gunicorn worker
```

### Inspect

- `main.py` / `server.py`
- `FastAPI(lifespan=...)`
- Startup initialization:
  - Database engine
  - Redis clients
  - Background workers

### Validation

- Startup logic is centralized
- No heavy logic executed at import time

---

## Step 5: API Layer & Request Pipeline

### Goal

Understand **how a request flows**.

### Typical Request Flow

```
HTTP request
 → APIRouter
 → Dependency injection (Depends)
 → Service / domain logic
 → Database / external calls
 → Response model
```

### Inspect

- `APIRouter` usage
- Dependency graph (auth, DB session, settings)
- Error handling and exception middleware

### Validation

- Dependencies are reusable and composable
- Authentication & authorization handled via dependencies

---

## Step 6: Data Layer & External Integrations

### Inspect

- Database session lifecycle
- Transaction boundaries
- External services:
  - HTTP APIs
  - Message queues
  - Object storage

### Validation

- Clear async vs sync boundaries
- External clients initialized once and reused

---

## Step 7: Development & Deployment Workflow

### Check For

- `Dockerfile`, `docker-compose.yml`
- `.env.example`
- CI workflows (`.github/workflows/`)
- Migration commands (Alembic)

### Typical Commands

```bash
uvicorn app.main:app --reload
pytest
alembic upgrade head
```

### Validation

- Development workflow is documented and reproducible
- Environment variables are explicit

---

## Step 8: Analysis Report Output

### Required Output Format

```markdown
# FastAPI Project Analysis: [Project Name]

## Overview
[1–2 sentence description of what the service does]

## Tech Stack
| Category | Technology |
|----------|------------|
| Language | Python |
| Framework | FastAPI |
| Server | Uvicorn |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Cache | Redis |

## Application Pipeline

server.py
 → FastAPI app creation
 → lifespan startup
 → router registration
 → request handling

## Key Directories

- `app/api/` - HTTP endpoints
- `app/services/` - Business logic
- `app/db/` - Database access
- `app/core/` - Configuration & security

## Request Flow

[Short explanation of request → response path]

## Development Commands

| Action | Command |
|------|---------|
| Run | `uvicorn app.main:app --reload` |
| Test | `pytest` |
| Migrate | `alembic upgrade head` |

## Open Questions

- [Anything unclear or requiring clarification]

---

## Final Validation Checklist

- [ ] README fully reviewed
- [ ] Dependencies understood
- [ ] Startup & request pipelines traced
- [ ] Major directories explained
- [ ] No assumptions made without code evidence
```
