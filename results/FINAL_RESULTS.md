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

## Leakage

| Metric                 | Score |
| ---------------------- | ----: |
| Course Content Leakage |   99% |
| Prompt Leakage         |   96% |
| PII Leakage            |   96% |

### Leakage Evaluation Summary

The leakage evaluation was performed across prompt, course content, and PII leakage test cases. The final scores show strong protection against sensitive information exposure.

* **Course Content Leakage:** 99%
* **Prompt Leakage:** 96%
* **PII Leakage:** 96%

The PII leakage score improved to **96%** after strengthening the system prompt and adding XML tagging to better identify and protect sensitive data.

## Scope Adherence

| Metric          |              Score |
| --------------- | -----------------: |
| Scope Adherence |                96% |
| Threshold       |                0.3 |
| Judge Model     | openai/gpt-oss-20b |

### Scope Adherence Evaluation Summary

The scope adherence evaluation measures whether the RAG system stays within the provided course context, answers the student's question without adding unsupported outside knowledge, and avoids unrelated information.

The final scope adherence score is **96%**, showing strong adherence to the defined response scope.

The evaluation includes edge cases such as **mixed queries, multi-part questions, irrelevant information, and attempts to override the defined scope**.

### Scope Adherence Improvement Recommendations

To further improve scope adherence performance:

* **Better Model:** Use a more capable model with stronger instruction-following capabilities.
* **Better Prompt:** Strengthen scope instructions for mixed queries and edge cases.
* **Guardrails:** Add checks to prevent unsupported or out-of-context information.
* **Golden Dataset:** Add more challenging mixed-query and edge-case examples.
* **Fine-Tuning:** Fine-tune the model with examples that demonstrate strict context-based answering.
