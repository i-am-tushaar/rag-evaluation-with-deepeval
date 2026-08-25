# Optimization 01 - Retriever Evaluation

## Objective

Improve the baseline retriever performance by optimizing the chunking configuration.

## Change from Baseline

| Parameter | Baseline | Optimization 01 |
|---|---:|---:|
| Chunk Size | 750 | 1000 |
| Chunk Overlap | 100 | 150 |

The retriever, embedding model, and `top_k` were kept unchanged.

## Configuration

| Parameter | Value |
|---|---|
| Retriever | `base_k5` |
| Search Type | Similarity |
| Top K | 5 |
| Embedding Model | `sentence-transformers/all-MiniLM-L6-v2` |
| Chunk Size | 1000 |
| Chunk Overlap | 150 |
| Test Cases | 15 |
| Threshold | 0.7 |
| Judge Model | `openai/gpt-oss-20b` |

## Results

| Metric | Baseline | Optimization 01 | Change |
|---|---:|---:|---:|
| Contextual Recall | 0.80 | 0.83 | +0.03 |
| Contextual Precision | 0.80 | 0.97 | +0.17 |
| Failed Cases | 5 | 3 | -2 |

## Conclusion

Optimization 01 improved both retrieval metrics.

- Contextual Recall increased from **0.80 → 0.83**.
- Contextual Precision increased from **0.80 → 0.97**.
- Failed test cases decreased from **5 → 3**.

## Decision

**Keep this configuration as the current best configuration** and use it as the baseline for the next optimization trial.

## Next Step

Run the next optimization trial by changing another retriever parameter while keeping the current best configuration unchanged as the starting point.