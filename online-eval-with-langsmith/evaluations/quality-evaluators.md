# Quality Evaluators

This file documents the three online evaluators configured to check
quality on every production trace, together known as the RAG Triad.

***

## Contextual Relevancy Evaluator

| Field | Value |
| --- | --- |
| Evaluator | DeepEval Contextual Relevancy |
| Runs On | Retriever output |
| Score Range | 0 to 1 |
| Direction | Higher is better |
| Threshold | `___` |

### What It Checks

Whether the retrieved context is relevant to the input query.

***

## Faithfulness Evaluator

| Field | Value |
| --- | --- |
| Evaluator | DeepEval Faithfulness |
| Runs On | LLM generation, checked against retrieved context |
| Score Range | 0 to 1 |
| Direction | Higher is better |
| Threshold | `___` |

### What It Checks

Whether the generated response is factually consistent with the
retrieved context, catching hallucinations.

***

## Answer Relevancy Evaluator

| Field | Value |
| --- | --- |
| Evaluator | DeepEval Answer Relevancy |
| Runs On | LLM generation, checked against the input query |
| Score Range | 0 to 1 |
| Direction | Higher is better |
| Threshold | `___` |

### What It Checks

Whether the generated response directly and completely addresses the
input query.

***

## Evaluator Configuration

`___ (model used for judging, any custom prompt or config passed to DeepEval)`