# Alerts

Alerts were configured in LangSmith for both latency and cost.

***

## P95 Latency Alert

### Threshold

```text
P95 Latency >= 7 seconds
```

### Purpose

This alert notifies us when the slowest 5% of requests take 7 seconds
or longer. It helps us react quickly when users start to feel the
application is slow.

### Alert Status

**Status:** `___ (Active / Triggered / Resolved)`

**Notification Channel:** `___ (for example: Email, Slack, Webhook)`

**Note:** The peak P95 latency of about 7.1 seconds reached the threshold once during the observed window.

***

## Average Cost Alert

### Threshold

```text
Average Cost >= $7
```

### Purpose

This alert notifies us when the average cost per request reaches $7
or more. It helps us spot runaway spending, for example from very long
prompts, too much retrieved context, or a switch to a more expensive model.

### Alert Status

**Status:** `___ (Active / Triggered / Resolved)`

**Notification Channel:** `___ (for example: Email, Slack, Webhook)`

**Note:** The observed average cost is under $0.01, so this alert is not expected to trigger under current traffic.


***

## Alert Summary

| Alert | Metric | Condition | Threshold | Current Value | Peak Value | Status |
| --- | --- | --- | --- | --- | --- | --- |
| P95 Latency Alert | P95 Latency | Greater than or equal to | 7 seconds | About 5.7 seconds | About 7.1 seconds | ___ |
| Average Cost Alert | Average Cost | Greater than or equal to | $7 | Less than $0.01 | Less than $0.01 | ___ |