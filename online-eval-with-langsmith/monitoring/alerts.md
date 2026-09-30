# Alerts

Alerts were configured in LangSmith across operational, safety, and
quality metrics, so the team is notified as soon as any of them crosses
an acceptable threshold.

***

## Operational Alerts

### P95 Latency Alert

```text
P95 Latency >= 7 seconds
```

**Status:** Not yet confirmed in LangSmith Alerts tab

### Average Cost Alert

```text
Average Cost >= $7
```

**Status:** Not yet confirmed in LangSmith Alerts tab

*Note: observed average cost is under $0.01, so a $7 threshold will
almost never fire. Consider lowering it, for example to $0.05, if you
want the alert to be useful at current traffic levels.*

***

## Safety Alerts

### Toxicity Alert

```text
Toxicity Score >= 0.5
```

**Status:** Not yet created in LangSmith

***

## Quality Alerts

### Contextual Relevancy Alert

```text
Contextual Relevancy <= 0.7
```

**Status:** Not yet created in LangSmith

### Faithfulness Alert

```text
Faithfulness <= 0.7
```

**Status:** Not yet created in LangSmith

### Answer Relevancy Alert

```text
Answer Relevancy <= 0.7
```

**Status:** Not yet created in LangSmith

***

## Alert Summary

### Operational

| Alert | Condition | Threshold | Current Value | Status |
| --- | --- | --- | --- | --- |
| P95 Latency | Greater than or equal to | 7 seconds | About 5.7s (peak 7.1s) | Not yet confirmed |
| Average Cost | Greater than or equal to | $7 | Less than $0.01 | Not yet confirmed |

### Safety

| Alert | Condition | Threshold | Current Value | Status |
| --- | --- | --- | --- | --- |
| Toxicity | Greater than or equal to | 0.5 | Not yet added to dashboard | Not yet created |

### Quality

| Alert | Condition | Threshold | Current Value | Status |
| --- | --- | --- | --- | --- |
| Contextual Relevancy | Less than or equal to | 0.7 | Not yet added to dashboard | Not yet created |
| Faithfulness | Less than or equal to | 0.7 | Not yet added to dashboard | Not yet created |
| Answer Relevancy | Less than or equal to | 0.7 | Not yet added to dashboard | Not yet created |