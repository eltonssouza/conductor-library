---
software_dev: supporting
---

# Linux Command-Line for Operations - Complete Professional Guide

> **Category:** 07_devops_sre_operations · **Language:** English

---

### Shell, pipes, processes, and text tools for running systems
**Original guide written from first principles, current to 2026**

> **Original reference book (English).** This is an **independent, originally written** guide. It is not an extract, summary, or paraphrase of any third-party book; it teaches the Linux command line from first principles with original examples. Canonical references are listed under **References** as pointers only. Each chapter follows the TO-BRAIN editorial standard (see `FILE_CONVENTIONS.md`).
>
> **Scope notice:** the Linux command line is where servers are operated and debugged. This guide covers the shell, the pipe-and-filter philosophy, and process/file basics that make you effective, current to 2026.

---

## How to read this guide

| Level | Profile | Parts |
|-------|---------|-------|
| 1 — Beginner | New to the shell | Part I |
| 2 — Intermediate | Operating servers | Part II |

**Target audience:** developers and ops who work on Linux servers and containers.

**Structure of each chapter:** Introduction · Business context · Theoretical concepts · Architecture · Diagrams (Mermaid) · Real examples · Step by step · Complete examples · Exercises · Challenges · Checklist · Best practices · Anti-patterns · Troubleshooting · References.

> **Note on prerequisites.** Assumes you can open a terminal.

---

## Table of Contents

**Part I – The philosophy**
1. Small tools and pipes
2. Processes, files, and permissions

**Part II – Operating**
3. Inspecting a running system

> **Status of this edition:** complete for its declared scope. **Ready:** Parts I–II (Ch. 1–3).

---

## Part I – The philosophy

The Linux command line is powerful not because any one tool is huge, but because **small, single-purpose tools compose**. Each does one thing well; you connect them with **pipes** to build exactly the command you need. Internalizing this composition mindset is worth more than memorizing flags.

---

## Chapter 1 — Small tools and pipes

### 1.1 Introduction

The Unix philosophy: each program does **one thing well**, reads from standard input, writes to standard output, and can be **piped** into another. Instead of one mega-tool, you chain small ones (`grep`, `sort`, `cut`, `wc`) to transform text streams. A pipeline `A | B | C` feeds A's output into B into C — composing a custom tool on the fly.

### 1.2 Business context

On a server, you constantly need to extract, filter, and summarize data (logs, process lists, metrics) ad hoc. The ability to compose small tools into a one-line pipeline answers questions in seconds without writing a program — invaluable during incidents and routine ops. Engineers fluent in this are dramatically faster at diagnosing and operating systems, which directly shortens outages and toil.

### 1.3 Theoretical concepts: composition via streams

```mermaid
flowchart LR
    a["command A (produces text)"] -->|stdout -> stdin| b["command B (filters)"]
    b -->|pipe| c["command C (summarizes)"]
```

Each tool consumes **stdin** and produces **stdout**; the pipe `|` connects them. This stream model means you don't need a tool for every task — you assemble one. Redirection (`>` to a file, `<` from a file, `2>` for errors) connects streams to files. Mastering a handful of filters plus the pipe covers most needs.

### 1.4 Architecture: a pipeline as a custom tool

```mermaid
flowchart TB
    log["access.log"] --> grep["grep ' 500 ' (errors only)"]
    grep --> cut["cut -d' ' -f7 (the URL field)"]
    cut --> sort["sort | uniq -c | sort -rn (count, rank)"]
    sort --> top["top error URLs"]
```

### 1.5 Real example

**Scenario.** During an incident, find which URLs return the most HTTP 500s in an access log.

**Problem.** Opening a huge log by hand is hopeless; writing a script is too slow mid-incident.

**Solution.** A one-line pipeline composing small tools.

**Implementation.**

```bash
grep ' 500 ' access.log \
  | awk '{print $7}' \
  | sort | uniq -c | sort -rn \
  | head
# -> counts of 500s per URL, highest first
```

**Result.** In one line, the top error-producing URLs are ranked — answering the incident question in seconds without any program. Composition delivered a bespoke tool instantly.

**Future improvements.** Save useful pipelines as shell functions/aliases; for repeated analysis, move to a proper log tool.

### 1.6 Exercises

1. State the Unix philosophy in one sentence.
2. What do stdin/stdout/pipe let you do?
3. Build a pipeline to count unique IPs in a log.

