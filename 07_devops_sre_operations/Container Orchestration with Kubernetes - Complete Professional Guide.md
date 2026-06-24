---
software_dev: supporting
---

# Container Orchestration with Kubernetes - Complete Professional Guide

> **Category:** 07_devops_sre_operations · **Language:** English

---

### Pods, deployments, services, and declarative desired state
**Original guide written from first principles, current to 2026**

> **Original reference book (English).** This is an **independent, originally written** guide. It is not an extract, summary, or paraphrase of any third-party book; it teaches Kubernetes from first principles with original examples. Canonical books are listed under **References** as pointers only. Each chapter follows the TO-BRAIN editorial standard (see `FILE_CONVENTIONS.md`).
>
> **Scope notice:** Kubernetes orchestrates containers across a cluster — scheduling, scaling, healing, and networking them. This guide covers its core objects and the declarative, reconciliation model that defines how it works, current to 2026.

---

## How to read this guide

| Level | Profile | Parts |
|-------|---------|-------|
| 1 — Beginner | New to Kubernetes | Part I |
| 2 — Intermediate | Deploying workloads | Part II |

**Target audience:** developers and platform engineers running containerized workloads.

**Structure of each chapter:** Introduction · Business context · Theoretical concepts · Architecture · Diagrams (Mermaid) · Real examples · Step by step · Complete examples · Exercises · Challenges · Checklist · Best practices · Anti-patterns · Troubleshooting · References.

> **Note on prerequisites.** Assumes containers (Docker) and basic networking.

---

## Table of Contents

**Part I – Core model**
1. Declarative desired state and reconciliation
2. Pods, Deployments, and Services

**Part II – Operations**
3. Scaling, health, and config

> **Status of this guide:** phased delivery. **Ready:** Part I (Ch. 1–2). **In progress:** Part II.

---

## Part I – Core model

Kubernetes' power comes from one idea applied everywhere: you **declare the desired state**, and the system continuously works to make reality match it. You don't run imperative commands to start/stop containers; you describe what you want, and controllers reconcile the cluster toward it — scheduling, restarting, and scaling automatically.

---

## Chapter 1 — Declarative desired state

### 1.1 Introduction

In Kubernetes you submit **declarative** specifications — "I want 3 replicas of this container running" — to the API server, which stores the **desired state**. **Controllers** constantly compare desired state to actual state and act to close any gap (this is **reconciliation**). If a container dies, the controller notices the gap and starts a new one. You manage the *goal*, not the steps.

### 1.2 Business context

Imperative ops ("ssh in and restart it") don't scale and drift from any documented intent. Declarative, self-healing infrastructure means the system maintains itself toward a known-good state, recovering from failures automatically and making deployments repeatable and auditable (the desired state is version-controlled YAML). This reduces operational toil and outages, and is why Kubernetes became the standard substrate for running services at scale.

### 1.3 Theoretical concepts: the reconciliation loop

```mermaid
flowchart LR
    desired["Desired state (your YAML)"] --> ctrl["Controller compares"]
    actual["Actual cluster state"] --> ctrl
    ctrl --> act["Act to close the gap (create/delete/scale)"]
    act --> actual
```

Everything in Kubernetes is an **object** with a desired `spec` and an observed `status`. Controllers run reconciliation loops: observe, diff, act, repeat. This loop is what makes the cluster self-healing — kill a pod and the loop recreates it to restore the declared replica count.

### 1.4 Architecture: API server + controllers

```mermaid
flowchart TB
    you["You: kubectl apply YAML"] --> api["API server (stores desired state)"]
    api --> ctrls["Controllers (reconcile)"]
    ctrls --> nodes["Schedule pods onto nodes"]
    nodes --> status["Status reported back"]
    status --> api
```

### 1.5 Real example

**Scenario.** You need a web service to always have 3 instances running, surviving node/pod failures.

**Problem.** Manually restarting crashed instances is error-prone and slow.

**Solution.** Declare 3 replicas; Kubernetes keeps that true automatically.

**Implementation (declarative spec).**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata: { name: web }
spec:
  replicas: 3                 # desired state
  selector: { matchLabels: { app: web } }
  template:
    metadata: { labels: { app: web } }
    spec:
      containers:
        - name: web
          image: myorg/web:1.4.2
