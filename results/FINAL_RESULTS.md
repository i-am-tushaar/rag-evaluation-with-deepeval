# RAG Evaluation Results

## Retriever

| Metric               | Score |
| -------------------- | ----: |
| Contextual Recall    |   95% |
| Contextual Precision |   93% |

## Generator

| Metric           | Score |
| ---------------- | ----: |
| Faithfulness     |   98% |
| Answer Relevancy |   98% |

## Full RAG Pipeline

| Metric               | Score |
| -------------------- | ----: |
| Contextual Relevancy |   90% |
| Faithfulness         |   96% |
| Answer Relevancy     |   94% |

## Application

| Metric       | Score |
| ------------ | ----: |
| Correctness  |   95% |
| Completeness |   76% |
| Style        |   84% |

## Toxicity

| Metric                        |              Score |
| ----------------------------- | -----------------: |
| Toxicity Evaluation Pass Rate |               100% |
| Passed Cases                  |                5/5 |
| Failed Cases                  |                0/5 |
| Threshold                     |                0.3 |
| Judge Model                   | openai/gpt-oss-20b |

### Toxicity Evaluation Summary

All 5 tested cases passed the toxicity evaluation. The toxicity score for each case was within the configured threshold of **0.3 or lower**.

### Toxicity Improvement Recommendations

To further improve toxicity performance:

* **Better Model:** Use a more capable model that naturally produces safer responses.
* **Better Prompt:** Improve the system prompt with clear instructions to avoid toxic, insulting, or degrading language.
* **Guardrails:** Add input/output guardrails to detect and prevent toxic content.
* **Fine-Tuning:** Fine-tune the model using safe, non-toxic response examples.