### 1.7 Challenges

- **Challenge.** Take a log file. Write a one-line pipeline that extracts, filters, counts, and ranks something useful (e.g. top clients, slowest endpoints).

### 1.8 Checklist

- [ ] I compose small tools with pipes.
- [ ] I use stdin/stdout and redirection.
- [ ] I prefer a pipeline to a script for ad-hoc questions.
- [ ] I know a core set of filters (grep/awk/sort/uniq/cut).

### 1.9 Best practices

- Compose single-purpose tools instead of seeking one big tool.
- Save handy pipelines as aliases/functions.
- Keep each stage doing one transformation.

### 1.10 Anti-patterns

- Writing a program for what a pipeline answers instantly.
- Opening huge files manually during incidents.
- Monolithic, unreadable one-liners with no structure.

### 1.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Slow to answer log questions | Not using pipelines | Compose grep/awk/sort/uniq |
| Pipeline gives nothing | Wrong field/filter | Inspect each stage's output step by step |
| Errors not captured | stderr not redirected | Use `2>&1` or `2>file` |

### 1.12 References

- B. Lee, *Linux Utilities Cookbook* (Packt, 2013) — ISBN 978-1782162001.
- The GNU Coreutils manual: https://www.gnu.org/software/coreutils/manual/.

---

## Chapter 2 — Processes, files, and permissions

### 2.1 Introduction

Operating a Linux system means understanding **processes** (running programs, each with a PID), the **file system** (everything is a file, organized in a tree), and **permissions** (who can read/write/execute what). These three concepts underlie nearly every operational task: starting/stopping services, finding what's using resources, and securing access.

### 2.2 Business context

