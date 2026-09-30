# Tracing Configuration

This file documents how LangSmith tracing is configured for the RAG
application, and what each traced component captures.

***

## LangSmith Project

**Project Name:**

`Customer_Doubt_Solver_RAG_Project`

*(Confirm this against your LangSmith sidebar. Your dashboard screenshot showed the application name as `RAG_Online_Evals`, so check whether that is the actual project name instead.)*

***

## Traced Components

### RAG Pipeline
- Captures the full end to end run for each user query.
- Records input query, final response, total latency, and total cost.

### Retriever
- Captures the query sent to the vector store.
- Records retrieved chunks, similarity scores, and retrieval latency.

### Reranker
- Captures the chunks passed in from the retriever.
- Records the reranked order and reranker latency.

### LLM
- Captures the final prompt sent to the model.
- Records the generated response, token usage, and generation latency.

***

## Trace Fields Captured

| Field | Description |
| --- | --- |
| Input query | The original user question |
| Retrieved context | Chunks returned by the retriever |
| Reranked context | Chunks after reranking |
| Final response | The LLM generated answer |
| Latency | Time taken per component and end to end |
| Token usage | Prompt and completion tokens |
| Cost | Per request cost based on token usage |
| Evaluator scores | Toxicity, Contextual Relevancy, Faithfulness, Answer Relevancy |

***

## Setup Notes

Tracing is enabled through the LangSmith SDK. Set the following
environment variables before running the pipeline:

```bash
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=<your_langsmith_api_key>
LANGCHAIN_PROJECT=Customer_Doubt_Solver_RAG_Project
```

Each traced function (retriever, reranker, LLM call) should be wrapped
with the `@traceable` decorator from `langsmith`, so every step shows
up as a nested span inside the parent RAG pipeline trace.