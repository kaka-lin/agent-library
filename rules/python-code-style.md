---
name: python-code-style
description: Python code style — linting, formatting, naming conventions, and documentation standards
activation: model_decision
---

# Python Code Style & Documentation

Consistent code style and clear documentation make codebases maintainable and collaborative. This rule covers modern Python tooling, naming conventions, type annotations, and documentation standards.

**Apply when:** writing, reviewing, or refactoring Python code.

## 1. Automated Tooling

### 1.1 Ruff — All-in-One Linter & Formatter

Use **ruff** as the single tool for linting and formatting. It replaces
`flake8`, `isort`, and `black` with superior performance.

```toml
# pyproject.toml
[tool.ruff]
line-length = 100
target-version = "py310"  # Adjust to your project's minimum Python version

[tool.ruff.lint]
select = [
    "E",    # pycodestyle errors
    "W",    # pycodestyle warnings
    "F",    # pyflakes
    "I",    # isort (import sorting)
    "B",    # flake8-bugbear
    "C4",   # flake8-comprehensions
    "UP",   # pyupgrade
    "SIM",  # flake8-simplify
    "RUF",  # ruff-specific rules
    "D",    # pydocstyle (enforces docstring conventions)
]
ignore = ["E501"]  # Line length handled by formatter

[tool.ruff.lint.pydocstyle]
convention = "google"  # Enforce Google-style docstrings

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
```

```bash
# Usage
ruff check --fix .   # Lint and auto-fix
ruff format .        # Format code
```

### 1.2 Type Checking — mypy or pyright

Enable **strict** type checking for production code.

**mypy:**

```toml
# pyproject.toml
[tool.mypy]
python_version = "3.10"
strict = true
warn_return_any = true
warn_unused_ignores = true
disallow_untyped_defs = true
disallow_incomplete_defs = true

[[tool.mypy.overrides]]
module = "tests.*"
disallow_untyped_defs = false
```

**pyright (alternative — faster):**

```toml
# pyproject.toml
[tool.pyright]
pythonVersion = "3.10"
typeCheckingMode = "strict"
```

## 2. Naming Conventions (PEP 8)

Use **descriptive** names — clarity always beats brevity.

| Element             | Style                  | Example                |
| ------------------- | ---------------------- | ---------------------- |
| Modules / files     | `snake_case`           | `user_repository.py`   |
| Classes             | `PascalCase`           | `UserRepository`       |
| Functions / methods | `snake_case`           | `get_user_by_email()`  |
| Variables           | `snake_case`           | `retry_count`          |
| Constants           | `SCREAMING_SNAKE_CASE` | `MAX_RETRY_ATTEMPTS`   |
| Type variables      | `PascalCase`           | `T`, `ResponseT`       |
| Private members     | `_leading_underscore`  | `_internal_cache`      |
| Acronyms in classes | Keep uppercase         | `HTTPClientFactory`    |

```python
# Constants — module-level, SCREAMING_SNAKE_CASE
MAX_RETRY_ATTEMPTS = 3
DEFAULT_TIMEOUT_SECONDS = 30
API_BASE_URL = "https://api.example.com"


class HTTPClientFactory:
    """Factory for creating configured HTTP clients."""

    def create_client(self, timeout: int = DEFAULT_TIMEOUT_SECONDS) -> httpx.Client:
        """Create and return a new HTTP client instance."""
        ...
```

## 3. Import Organization

Group imports in three blocks, separated by blank lines, in this order:

1. **Standard library**
2. **Third-party packages**
3. **Local / project imports**

```python
# 1. Standard library
import os
from collections.abc import Callable
from typing import Any

# 2. Third-party packages
import httpx
from pydantic import BaseModel
from sqlalchemy import Column

# 3. Local imports
from myproject.models import User
from myproject.services import UserService
```

**Rules:**

- Always use **absolute imports** (avoid relative imports like `from ..utils`).
- Let `ruff` handle import sorting automatically (`I` rule enabled).
- Define `__all__` in modules that serve as public APIs to explicitly control
  exported names. This improves clarity and prevents internal symbols from
  leaking.

```python
# myproject/models/__init__.py
__all__ = ["User", "UserRole", "Permission"]

from myproject.models.permission import Permission
from myproject.models.user import User, UserRole
```

## 4. Type Annotations

Modern Python code **must** include type hints for all public APIs.

```python
# Function signatures — always annotate parameters and return types
def get_user(user_id: str) -> User | None:
    """Retrieve a user by their unique identifier."""
    ...


# Use collections.abc for abstract types (Python 3.9+)
from collections.abc import Callable, Sequence


def process_items(
    items: Sequence[Item],
    callback: Callable[[Item], bool] | None = None,
) -> list[Item]:
    ...


# Use built-in generics (Python 3.10+): list, dict, tuple, set
def merge_configs(base: dict[str, Any], overrides: dict[str, Any]) -> dict[str, Any]:
    ...
```

**Guidelines:**

