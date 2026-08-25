# Optimization 02 - Cross-Encoder Reranker Evaluation

## Objective

Improve retriever performance by adding a Sentence Transformer cross-encoder reranker to the existing retrieval pipeline.

## Change from Previous Trial

| Parameter | Optimization 01 | Optimization 02 |
|---|---|---|
| Retriever | `base_k5` | `cross_encoder_reranker` |
| Search Type | Similarity | Similarity + Cross-Encoder Reranking |
| Top K | 5 | 5 |

The embedding model and chunking configuration were kept unchanged.

## Configuration

| Parameter | Value |
|---|---|
| Retriever | `cross_encoder_reranker` |
| Search Type | Similarity + Cross-Encoder Reranking |
| Top K | 5 |
| Embedding Model | `sentence-transformers/all-MiniLM-L6-v2` |
| Chunk Size | 1000 |
| Chunk Overlap | 150 |
| Test Cases | 15 |
| Threshold | 0.7 |
| Judge Model | `openai/gpt-oss-20b` |

## Results

| Metric | Optimization 01 | Optimization 02 | Change |
|---|---:|---:|---:|
| Contextual Recall | 0.83 | 0.85 | +0.02 |
| Contextual Precision | 0.97 | 0.92 | -0.05 |
| Failed Cases | 3 | 2 | -1 |

## Conclusion

Adding the cross-encoder reranker improved contextual recall from **0.83 → 0.85** and reduced failed test cases from **3 → 2**.

However, contextual precision decreased from **0.97 → 0.92**.

## Decision

**Keep this configuration for further experimentation** because it achieved the highest contextual recall so far and the lowest number of failed test cases.

## Next Step

Use this configuration as the starting point for the next optimization trial and evaluate another retrieval parameter.