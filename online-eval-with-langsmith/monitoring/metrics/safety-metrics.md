# Safety Metrics

Safety metrics track whether the RAG application generates content that
could be harmful, offensive, or inappropriate for end users.

***

## Toxicity

### Metric Details

| Field | Value |
| --- | --- |
| Evaluator | DeepEval Toxicity |
| Score Range | 0 to 1 |
| Direction | Lower is better |

### Observed Value

| Field | Value |
| --- | --- |
| Average Toxicity Score | Not yet added to dashboard |
| Threshold | 0.5 (DeepEval default) |
| Monitoring Window | N/A |

*Toxicity is listed as a tracked metric in the README but is not yet
configured as a chart on the current LangSmith dashboard. Add a
toxicity chart in LangSmith and fill this in once available.*

### Monitoring Purpose

Toxicity is monitored to make sure the RAG application never surfaces
harmful or offensive content to end users.