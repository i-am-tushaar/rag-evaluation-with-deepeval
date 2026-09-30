# Operational Metrics

Operational metrics track the cost and speed of running the RAG
application in production.

***

## Latency

### P95 Latency

| Field | Value |
| --- | --- |
| P95 Latency (latest) | About 5.7 seconds |
| Peak P95 Latency | About 7.1 seconds |
| Lowest P95 Latency | About 3.2 seconds |
| Monitoring Window | Last 1 hour (9/28/26) |

### P99 Latency

| Field | Value |
| --- | --- |
| P99 Latency | Not yet added to dashboard |
| Monitoring Window | N/A |

*P99 latency is listed as a tracked metric in the README but is not
yet configured as a chart on the current LangSmith dashboard. Add a
P99 latency chart in LangSmith and fill this in once available.*

### Monitoring Purpose

Latency is monitored to identify slow requests and understand the
performance experienced by the majority of users, with P99 used to
catch worst case outliers that P95 can miss.

### Observation

P95 latency started at about 3.2 seconds and rose steadily to about
4.7 seconds. It then spiked to about 6.9 seconds, dropped to about 3.9
seconds, and rose again to about 4.8 seconds. A second spike reached
about 7.1 seconds, which touched the 7 second alert threshold. After
the second spike, latency settled between about 5.4 and 5.7 seconds.
The spikes are likely caused by the mix of queries and the multi step
pipeline (retriever, reranker, and LLM generation).

***

## Cost

### Average Cost

| Field | Value |
| --- | --- |
| Average Cost | Less than $0.01 per request |
| Monitoring Window | Last 1 hour (9/28/26) |

### P95 Cost

| Field | Value |
| --- | --- |
| P95 Cost | Not yet added to dashboard |
| Monitoring Window | N/A |

*P95 cost is listed as a tracked metric in the README but is not yet
configured as a chart on the current LangSmith dashboard. Add a P95
cost chart in LangSmith and fill this in once available.*

### Monitoring Purpose

Cost is monitored to understand the typical and worst case cost of
processing RAG requests, and to catch unexpected cost increases early.

### Observation

The average total cost stayed very close to $0.00 for the whole
window. The line moved only slightly and never reached the $0.01 mark
on the chart. This means each RAG request is very cheap to run.