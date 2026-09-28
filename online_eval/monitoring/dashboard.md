# Dashboard

## Dashboard Name

`Customer Doubt Solver RAG - Online Evaluation`

The dashboard was created in LangSmith to monitor the operational
performance of the RAG application.

***

## Dashboard Metrics

The dashboard currently monitors:

* **P95 Latency**
* **Average Cost**

***

## Dashboard Settings

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