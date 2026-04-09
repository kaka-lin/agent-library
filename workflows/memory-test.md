---
description: Generic memory leak test methodology for Python/AI backend servers
---

# Memory Leak Test (Generic Template)

Run memory and resource leak diagnostics against a running Python backend server.

> [!NOTE]
> This is a **generic template**. Each project may override this with a local
> `.agents/workflows/memory-test.md` containing project-specific environment
> variables, startup commands, and custom test scripts.

## Prerequisites

- Server must NOT already be running on the target port.
- `nvidia-smi` available if GPU metrics are needed.
- Project-specific environment variables are set.

## Steps

1. **Start the Server**

    Set environment variables and start the server process:

    ```bash
    # Export project-specific env vars (e.g., API keys, environment settings)
    export <ENV_VAR>=<VALUE>
    
    # Then start the server
    <START_COMMAND>
    ```

    Wait until the server is fully ready (log output confirms listening).

2. **Capture Baseline Metrics**

    In a **separate terminal**, record the baseline before sending any requests.

    - **RSS and VSZ (main server process):**

        ```bash
        ps -eo pid,ppid,rss,vsz,etime,args | grep "<server_process_pattern>" | grep -v grep
        ```

      - **RSS** — Resident Set Size (physical memory actually used)
      - **VSZ** — Virtual Memory Size (total virtual address space allocated)

    - **GPU VRAM (if applicable):**

        ```bash
        nvidia-smi --query-gpu=index,memory.used,memory.total \
            --format=csv,noheader,nounits
        ```

    - **Child processes (e.g. workers, subprocesses):**

        ```bash
        pgrep -fa "<child_process_pattern>" | wc -l
        ```

3. **Run Request/Stop Cycles**

    Send multiple request/stop cycles to the server (at least 3 rounds). After **each stop**:

    - **Check RSS/VSZ:**

        ```bash
        ps -eo pid,rss,vsz,args | grep "<server_process_pattern>" | grep -v grep
        ```

        Compare against baseline. RSS should return close to the initial value after
        each stop. Significant growth across cycles indicates a memory leak.

    - **Check GPU VRAM:**

        ```bash
        nvidia-smi --query-gpu=index,memory.used --format=csv,noheader,nounits
        ```

    - **Check child process count:**

        ```bash
        pgrep -fa "<child_process_pattern>" | wc -l
        ```

        Should be `0` after stop. Leftover child processes indicate cleanup failure.

4. **Check for Orphan/Zombie Processes**

    After all cycles complete, look for orphan processes (PPID=1) that were not
    properly cleaned up:

    - **Orphan Processes:**

        ```bash
        ps -eo pid,ppid,rss,etime,args | grep "<server_process_pattern>" | awk '$2 == 1'
        ```

    - **Zombie Processes:**

        ```bash
        ps -eo pid,stat,args | grep "<server_process_pattern>" | grep -E "Z|defunct"
        ```

5. **Stop the Server and Final Verification**

    Stop the server (`Ctrl+C` or `kill`) and verify everything is cleaned up:

    - **Server processes:** `pgrep -f "<server_process_pattern>" | wc -l` (Should be 0)
    - **Child processes:** `pgrep -f "<child_process_pattern>" | wc -l` (Should be 0)
    - **GPU VRAM:** `nvidia-smi --query-gpu=index,memory.used --format=csv,noheader,nounits`
