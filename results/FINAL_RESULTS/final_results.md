# RAG Evaluation Results

The RAG Evaluation Suite is divided into three main evaluation levels:

1. Component-Level Evaluations
2. Pipeline-Level Evaluations
3. Application-Level Evaluations

---

# 1. Component-Level Evaluations

Component-level evaluations check the individual components of the RAG system.

## 1.1 Retriever Evaluation

The retriever is responsible for finding relevant documents or chunks for the user’s question.

| Metric | Score |
| -------------------- | ----: |
| Contextual Recall | 95% |
| Contextual Precision | 93% |

### Retriever Evaluation Summary

The retriever achieved:

- **Contextual Recall:** 95%
- **Contextual Precision:** 93%

These metrics measure how effectively the retriever finds relevant and useful context for the user’s question.

---

## 1.2 Generator Evaluation

The generator is responsible for creating the final answer using the retrieved context.

| Metric | Score |
| ---------------- | ----: |
| Faithfulness | 98% |
| Answer Relevancy | 98% |

### Generator Evaluation Summary

The generator achieved:

- **Faithfulness:** 98%
- **Answer Relevancy:** 98%

These metrics measure whether the generated answer is supported by the retrieved context and relevant to the user’s question.

---

# 2. Pipeline-Level Evaluations

Pipeline-level evaluation checks the complete RAG pipeline, including retrieval and answer generation.

## 2.1 RAG Triad Evaluation

The RAG Triad evaluates the quality of the complete RAG pipeline.

| Metric | Score |
| -------------------- | ----: |
| Contextual Relevancy | 90% |
| Faithfulness | 96% |
| Answer Relevancy | 94% |

### RAG Triad Evaluation Summary

The full RAG pipeline achieved:

- **Contextual Relevancy:** 90%
- **Faithfulness:** 96%
- **Answer Relevancy:** 94%

These metrics evaluate:

- Whether the retrieved context is relevant.
- Whether the answer is supported by the retrieved context.
- Whether the final answer is relevant to the user’s question.

---

# 3. Application-Level Evaluations

Application-level evaluations check the final user-facing RAG application.

Application-level evaluations are divided into:

1. Application Quality
2. Safety
3. Operations

---

## 3.1 Application Quality

Application quality evaluates the quality of the final answer shown to the user.

### 3.1.1 Application Quality Evaluation

| Metric | Score |
| ---------------- | ----: |
| Correctness | 95% |
| Completeness | 76% |
| Style | 84% |

### Application Quality Evaluation Summary

The application achieved:

- **Correctness:** 95%
- **Completeness:** 76%
- **Style:** 84%

### Application Quality Metric Description

- **Correctness:** Measures whether the final answer is factually correct.
- **Completeness:** Measures whether the answer includes all important information required by the question.
- **Style:** Measures whether the answer is clear, readable, and appropriately formatted.

---

## 3.2 Safety

Safety evaluations check whether the application produces safe responses, protects sensitive information, and follows the defined response scope.

Safety evaluations include:

1. Toxicity Evaluation
2. Leakage Evaluation
3. Scope Adherence Evaluation

---

### 3.2.1 Toxicity Evaluation

This evaluation checks whether the system produces toxic, insulting, or degrading responses.

| Metric | Score |
| ----------------------------- | -----------------: |
| Toxicity Evaluation Pass Rate | 100% |
| Passed Cases | 5/5 |
| Failed Cases | 0/5 |
| Threshold | 0.3 |
| Judge Model | openai/gpt-oss-20b |

#### Toxicity Evaluation Summary

All 5 tested cases passed the toxicity evaluation.

The toxicity score for each case was within the configured threshold of **0.3 or lower**.

#### Toxicity Improvement Recommendations

To further improve toxicity performance:

- **Better Model:** Use a more capable model that naturally produces safer responses.
- **Better Prompt:** Improve the system prompt with clear instructions to avoid toxic, insulting, or degrading language.
- **Guardrails:** Add input/output guardrails to detect and prevent toxic content.
- **Fine-Tuning:** Fine-tune the model using safe, non-toxic response examples.

---

### 3.2.2 Leakage Evaluation

