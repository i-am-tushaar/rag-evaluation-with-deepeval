# Online Evaluation Configuration

## LangSmith Project

Project:

rag-online-evaluation

## Tracing

Enabled:

LANGSMITH_TRACING=true

## Traced Components

- RAG Pipeline
- Retriever
- Reranker
- LLM

## Operational Metrics

- Latency
- P95 Latency
- P99 Latency
- Cost
- Average Cost
- P95 Cost

## Online Evaluators

- Toxicity
- Contextual Relevancy
- Faithfulness
- Answer Relevancy

## Dashboard

Dashboard:

RAG Online Evaluation Dashboard

Panels:

- Latency P95
- Cost P95
- Toxicity
- Contextual Relevancy
- Faithfulness
- Answer Relevancy

## Alerts

Configured alerts:

- High P95 latency
- High P95 cost
- High toxicity
- Low quality metrics

## Dataset

Dataset:

rag-online-evaluation-dataset