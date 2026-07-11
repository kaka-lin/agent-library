# Python Architecture — Concurrency & Background Work

Micro-level code style lives in [python-code-style.md](python-code-style.md).
This file covers the macro decisions that guide *cannot*: how to run background
work, pick a concurrency model, and structure long-running or one-shot jobs.

**Apply when:** designing background tasks, concurrency, streaming pipelines, or
task orchestration in a Python service (FastAPI, workers, CLIs).

## 1. Pick the Work Shape First, Then the Tool

There is no "threads vs async" answer. Choose by the **shape of the work**, along
this spectrum from lightest to heaviest:

| # | Pattern | Representative tools | Fits work that is |
| --- | --- | --- | --- |
| 1 | Inline `await` | stdlib | sub-second; caller can wait |
| 2 | In-process fire-and-forget | `asyncio.create_task`, FastAPI `BackgroundTasks` | seconds; failure non-critical; need not survive restart |
| 3 | Async task queue | **arq**, Taskiq | one-shot but must be reliable: retries, pollable status, I/O-bound |
| 4 | General task queue | Celery, Dramatiq, RQ | huge scale, CPU-heavy, many workers (Celery has no native async) |
| 5 | Long-lived worker | `threading.Thread` subclass + `Queue` | a continuous stream with long-lived internal state |
| + | Workflow engine | Temporal | durable multi-step orchestration |

## 2. Decision Axes

Answer these before choosing a pattern:

- **One-shot or continuous?** One request → done, versus a loop over a stream.
- **Duration?** Milliseconds, seconds, minutes, hours.
- **Durability?** Must an in-flight job survive a process restart?
- **CPU-bound/blocking or I/O-bound?** Whisper inference vs awaiting an HTTP API.
- **Scale?** Do workers need to scale independently of the web process?
- **Retries / observability?** Is at-least-once delivery and status tracking required?

## 3. Rules

- **R1 — Short async I/O → asyncio, not threads.** A request-scoped call that
  merely awaits network I/O (a vendor API, an LLM) belongs in
  `asyncio.create_task` (or `BackgroundTasks`). Wrapping it in a
  `threading.Thread` subclass adds a lifecycle it does not need and is slower.
- **R2 — Long-lived streaming worker → a worker class.** A component that owns a
  `while running:` loop and long-lived state (buffers, a model handle, queue
  positions) belongs in a named worker: `threading.Thread` subclass + `Queue`
  when the libraries are blocking (e.g. Whisper), or an `asyncio.Task` +
  `asyncio.Queue` when the pipeline is async-native.
- **R3 — Background work is a named unit, never an anonymous closure.** Give it a
  name and a home (a task function in a `tasks` module, a service method, or a
  worker class). Do not bury the job body in an inline closure inside a route
  handler.
- **R4 — Inject dependencies via `Depends`.** In FastAPI, do not hand-wire
  singletons (`store`, provider registries, config) inside the handler body.
  Resolve them through `Depends` so handlers stay pure HTTP glue.
- **R5 — Job state lives in a store, not process memory.** Persist status to a DB
  row or the broker, not an in-memory dict, so it is pollable, survives a
  restart, and can scale horizontally.
- **R6 — Cross-thread → event loop uses `queue.Queue`.** When a plain thread
  hands work to an asyncio loop in another thread, use a thread-safe
  `queue.Queue`; `asyncio.Queue` is only safe within one event loop.
- **R7 — Need durability/retries/independent scaling → a task queue.** Reach for
  a real queue, not a hand-rolled one. Prefer **arq** for async-first services
  (Redis-only, workers in the event loop, natural FastAPI fit); Celery for very
  large multi-broker fleets (no native async); Dramatiq as a simpler Celery.
- **R8 — Make retried work idempotent, assume at-least-once.** Any durable queue
  can deliver a task twice (crash between run and ack). Design the task so a
  repeat is harmless, and add a reaper for jobs stuck in `running`.

## 4. Anti-Patterns

- Wrapping a 2-second async call in a `threading.Thread` subclass — heavy
  machinery for a paper box; also discards the DB-backed job benefits (R5).
- A long anonymous `_work` closure defined inside a route handler (violates R3).
- Job status kept only in memory — lost on restart, not pollable (violates R5).
- A class, factory, or `SharedContext` object built for a single implementation —
  that is [python-code-style.md](python-code-style.md) territory: no abstraction
  without a second caller.

## 5. Mapping to This Org's Systems

- **Live captioning** (`ai-live-captioning-api`) → **Pattern 5**. A per-session
  pipeline of `Thread` subclasses (`PullerThread` → `TranscriberThread` →
  translation) wired by a `SessionManager`, communicating over `Queue`s.
  Continuous stream + blocking Whisper + per-session lifecycle → the correct fit;
  do not "modernise" it into async.
- **Eden image/scene generation** (`ai-eden-service`) → between **Pattern 2 and
  3**. One-shot, I/O-bound vendor calls, a few seconds each. Today it is
  `asyncio.create_task` + a DB job row (a hand-rolled Pattern 2.5: pollable but
  not durable — a restart orphans `running` jobs). Upgrade path if reliability
  matters is **arq** (Redis already in the stack), not threads.

## References

- [FastAPI Background Tasks vs Celery vs Arq](https://medium.com/@komalbaparmar007/fastapi-background-tasks-vs-celery-vs-arq-picking-the-right-asynchronous-workhorse-b6e0478ecf4a)
- [Why arq/RQ over Celery for LLM workloads](https://dangquan1402.github.io/llm-engineering-notes/2026/04/02/lightweight-task-queues-for-llm-apps.html)
- [Async/Await vs Threads — choosing the right approach](https://dev.to/koladev/asyncawait-vs-threads-choosing-the-right-approach-2l1d)
- [Choosing the right Python task queue (Judoscale)](https://judoscale.com/blog/choose-python-task-queue)