- Use `X | None` instead of `Optional[X]` (Python 3.10+).
- Use `X | Y` instead of `Union[X, Y]` (Python 3.10+).
- Annotate `self` and `cls` return types with `-> Self` (`typing.Self`, Python 3.11+).
- Use `TypeAlias` or the `type` statement (Python 3.12+) for complex types.

## 5. Docstrings — Google Style

Write docstrings for **all public** classes, methods, and functions.

### 5.1 Simple Function

```python
def get_user(user_id: str) -> User:
    """Retrieve a user by their unique identifier."""
    ...
```

### 5.2 Complex Function

```python
def process_batch(
    items: list[Item],
    max_workers: int = 4,
    on_progress: Callable[[int, int], None] | None = None,
) -> BatchResult:
    """Process items concurrently using a worker pool.

    Distributes items across the configured number of workers.
    Progress can be monitored via the optional callback.

    Args:
        items: The items to process. Must not be empty.
        max_workers: Maximum concurrent workers. Defaults to 4.
        on_progress: Optional callback receiving (completed, total) counts.

    Returns:
        BatchResult containing succeeded items and any failures with
        their associated exceptions.

    Raises:
        ValueError: If items is empty.
        ProcessingError: If the batch cannot be processed.

    Example:
        >>> result = process_batch(items, max_workers=8)
        >>> print(f"Processed {len(result.succeeded)} items")
    """
    ...
```

### 5.3 Class Docstring

```python
class UserService:
    """Service for managing user lifecycle operations.

    Provides methods for creating, retrieving, updating, and
    deleting users with proper validation and error handling.

    Attributes:
        repository: The data access layer for user persistence.
        logger: Logger instance for operation tracking.

    Example:
        >>> service = UserService(repository, logger)
        >>> user = service.create_user(CreateUserInput(...))
    """

    def __init__(self, repository: UserRepository, logger: Logger) -> None:
        """Initialize the user service.

        Args:
            repository: Data access layer for users.
            logger: Logger for tracking operations.
        """
        self.repository = repository
        self.logger = logger
```

## 6. Formatting & Readability

### 6.1 Line Length

Target **120 characters**. Break long lines with readability in mind.

> **Note:** PEP 8 default is 79 characters and Black/Ruff default is 88.
> We use 120 as a project convention — it's a practical choice for modern
> wide displays while still preventing excessively long lines.

### 6.2 Function Signatures

```python
# One argument per line when signature exceeds line length
def create_user(
    email: str,
    name: str,
    role: UserRole = UserRole.MEMBER,
    notify: bool = True,
) -> User:
    ...
```

### 6.3 Method Chaining

```python
# Wrap chains with parentheses for clarity
result = (
    db.query(User)
    .filter(User.active == True)
    .order_by(User.created_at.desc())
    .limit(10)
    .all()
)
```

### 6.4 Long Strings

```python
# Use implicit string concatenation inside parentheses
error_message = (
    f"Failed to process user {user_id}: "
    f"received status {response.status_code} "
    f"with body {response.text[:100]}"
)
```

### 6.5 Comprehensions

```python
# Simple — single line
names = [user.name for user in users if user.active]

# Complex — multi-line for readability
results = [
    transform(item)
    for item in source_data
    if item.is_valid()
    and item.category in allowed_categories
]
```

## 7. Comments

### 7.1 When to Comment

- Explain **why**, not **what** — the code shows what, comments explain intent.
- Document non-obvious business logic, edge cases, and workarounds.
- Add `TODO`, `FIXME`, `HACK` markers with context.

```python
# Good — explains why
# Retry with exponential backoff because the upstream API
# rate-limits to 100 req/min and returns 429 on overflow.
for attempt in range(MAX_RETRY_ATTEMPTS):
    ...

# Bad — restates the code
# Increment counter by 1
counter += 1
```

### 7.2 Inline Comments

Use sparingly, separated by at least **two spaces** from code.

```python
timeout = 30  # Seconds; upstream SLA guarantees < 10s response
```

## 8. Error Handling

### 8.1 Catch Specific Exceptions

Never use bare `except` or `except Exception`. Always catch the most specific
exception type possible.

```python
# Good — specific exception
try:
    user = repository.get(user_id)
except UserNotFoundError:
    logger.warning("User %s not found", user_id)
    return None

# Bad — catches everything, hides bugs
try:
    user = repository.get(user_id)
except Exception:
    return None
```

### 8.2 EAFP Over LBYL

Prefer **EAFP** (Easier to Ask Forgiveness than Permission) — attempt the
operation and handle the exception — over **LBYL** (Look Before You Leap).

```python
# EAFP — Pythonic
try:
    value = data[key]
except KeyError:
    value = default

# LBYL — less Pythonic
if key in data:
    value = data[key]
else:
    value = default
```

### 8.3 Custom Exceptions

Define domain-specific exceptions to make error handling expressive and
decoupled from implementation details.

