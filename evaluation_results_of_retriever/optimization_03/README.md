# Optimization 03 - Embedding Model Evaluation

## Objective

Improve retriever performance by upgrading the embedding model from `sentence-transformers/all-MiniLM-L6-v2` to `BAAI/bge-base-en-v1.5`.

The Cross-Encoder Reranker configuration from Optimization 02 was kept unchanged.

## Change from Previous Trial

| Parameter | Optimization 02 | Optimization 03 |
|---|---|---|
| Embedding Model | `sentence-transformers/all-MiniLM-L6-v2` | `BAAI/bge-base-en-v1.5` |
| Retriever | `cross_encoder_reranker` | `cross_encoder_reranker` |
| Search Type | Similarity + Cross-Encoder Reranking | Similarity + Cross-Encoder Reranking |
| Top K | 5 | 5 |

Only the embedding model was changed. The retriever, reranker, top-k, and chunking configuration were kept unchanged.

## Configuration

| Parameter | Value |
|---|---|
| Retriever | `cross_encoder_reranker` |
| Search Type | Similarity + Cross-Encoder Reranking |
| Top K | 5 |
| Embedding Model | `BAAI/bge-base-en-v1.5` |
| Chunk Size | 1000 |
| Chunk Overlap | 150 |
| Test Cases | 15 |
| Threshold | 0.7 |
| Judge Model | `openai/gpt-oss-20b` |

## Results

| Metric | Optimization 02 | Optimization 03 | Change |
|---|---:|---:|---:|
| Contextual Recall | 0.92 | **0.98** | **+0.06** |
| Contextual Precision | 0.85 | **0.85** | **0.00** |
| Failed Cases | 2 | 3 | +1 |

## Conclusion

Upgrading the embedding model from `sentence-transformers/all-MiniLM-L6-v2` to `BAAI/bge-base-en-v1.5` significantly improved contextual recall from **0.92 → 0.98** while maintaining contextual precision at **0.85**.

However, failed test cases increased from **2 → 3**.

This indicates that the BGE embedding model improved the retriever's ability to retrieve relevant information, while maintaining the same precision after Cross-Encoder reranking.

## Decision

**Keep this configuration for further experimentation.**

The combination of `BAAI/bge-base-en-v1.5` with the Cross-Encoder Reranker achieved the highest contextual recall so far at **0.98**.

Although the number of failed cases increased from 2 to 3, the significant improvement in recall makes this configuration a strong candidate for further optimization.

## Next Step

Use this configuration as the starting point for the next optimization trial and evaluate another retrieval parameter, such as `top_k`, reranker configuration, or retrieval strategy.