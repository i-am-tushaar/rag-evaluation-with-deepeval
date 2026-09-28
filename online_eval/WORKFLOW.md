# Online Evaluation Workflow

## Phase 1: Setup

1. Create LangSmith project.
2. Generate API key.
3. Add API key to `.env`.
4. Install LangSmith.
5. Enable tracing.

## Phase 2: Add Tracing

Add LangSmith tracing to:

- RAG pipeline
- Retriever
- Reranker
- LLM generation if required

## Phase 3: Run the Application

Run the RAG pipeline normally.

Example:

python -m src.rag_pipeline

Verify that traces appear in LangSmith.

## Phase 4: Validate Trace

Check:

- Input
- Output
- Retriever
- Reranker
- LLM
- Execution time
- Token usage
- Cost where available
- Errors

## Phase 5: Generate Sample Data

Run the pipeline at least 5 times with representative questions.

Example:

Question 1
Question 2
Question 3
Question 4
Question 5

Use different realistic queries instead of sending exactly the same query every time.

## Phase 6: Monitor Latency

Collect:

- Individual request latency
- Average latency
- P95 latency
- P99 latency

P95 means:

95% of requests completed within this latency.

## Phase 7: Monitor Cost

Collect:

- Cost per request
- Average cost
- P95 cost
- Total cost

Cost depends on model usage and token consumption.

## Phase 8: Create Dashboard

Create LangSmith dashboard containing:

- Latency P95
- Cost P95
- Toxicity
- Faithfulness
- Contextual Relevancy
- Answer Relevancy

## Phase 9: Create Alerts

Create alerts for important thresholds.

Examples:

High P95 latency
High toxicity
High cost
Quality degradation

## Phase 10: Create Online Evaluators

Configure:

1. Toxicity evaluator
2. Contextual Relevancy evaluator
3. Faithfulness evaluator
4. Answer Relevancy evaluator

## Phase 11: Run Online Evaluation

New production traces are evaluated automatically according to the configured evaluator rules.

## Phase 12: Create/Grow Dataset

Use useful production examples to create or expand a LangSmith dataset.

These examples can later be used for offline evaluation and regression testing.

## Final Flow

Application
→ Trace
→ Metrics
→ Online Evaluators
→ Dashboard
→ Alerts
→ Production Examples
→ Dataset
→ Future Offline Evaluation