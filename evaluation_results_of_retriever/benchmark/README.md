# Final Retriever Benchmark

## Objective

Benchmark the final optimized RAG retriever against the baseline and all previous optimization trials.

The benchmark uses the same golden dataset, evaluation metrics, threshold, and judge model to ensure a fair comparison.

## Final Retriever Configuration

| Parameter | Value |
|---|---|
| Retriever | `cross_encoder_reranker` |
| Search Type | Similarity + Cross-Encoder Reranking |
| Embedding Model | `BAAI/bge-base-en-v1.5` |
| Reranker | `cross-encoder/ms-marco-MiniLM-L-6-v2` |
| Fetch K | 10 |
| Top K | 5 |
| Chunk Size | 1000 |
| Chunk Overlap | 150 |
| Test Cases | 15 |
| Threshold | 0.7 |
| Judge Model | `openai/gpt-oss-20b` |

## Historical Comparison

| Experiment | Recall | Precision | Average Score | Failed Cases |
|---|---:|---:|---:|---:|
| Baseline | 0.80 | 0.80 | 0.800 | 5 |
| Optimization 01 | 0.83 | 0.97 | 0.900 | 3 |
| Optimization 02 | 0.92 | 0.85 | 0.885 | 2 |
| Optimization 03 | 0.98 | 0.85 | 0.915 | 3 |
| Final Benchmark | TBD | TBD | TBD | TBD |

## Benchmark Purpose

The final benchmark verifies whether the optimized retriever consistently performs well across the complete golden dataset.

The benchmark should use all 15 test cases.

## Current Best Configuration

Optimization 03 currently has the highest average score of `0.915` and the highest contextual recall of `0.98`.

However, the final benchmark result will be used as the official final performance record.

## Evaluation Metrics

### Contextual Recall

Measures whether the retrieved context contains the information required to answer the expected answer.

### Contextual Precision

Measures whether the retrieved context is relevant and well-ranked.

## Final Decision

The final retriever configuration will be selected based on the final benchmark results and comparison with previous experiments.

## Run Benchmark

From the project root:

```bash
python -m benchmark.final_benchmark