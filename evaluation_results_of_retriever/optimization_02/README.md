# Optimization 02 - Cross-Encoder Reranker Evaluation

## Objective

Improve retriever performance by adding a Sentence Transformer Cross-Encoder Reranker to the existing retrieval pipeline.

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
| Contextual Recall | 0.97 | 0.92 | -0.05 |
| Contextual Precision | 0.83 | 0.85 | +0.02 |
| Failed Cases | 3 | 2 | -1 |

## Conclusion

Adding the Cross-Encoder Reranker improved contextual precision from **0.83 → 0.85** and reduced failed test cases from **3 → 2**.

However, contextual recall decreased from **0.97 → 0.92**.

This indicates that the reranker improved the relevance and ranking quality of the retrieved chunks, but some relevant chunks were lost from the final top-5 results.

## Decision

**Keep this configuration for further experimentation.**

Although recall decreased, the reranker improved precision and reduced the number of failed test cases. The precision-recall trade-off should be evaluated further before selecting the final retriever configuration.

## Next Step

Use this configuration as the starting point for the next optimization trial and evaluate another retrieval parameter, such as the embedding model or `top_k`.