# LangSmith Alerts

## Purpose

Alerts notify the team when an important production metric crosses a defined threshold.

## Alert 1: High Latency

Metric:

P95 latency

Condition:

P95 latency > defined threshold

Action:

Send notification.

## Alert 2: High Cost

Metric:

P95 cost

Condition:

P95 cost > defined threshold

Action:

Send notification.

## Alert 3: Toxicity

Metric:

Toxicity evaluation

Condition:

Toxicity exceeds the acceptable threshold.

Action:

Send notification.

## Alert 4: Quality Degradation

Metric:

Faithfulness / Contextual Relevancy / Answer Relevancy

Condition:

Metric falls below the defined threshold.

Action:

Investigate affected traces.

## Important

Thresholds should be based on the application's actual baseline and SLO/quality requirements.

Do not choose arbitrary thresholds without observing normal production behavior.