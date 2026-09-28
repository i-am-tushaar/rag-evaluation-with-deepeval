# Online Evaluation Results

This folder contains the results, observations, screenshots, and monitoring
records from the LangSmith Online Evaluation setup for the RAG application.

***

## LangSmith Project

**Project Name:**

`Customer_Doubt_Solver_RAG_Project`

***

## Initial Traffic Simulation

The RAG pipeline was executed approximately **7 to 8 times** with different
representative queries to simulate multiple real world requests.

The generated LangSmith traces were collected and used to validate:

* RAG pipeline execution
* Retriever execution
* Reranker execution
* LLM generation
* Latency
* Cost
* Trace logging

### Number of Test Runs

**7 to 8 runs**

***

## LangSmith Traces

Each RAG pipeline execution generated a trace in the
`Customer_Doubt_Solver_RAG_Project` LangSmith project.

The traces were used to inspect:

* Input query
* Retrieved context
* Reranking
* LLM execution
* Final response
* Execution latency
* Token usage
* Cost

![LangSmith Traces](screenshots/traces.png)

***

# Dashboard

## Dashboard Name

`Customer Doubt Solver RAG - Online Evaluation`

The dashboard was created in LangSmith to monitor the operational
performance of the RAG application.

### Dashboard Metrics

The dashboard currently monitors:

* **P95 Latency**
* **Average Cost**

### Dashboard Settings

* **Time Range:** Last 1 hour
* **Observation Date:** 9/28/26
* **Observed Period:** Approximately 8:40 PM to 9:20 PM

***

## P95 Latency

P95 latency represents the latency value below which approximately
95% of requests fall.

### Observed Value

**P95 Latency (latest reading):** `About 5.7 seconds`

**Peak P95 Latency:** `About 7.1 seconds`

**Lowest P95 Latency:** `About 3.2 seconds`

**Monitoring Window:** `Last 1 hour (9/28/26)`

### Observation

* P95 latency started at about 3.2 seconds and rose steadily to about 4.7 seconds.
* It then spiked to about 6.9 seconds, dropped to about 3.9 seconds, and rose again to about 4.8 seconds.
* A second spike reached about 7.1 seconds, which touched the 7 second alert threshold.
* After the second spike, latency settled between about 5.4 and 5.7 seconds.
* The spikes are likely caused by the mix of queries and the multi step pipeline (retriever, reranker, and LLM generation).

### Monitoring Purpose

P95 latency is monitored to identify slow requests and understand the
performance experienced by the majority of users.

***

## Average Cost

Average cost represents the average model and API cost per request over
the selected monitoring period.

### Observed Value

**Average Cost:** `Less than $0.01 per request`

**Monitoring Window:** `Last 1 hour (9/28/26)`

### Observation

* The average total cost stayed very close to $0.00 for the whole window.
* The line moved only slightly and never reached the $0.01 mark on the chart.
* This means each RAG request is very cheap to run.

### Monitoring Purpose

Average cost is monitored to understand the typical cost of processing
RAG requests and to catch unexpected cost increases early.

***

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

### Screenshot

![P95 Latency Alert](screenshots/p95_latency_alert.png)

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

### Screenshot

![Average Cost Alert](screenshots/average_cost_alert.png)

***

## Alert Summary

| Alert | Metric | Condition | Threshold | Current Value | Peak Value | Status |
| --- | --- | --- | --- | --- | --- | --- |
| P95 Latency Alert | P95 Latency | Greater than or equal to | 7 seconds | About 5.7 seconds | About 7.1 seconds | ___ |
| Average Cost Alert | Average Cost | Greater than or equal to | $7 | Less than $0.01 | Less than $0.01 | ___ |