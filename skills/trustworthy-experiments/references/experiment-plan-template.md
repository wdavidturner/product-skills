# Experiment Plan (A/B Test) Template

Use this as a pre-registered plan before you launch.

## 1) Summary

- **Experiment name:** `…`
- **Owner / DRI:** `…`
- **Start date:** `…`
- **Planned end date (or sample-size stop):** `…`
- **Surface:** `…` (web, iOS, Android, email, backend API, etc.)
- **Randomization unit:** `user_id` / `account_id` / `session_id` / other: `…`

## 2) Hypothesis

- **We believe that** `change`
- **for** `target users`
- **will** `expected user behavior change`
- **because** `mechanism`

## 3) Variants

### Control (A)
- `Current experience`

### Treatment (B)
- `New experience`

### Allocation
- **Planned split:** `50/50` (or `…`)
- **Ramp plan:** `…` (e.g., 1% → 10% → 50%, with SRM + guardrail checks at each step)

## 4) Eligibility & Exclusions

- **Inclusion:** `…`
- **Exclusions:** `…` (employees, bots, internal traffic, already-exposed cohorts, etc.)
- **Concurrency risks:** `…` (overlapping experiments on same surface/users)

## 5) Metrics (OEC + Guardrails)

### Primary success metric (OEC proxy)
- **Metric:** `…`
- **Definition:** `…` (numerator/denominator, event names, attribution window)
- **Why it predicts long-term value:** `…`

### Guardrails (must not regress)
- `Metric` — threshold: `…`
- `Metric` — threshold: `…`

### Debug metrics (diagnostics only)
- `…` (do not “ship” based solely on these)

## 6) Instrumentation & Data Quality

- **Event parity:** Confirm logging is identical across variants except the intended change.
- **Exposure logging:** Record exposure at assignment time (`experiment_id`, `variant`, `unit_id`, timestamp).
- **Persistent assignment:** Ensure the same unit stays in the same variant across sessions/devices as intended.
- **Bot filtering:** `…`
- **Latency/perf tracking:** `…`

## 7) Power, Sample Size, Runtime

- **Baseline rate:** `…`
- **MDE:** `…` (absolute or relative)
- **Alpha / power:** `0.05` / `0.8` (or `…`)
- **Required sample size:** `…` per variant
- **Minimum runtime:** `≥ 1 full week` (capture weekday/weekend), plus `…` for novelty/seasonality if needed

## 8) Stopping Rules (pre-commit)

- **Stop when:** `required sample size reached` AND `minimum runtime reached`
- **No peeking policy:** `…` (e.g., dashboards allowed for guardrails only, no decision until stop)
- **If SRM is detected:** pause / fix / restart: `…`

## 9) Analysis Plan

- **Primary comparison:** `B vs A` on primary metric
- **SRM check:** required before interpreting outcomes
- **Multiple comparisons:** list additional metrics and how you’ll adjust or interpret: `…`
- **Segment cuts (pre-registered):** `…` (device, geo, new vs. existing, etc.)
- **Novelty/primacy:** compare early vs late period: `…`

## 10) Decision Rules

- **Ship if:** primary metric improves by `≥ …` AND guardrails not worse than thresholds AND validity checks pass
- **Don’t ship if:** flat / underpowered / guardrail regression / validity threat
- **If surprising win:** replicate before rollout (Twyman’s Law)

## 11) Rollout & Post-Experiment

- **Rollout plan:** `…`
- **Monitoring after ship:** `…`
- **Write-up location:** `…` (link to doc/issue)
- **Learnings:** `…`