```

```bash
kubectl apply -f web.yaml    # submit desired state; controllers maintain 3 replicas
# kill a pod -> the Deployment controller starts a replacement automatically
```

**Result.** Three replicas are always maintained; a crashed pod or failed node is healed without human action. You manage intent (3 replicas), not individual containers.

**Future improvements.** Add health probes and resource requests (Chapter 3) so scheduling and healing are accurate.

### 1.6 Exercises

1. What does "declarative desired state" mean in Kubernetes?
2. What is a reconciliation loop?
3. How does the cluster self-heal a killed pod?

### 1.7 Challenges

- **Challenge.** Apply a Deployment with 2 replicas. Delete a pod and watch Kubernetes recreate it. Explain what closed the gap.

### 1.8 Checklist

- [ ] I declare desired state, not imperative steps.
- [ ] I understand controllers reconcile spec vs status.
- [ ] My manifests are version-controlled.
- [ ] I rely on self-healing rather than manual restarts.

### 1.9 Best practices

- Keep manifests in version control (GitOps).
- Express intent declaratively; let controllers act.
- Treat the cluster's desired state as the source of truth.

### 1.10 Anti-patterns

- Imperative `kubectl` edits that drift from manifests.
- Manually managing individual containers.
- Snowflake clusters configured by hand.

### 1.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Config drift | Imperative changes | Apply from version-controlled manifests |
| Pods not recovering | Wrong/no controller | Use a Deployment/ReplicaSet |
| Surprised by changes | Out-of-band edits | Reconcile from declared state |

### 1.12 References

- B. Burns, J. Beda, K. Hightower, *Kubernetes: Up and Running*, 3rd ed. (O'Reilly, 2022) — ISBN 978-1098110208.
- Kubernetes docs, "Concepts": https://kubernetes.io/docs/concepts/.

---

## Chapter 2 — Pods, Deployments, and Services

### 2.1 Introduction

Three objects cover most workloads. A **Pod** is the smallest deployable unit — one or more containers sharing network/storage. A **Deployment** manages a set of identical Pods (replicas, rolling updates, self-healing). A **Service** gives a stable network endpoint to a changing set of Pods. Together: Deployment runs your app, Service exposes it.

### 2.2 Business context

Pods are ephemeral — they come and go, with changing IPs — so you never address them directly. Deployments make running many copies and updating them safely routine, and Services provide the stable address and load balancing that let clients reach the app despite pod churn. Understanding this trio is the minimum to deploy a real service reliably; misusing it (e.g. addressing pods directly) causes brittle, broken connectivity.

### 2.3 Theoretical concepts: the trio

```mermaid
flowchart TB
    deploy["Deployment: manages N identical Pods, rolling updates"] --> pods["Pods (ephemeral, may be replaced)"]
    svc["Service: stable virtual IP/DNS + load balancing"] --> pods
```

- **Pod** — your container(s) plus shared network/volume; ephemeral and replaceable.
- **Deployment** — declares replica count, handles rolling updates and rollbacks, recreates failed Pods.
- **Service** — a stable name/IP that load-balances to the current set of healthy Pods (selected by labels), so clients don't track individual Pod IPs.

### 2.4 Architecture: client → Service → Pods

```mermaid
flowchart LR
    client["Client"] --> svc["Service (stable endpoint)"]
    svc --> p1["Pod"]
    svc --> p2["Pod"]
    svc --> p3["Pod"]
    deploy["Deployment maintains the Pods"] -.-> p1
```

### 2.5 Real example

**Scenario.** A frontend must reach a backend whose pods are recreated and rescheduled constantly.

**Problem.** Pod IPs change; hardcoding them breaks connectivity on every restart.

**Solution.** A Service gives the backend a stable DNS name; the frontend calls that.

**Implementation.**

```yaml
apiVersion: v1
kind: Service
metadata: { name: backend }
spec:
  selector: { app: backend }      # routes to any Pod with this label
  ports: [ { port: 80, targetPort: 8080 } ]
# frontend calls http://backend  (stable DNS) — never a Pod IP
```

**Result.** The frontend reaches the backend via the stable `backend` name; the Service load-balances across whatever healthy Pods exist, surviving pod churn and scaling. Connectivity no longer breaks on restart.

**Future improvements.** Add an Ingress/Gateway for external traffic; set readiness probes so the Service only routes to ready Pods.

### 2.6 Exercises

1. Why don't you address Pods directly?
2. What does a Deployment add over a bare Pod?
3. How does a Service find the right Pods?

### 2.7 Challenges

- **Challenge.** Deploy an app via a Deployment and expose it with a Service. Scale the Deployment and confirm the Service still routes correctly.

### 2.8 Checklist

- [ ] I run apps via Deployments, not bare Pods.
- [ ] I expose Pods through Services, not direct IPs.
- [ ] Services select Pods by labels.
- [ ] Rolling updates/rollbacks go through the Deployment.

### 2.9 Best practices

- Use Deployments for stateless apps; Services for stable access.
- Select Pods by clear, consistent labels.
- Let the Service handle load balancing and pod churn.

### 2.10 Anti-patterns

- Hardcoding Pod IPs.
- Running long-lived apps as bare Pods (no self-healing/updates).
- Inconsistent labels breaking Service selection.

### 2.11 Troubleshooting

| Symptom | Likely cause | Action |
|---------|--------------|--------|
| Connectivity breaks on restart | Addressing Pods directly | Use a Service's stable endpoint |
| No self-healing/rolling update | Bare Pod, no Deployment | Wrap in a Deployment |
| Service routes to nothing | Label selector mismatch | Align Service selector with Pod labels |

### 2.12 References

- B. Burns, J. Beda, K. Hightower, *Kubernetes: Up and Running*, 3rd ed. (O'Reilly, 2022) — ISBN 978-1098110208.
- Kubernetes docs, "Workloads" & "Services": https://kubernetes.io/docs/concepts/.

---

> **End of Part I.** You can now reason about Kubernetes via its core model — declare desired state and let controllers reconcile reality toward it (self-healing) — and the three workhorse objects: Pods (ephemeral units), Deployments (managing replicas and rolling updates), and Services (stable endpoints load-balancing across pod churn). **Part II — Operations** (Chapter 3) covers scaling (manual and autoscaling), health probes (liveness/readiness), and configuration/secrets so workloads are robust and properly wired.

<!--APPEND-PART-II-->