This evaluation checks whether the system exposes course content, prompts, or personally identifiable information.

| Metric | Score |
| ---------------------- | ----: |
| Course Content Leakage | 99% |
| Prompt Leakage | 96% |
| PII Leakage | 96% |

#### Leakage Evaluation Summary

The leakage evaluation was performed across:

- Prompt leakage test cases.
- Course content leakage test cases.
- PII leakage test cases.

The final scores were:

- **Course Content Leakage:** 99%
- **Prompt Leakage:** 96%
- **PII Leakage:** 96%

The PII leakage score improved to **96%** after strengthening the system prompt and adding XML tagging to better identify and protect sensitive data.

---

### 3.2.3 Scope Adherence Evaluation

This evaluation checks whether the RAG system stays within the provided course context.

| Metric | Score |
| --------------- | ----: |
| Scope Adherence | 96% |
| Threshold | 0.3 |
| Judge Model | openai/gpt-oss-20b |

#### Scope Adherence Evaluation Summary

The scope adherence evaluation measures whether the RAG system:

- Stays within the provided course context.
- Answers the student’s question without adding unsupported outside knowledge.
- Avoids unrelated information.

The final scope adherence score is **96%**, showing strong adherence to the defined response scope.

The evaluation includes edge cases such as:

- Mixed queries.
- Multi-part questions.
- Irrelevant information.
- Attempts to override the defined scope.

#### Scope Adherence Improvement Recommendations

To further improve scope adherence performance:

- **Better Model:** Use a more capable model with stronger instruction-following capabilities.
- **Better Prompt:** Strengthen scope instructions for mixed queries and edge cases.
- **Guardrails:** Add checks to prevent unsupported or out-of-context information.
- **Golden Dataset:** Add more challenging mixed-query and edge-case examples.
- **Fine-Tuning:** Fine-tune the model with examples that demonstrate strict context-based answering.

---

## 3.3 Operations

Operations evaluations measure the runtime performance and latency of the RAG application.

### 3.3.1 Latency Evaluation

The latency evaluation measures how quickly the RAG application retrieves context and generates an answer.

The latency evaluation shows that **generation is the main bottleneck**.

The mean generation latency was **12334.0 ms**, while the mean retrieval latency was **1634.6 ms**. Therefore, generation optimization should be prioritized.

#### Main Latency Issues

- End-to-end p95 latency was **17711.3 ms** against a target of **3000 ms**.
- TTFT p95 latency was **17222.3 ms** against a target of **1200 ms**.
- Generation mean latency was **12334.0 ms**.
- Average answer length was **965 characters**.
- Retrieval p95 latency was **2571.1 ms**.

#### Latency Improvement Recommendations

1. **Use a Faster LLM**

   Use a smaller or faster model to reduce generation time.

2. **Reduce Output Length**

   Add prompt instructions to generate concise answers and reduce the maximum output token limit.

3. **Enable Streaming**

   Enable streaming so that users can see the first token earlier.

   Streaming improves perceived latency but may not reduce total answer generation time.

4. **Reduce Retrieved Context**

   Reduce `top_k` and `fetch_k` to send fewer document chunks to the LLM.

5. **Optimize the Prompt**

   Remove unnecessary instructions, duplicate context, and irrelevant information.

6. **Optimize Chunking**

   Test smaller chunk sizes and lower overlap values to reduce the amount of context passed to the model.

7. **Add Caching**

   Cache repeated queries and embeddings to avoid repeating the same computation.

8. **Load Models Only Once**

   Initialize embedding models, vector stores, and LLMs once during application startup instead of loading them for every request.

9. **Optimize Retrieval**

   Reduce unnecessary reranking and optimize vector database search.

10. **Use GPU Acceleration**

    Use a supported GPU environment to improve embedding, reranking, and model inference performance.

#### Recommended Optimization Order

- Use a faster LLM.
- Reduce maximum output tokens.
- Reduce prompt and context size.
- Reduce `top_k` and `fetch_k`.
- Enable streaming.
- Add caching.
- Optimize embedding and reranking.
- Test GPU acceleration.
- Run the latency evaluation again.

#### Re-evaluation

After applying the improvements, run:

```bash
python -m evals.eval_latency