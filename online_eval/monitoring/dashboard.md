# LangSmith Dashboard

## Dashboard Name

RAG Online Evaluation Dashboard

## Purpose

The dashboard provides a single view of RAG application performance, cost and quality.

## Dashboard Panels

### Panel 1: Latency P95

Metric:

P95 latency

Purpose:

Monitor slow production requests.

### Panel 2: Cost P95

Metric:

P95 cost

Purpose:

Monitor unusually expensive requests.

### Panel 3: Toxicity

Metric:

Toxicity evaluator score

Purpose:

Monitor unsafe or toxic responses.

### Panel 4: Faithfulness

Metric:

Faithfulness score

Purpose:

Monitor whether answers are supported by retrieved context.

### Panel 5: Contextual Relevancy

Metric:

Contextual relevancy score

Purpose:

Monitor retrieval quality.

### Panel 6: Answer Relevancy

Metric:

Answer relevancy score

Purpose:

Monitor whether answers address user questions.

## Dashboard Interpretation

Example:

Latency P95 increases
→ Application may be becoming slower.

Cost P95 increases
→ Some requests may be consuming more tokens or using expensive models.

Faithfulness decreases
→ Generated answers may not be sufficiently supported by retrieved context.

Contextual Relevancy decreases
→ Retrieval may be returning less relevant documents.

Toxicity increases
→ More responses may contain problematic language.

## Dashboard Location

The actual dashboard is created and stored in LangSmith.

This file documents the dashboard configuration.