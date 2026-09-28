# Online Monitoring Metrics

## 1. Latency

Latency is the time required to process one request.

Example:

Request A = 1.2 seconds
Request B = 1.5 seconds
Request C = 2.0 seconds

## Average Latency

Average latency represents the mean latency across requests.

## P95 Latency

P95 tells us the latency value below which approximately 95% of requests fall.

Example:

P95 latency = 3 seconds

This means approximately 95% of requests completed within 3 seconds.

The remaining approximately 5% took longer.

## P99 Latency

P99 focuses on the slowest approximately 1% of requests.

## 2. Cost

Cost represents the estimated model/API cost associated with requests.

## Average Cost

Average cost represents the average cost per request over the selected period.

## P95 Cost

P95 cost shows the cost level below which approximately 95% of requests fall.

## Total Cost

Total cost is the sum of costs across all requests in the selected period.

## 3. Quality Metrics

### Faithfulness

Checks whether the answer is supported by the retrieved context.

### Contextual Relevancy

Checks whether the retrieved context is relevant to the user's question.

### Answer Relevancy

Checks whether the generated answer addresses the user's question.

### Toxicity

Checks whether the generated response contains toxic or harmful language.

## Operational vs Quality Metrics

Operational:

- Latency
- Cost
- Errors

Quality:

- Faithfulness
- Contextual Relevancy
- Answer Relevancy
- Toxicity