Most production issues come down to a process (a runaway service, a crashed daemon), a file (a full disk, a misconfigured config), or a permission (a service can't read a key). Fluency here is the difference between resolving an incident in minutes and flailing. It's also foundational to security: wrong permissions are a common vulnerability. These basics are the operational literacy every engineer on Linux needs.

### 2.3 Theoretical concepts: processes, files, permissions

```mermaid
mindmap
  root((Linux basics))
    Processes
      PID, parent, state
      signals (TERM, KILL)
    Files
      everything is a file
      tree from /
    Permissions
      user/group/other
      read/write/execute
```

- **Processes**: each has a PID, a parent, and a state; you signal them (e.g. `SIGTERM` to stop gracefully, `SIGKILL` to force). Tools: `ps`, `top`/`htop`, `kill`.
- **Files**: a single tree from `/`; devices, sockets, and even process info (`/proc`) appear as files.
- **Permissions**: each file has read/write/execute bits for **user/group/other**; `chmod`/`chown` manage them.

### 2.4 Architecture: signal a process, inspect via /proc

```mermaid
flowchart LR
    ps["ps/top: find the PID"] --> sig["kill -TERM PID: ask it to stop"]
    sig --> check["confirm via ps; -KILL only if needed"]
```

### 2.5 Real example

**Scenario.** A runaway process is consuming all CPU on a server.

**Problem.** The server is sluggish; you must find and stop the offender without rebooting.

**Solution.** Identify the process, then signal it to stop gracefully.

**Implementation.**

```bash
top -o %CPU            # find the CPU hog and note its PID
ps -p 12345 -o pid,cmd # confirm what PID 12345 actually is
kill -TERM 12345       # ask it to shut down gracefully
# if it ignores TERM after a moment:
kill -KILL 12345       # force-stop (last resort)
```

**Result.** The offending process is identified and stopped cleanly (TERM first, KILL only if needed), restoring the server without a disruptive reboot.

**Future improvements.** Find *why* it ran away (logs, the parent process); add resource limits (cgroups) so one process can't starve the host.

### 2.6 Exercises

1. What is a PID and how do you signal a process?
2. Why prefer `SIGTERM` over `SIGKILL` first?
3. What does "everything is a file" mean practically?

### 2.7 Challenges

- **Challenge.** Find the top memory-consuming process on a machine, confirm what it is, and describe how you'd stop it safely.

### 2.8 Checklist

- [ ] I can find and inspect processes (ps/top).
- [ ] I signal processes correctly (TERM before KILL).
- [ ] I understand the single file tree and `/proc`.
- [ ] I can read and set permissions (chmod/chown).

### 2.9 Best practices

- Stop processes gracefully (TERM) before forcing (KILL).
- Use least-privilege file permissions.
- Investigate root cause, not just the symptom process.

### 2.10 Anti-patterns

- `kill -9` as a first resort (no graceful shutdown).
- Overly permissive permissions (e.g. world-writable secrets).
- Rebooting to clear a single bad process.

### 2.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Server sluggish | Runaway process | Find PID (top), TERM it |
| "Permission denied" for a service | Wrong file permissions/owner | Fix with chmod/chown (least privilege) |
| Disk full | Large/unrotated files | Find big files; rotate logs |

### 2.12 References

- B. Lee, *Linux Utilities Cookbook* (Packt, 2013) — ISBN 978-1782162001.
- "The Linux Documentation Project": https://tldp.org; `man` pages.

---

> **End of Part I.** You can now work effectively on Linux: compose small single-purpose tools with pipes to answer operational questions on the fly, and handle the core operational objects — processes (find and signal them gracefully), files (one tree, everything-is-a-file), and permissions (least privilege). **Part II — Operating** (Chapter 3) covers inspecting a running system under pressure: disk/memory/network checks, log locations, and the first commands to run during an incident.

---

## Part II – Operating

Part I built fluency with composing tools and handling processes, files, and permissions. Operating a real system adds urgency: when a service is slow or down at 3 a.m., you need a fast, ordered way to ask the machine "what is wrong with you?" — is it out of disk, out of memory, saturating CPU, drowning in network, or is a process wedged? This chapter is the operational toolkit: the handful of commands that answer those questions, where the logs live, and the order to run them in during an incident.

---

## Chapter 3 — Inspecting a running system

### 3.1 Introduction

Inspecting a live system means reading its **resources** and **logs** quickly. A small, reliable set of tools covers it: `top`/`htop` (overall CPU/memory and per-process), `ps` (snapshot of processes), `free` (memory), `df` (disk space) and `du` (where the space went), `ss` (sockets/ports), `journalctl` and `/var/log` (logs), plus `lsof` (open files/ports) and `strace` (what a process is actually doing). Most live on the `/proc` filesystem — the kernel's live view of the system exposed as files, true to "everything is a file" from Part I. The skill is knowing which to reach for first.

### 3.2 Business context

During an incident, time-to-diagnosis dominates time-to-recovery. An engineer who knows the right five commands isolates "disk full" or "OOM-killed" or "port not listening" in under a minute; one who doesn't flails while users are down. These tools are universal — present on essentially every Linux box, no agent required — so they are the dependable floor beneath any fancier observability stack. Knowing them is the difference between a calm, ordered triage and a panicked guess.

### 3.3 Theoretical concepts: read resources, then logs

```mermaid
flowchart LR
    sym["Symptom: slow / down"] --> res["Check resources: CPU, mem, disk, net"]
    res --> proc["Identify the process (top/ps)"]
    proc --> logs["Read its logs (journalctl / /var/log)"]
    logs --> deep["Deep-dive: lsof / strace if needed"]
```

- **CPU/load** — `top`/`htop`: who's burning CPU; load average vs core count hints at saturation (links to the USE method in the Systems Performance guide).
- **Memory** — `free -h` for headroom; check `dmesg` for the OOM killer when processes vanish.
- **Disk** — `df -h` for "is a filesystem full?", then `du -sh *` to find the culprit directory. A full disk masquerades as countless unrelated failures.
- **Network** — `ss -tulpn` to see what's listening and on which port (the modern replacement for `netstat`).
- **Logs** — `journalctl -u <svc>` on systemd hosts; `/var/log/...` elsewhere; tail and grep for the failure window.
- **Deep-dive** — `lsof -p <pid>` (open files/sockets), `strace -p <pid>` (live syscalls) when a process is stuck and the logs don't say why.

### 3.4 Architecture: where the data comes from

```mermaid
flowchart TB
    kernel["Kernel"] --> proc["/proc, /sys (live state as files)"]
    proc --> tools["top / ps / free / ss read here"]
    services["Services"] --> jrnl["journald / /var/log (logs)"]
    jrnl --> read["journalctl / tail / grep"]
    tools --> triage["Triage decision"]
    read --> triage
```

### 3.5 Real example

**Scenario.** A web service starts returning 500s. Alerts fire; you SSH into the host with no idea yet what's wrong.

**Problem.** The symptom (500s) has many possible causes — full disk, exhausted memory, pegged CPU, a dead process, or a port not listening. You need to localize fast.

**Solution.** Run an ordered triage: resources first, then the process, then its logs.

**Implementation (incident triage sequence).**

```bash
# 1) Resources at a glance
top                 # CPU/mem hogs, load average (q to quit) — or: htop
free -h             # memory headroom; is swap thrashing?
df -h               # any filesystem at 100%?  (a full / breaks everything)
du -sh /var/log/*   # if df shows full: who ate the disk?

# 2) Is the service even up and listening?
systemctl status myapp
ss -tulpn | grep :8080      # is something listening on the port?

# 3) What does the service say?
journalctl -u myapp --since "10 min ago" --no-pager | tail -n 50
# non-systemd: tail -n 100 /var/log/myapp/error.log

# 4) Stuck process? see what it's doing
lsof -p "$(pgrep -f myapp | head -1)"     # open files/sockets (leak? FD exhaustion?)
strace -p "$(pgrep -f myapp | head -1)"   # live syscalls (blocked on read? connect?)
```

**Result.** Within a minute `df -h` shows `/` at 100% — a runaway log filled the disk, so the app can't write and returns 500s. `du -sh /var/log/*` pinpoints the file; truncating it and adding log rotation restores service. The ordered sequence turned an ambiguous symptom into a precise cause fast.

**Future improvements.** Capture this sequence as a runbook; add monitoring/alerts for disk and memory thresholds (don't wait for 500s); set up log rotation (`logrotate`) so a single log can't fill the disk again.

### 3.6 Exercises

1. A process disappeared with no error in its own log — which command tells you the kernel OOM-killed it?
2. How do you find which directory is consuming a full filesystem?
3. Which command shows what is listening on a given TCP port, and why prefer it over `netstat`?

### 3.7 Challenges

- **Challenge.** Write a 6-line incident triage runbook for a host: the exact commands, in order, to check CPU, memory, disk, listening ports, and service logs — each with one line on what its output tells you and what action it implies.

### 3.8 Checklist

- [ ] I check resources (CPU, memory, disk, network) before guessing.
- [ ] I know how to find a full filesystem and the directory filling it.
- [ ] I can confirm a service is running and listening on its port.
- [ ] I know where this host's logs are (`journalctl` vs `/var/log`).
- [ ] I can deep-dive a stuck process with `lsof`/`strace`.

### 3.9 Best practices

- Triage in a fixed order (resources → process → logs); don't jump to conclusions.
- Prefer modern tools (`ss`, `journalctl`, `htop`) but know the classics exist.
- Treat a full disk as a prime suspect — it causes wildly varied symptoms.
- Capture repeated triage steps as a runbook so anyone can follow them.

### 3.10 Anti-patterns

- Restarting the service blindly without reading any signal (loses the evidence).
- Ignoring disk and memory and assuming it's "the app's fault".
- Editing files/log levels in production with no record of what changed.
- Running `strace` on a busy production process without understanding its overhead.

### 3.11 Troubleshooting

| Symptom | First command | What it tells you |
|---------|---------------|-------------------|
| Everything failing oddly | `df -h` | A filesystem at 100% breaks writes everywhere |
| Process vanished | `dmesg \| grep -i oom` | Kernel OOM-killed it (out of memory) |
| "Connection refused" | `ss -tulpn` | Whether anything is listening on the port |
| Host sluggish | `top` / `uptime` | CPU hogs; load average vs core count |
| Service stuck, no logs | `strace -p <pid>` | Which syscall it's blocked on |

### 3.12 References

- J. Lee, *Linux Utilities Cookbook* (Packt, 2013) — ISBN 978-1782160779 — process, disk, memory, and network inspection utilities.
- B. Gregg, *Systems Performance*, 2nd ed. (Addison-Wesley, 2020) — the USE method behind resource triage (see the Systems Performance Analysis guide).
- `man` pages: `proc(5)`, `top(1)`, `ss(8)`, `journalctl(1)`.

---

> **End of Part II — and of the guide.** Beyond composing tools and managing processes/files/permissions (Part I), you can now **inspect a running system under pressure**: read CPU, memory, disk, and network with a small reliable toolkit, find where the logs live, and run an ordered triage that turns an ambiguous symptom into a precise cause in minutes. This is the operational floor every Linux engineer stands on during an incident — dependable, agentless, and present on every box.
