# Quality Metrics

Quality metrics track whether the RAG application retrieves the right
context and produces answers that are accurate and relevant.

***

## Contextual Relevancy

| Field | Value |
| --- | --- |
| Evaluator | DeepEval Contextual Relevancy |
| Score Range | 0 to 1 |
| Direction | Higher is better |
| Average Score | Not yet added to dashboard |
| Threshold | 0.7 (DeepEval default) |

***

## Faithfulness

| Field | Value |
| --- | --- |
| Evaluator | DeepEval Faithfulness |
| Score Range | 0 to 1 |
| Direction | Higher is better |
| Average Score | Not yet added to dashboard |
| Threshold | 0.7 (DeepEval default) |

***

## Answer Relevancy

| Field | Value |
| --- | --- |
| Evaluator | DeepEval Answer Relevancy |
| Score Range | 0 to 1 |
| Direction | Higher is better |
| Average Score | Not yet added to dashboard |
| Threshold | 0.7 (DeepEval default) |

*None of the three quality metrics have charts on the current
LangSmith dashboard yet. Add charts for each in LangSmith and fill in
the observed scores once available.*

***

## Monitoring Purpose

These three metrics together, known as the RAG Triad, catch retrieval
failures (contextual relevancy), hallucinations (faithfulness), and
answers that drift off topic (answer relevancy).