```python
class ServiceError(Exception):
    """Base exception for service layer errors."""


class UserNotFoundError(ServiceError):
    """Raised when a requested user does not exist."""

    def __init__(self, user_id: str) -> None:
        super().__init__(f"User not found: {user_id}")
        self.user_id = user_id
```

### 8.4 Context Managers

Use `with` statements for any resource that requires cleanup (files, database
connections, locks, HTTP sessions).

```python
# Always use context managers for resource cleanup
with open("config.yaml") as f:
    config = yaml.safe_load(f)

# Custom context manager with contextlib
from contextlib import contextmanager


@contextmanager
def database_transaction(session: Session):
    """Provide a transactional scope around a series of operations."""
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
```

### 8.5 `try/except/else/finally`

Use the full form when each clause has a distinct purpose.

```python
try:
    result = perform_operation()
except OperationError as exc:
    logger.error("Operation failed: %s", exc)
    raise
else:
    # Runs only if no exception was raised
    process_result(result)
finally:
    # Always runs — use for cleanup
    cleanup()
```

## 9. Data Classes

### 9.1 Standard `dataclass`

Use `dataclass` for simple internal data structures where input is trusted.

```python
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Coordinate:
    """An immutable geographic coordinate.

    Using frozen=True for immutability (thread-safe, hashable).
    Using slots=True for lower memory footprint and faster access.
    """

    latitude: float
    longitude: float
```

### 9.2 Dataclass vs Pydantic

| Use Case                         | Choice        |
| -------------------------------- | ------------- |
| Internal data, trusted input     | `dataclass`   |
| External/untrusted data (APIs)   | `Pydantic`    |
| Need runtime validation/coercion | `Pydantic`    |
| Config files, env vars           | `Pydantic`    |
| Simple value objects, DTOs       | `dataclass`   |

```python
# Pydantic — for API boundaries and validation
from pydantic import BaseModel, Field


class CreateUserRequest(BaseModel):
    """Request model for user creation endpoint."""

    email: str = Field(..., description="User email address")
    name: str = Field(..., min_length=1, max_length=100)
    age: int = Field(..., ge=0, le=150)
```

## 10. Testing Conventions

### 10.1 Framework & File Structure

Use **pytest** as the default testing framework.

```text
tests/
├── conftest.py          # Shared fixtures
├── test_user_service.py # Tests for user service
└── test_repository.py   # Tests for repository layer
```

**Naming rules:**

- Test files: `test_<module>.py`
- Test functions: `test_<behavior_being_tested>()`
- Test classes (optional grouping): `TestClassName`

### 10.2 Fixtures & Parametrize

```python
import pytest


@pytest.fixture
def sample_user() -> User:
    """Create a sample user for testing."""
    return User(id="123", name="Alice", email="alice@example.com")


@pytest.mark.parametrize(
    ("input_email", "expected_valid"),
    [
        ("user@example.com", True),
        ("invalid-email", False),
        ("", False),
    ],
)
def test_email_validation(input_email: str, expected_valid: bool) -> None:
    """Verify email validation accepts valid and rejects invalid formats."""
    assert validate_email(input_email) == expected_valid
```

### 10.3 Assertion Style

- Use plain `assert` statements — pytest introspection provides clear failure
  messages.
- Test one behavior per test function.
- Use descriptive test names that read as specifications.

## 11. Project File Standards

### 11.1 README Structure

Every project should include a `README.md` with at minimum:

- Project description
- Installation instructions
- Quick start / usage example
- Development setup
- Configuration reference

### 11.2 CHANGELOG Format

Follow [Keep a Changelog](https://keepachangelog.com/) conventions:

```markdown
# Changelog

## [Unreleased]

### Added
- New feature X

### Changed
- Modified behavior of Y

### Fixed
- Bug in Z
```

## 12. Best Practices Checklist

1. **Use `ruff`** — single tool for linting, formatting, and docstring enforcement.
2. **Enable strict type checking** — `mypy --strict` or `pyright` strict mode.
3. **100-character lines** — project convention for wide displays.
4. **Descriptive names** — clarity over brevity, always.
5. **Absolute imports** — more maintainable than relative imports.
6. **Google-style docstrings** — consistent and readable.
7. **Document all public APIs** — every public function, class, and method.
8. **Type-annotate everything** — leverage `X | None` syntax (3.10+).
9. **Comments explain *why*** — not *what* the code does.
10. **Catch specific exceptions** — never use bare `except`.
11. **Use context managers** — `with` for any resource requiring cleanup.
12. **Prefer `dataclass`** — with `slots=True` and `frozen=True` where appropriate.
13. **Use Pydantic at boundaries** — validate untrusted / external data.
14. **Write tests with pytest** — descriptive names, focused assertions.
15. **Automate in CI** — run `ruff` and type checker on every commit.
16. **Target Python 3.10+** — for new projects, prefer 3.12+ for modern features.
17. **Trailing commas** — use in multi-line structures for cleaner diffs.
