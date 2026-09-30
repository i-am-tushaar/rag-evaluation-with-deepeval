# Results and Observations

This file summarizes overall findings from the online evaluation period,
across all three metric categories.

***

## Summary

| Category | Status | Notes |
| --- | --- | --- |
| Operational | Reviewed | P95 latency peaked at 7.1s, touching the alert threshold. Average cost stayed under $0.01. |
| Safety | Not yet reviewed | Toxicity chart not yet added to the dashboard |
| Quality | Not yet reviewed | Contextual Relevancy, Faithfulness, and Answer Relevancy charts not yet added to the dashboard |

***

## Operational Observations

P95 latency showed two spikes during the observed 1 hour window, the
second one reaching about 7.1 seconds and touching the alert
threshold. This suggests certain queries trigger a slower path through
the retriever, reranker, or LLM generation step, and is worth
investigating further with per component latency breakdowns. Average
cost stayed consistently under $0.01 per request, so cost is not a
current concern.

***

## Safety Observations

Not yet available. Add a Toxicity chart to the LangSmith dashboard and
run enough traffic to gather a meaningful sample before filling this
in.

***

## Quality Observations

Not yet available. Add Contextual Relevancy, Faithfulness, and Answer
Relevancy charts to the LangSmith dashboard and run enough traffic to
gather a meaningful sample before filling this in.

***

## Action Items

- Add P99 Latency and P95 Cost charts to the LangSmith dashboard
- Add Toxicity, Contextual Relevancy, Faithfulness, and Answer Relevancy charts to the LangSmith dashboard
- Create alerts in LangSmith for all five metrics not yet configured
- Investigate the cause of the two P95 latency spikes observed on 9/28/26
- Reconsider the $7 Average Cost alert threshold given real costs are under $0.01