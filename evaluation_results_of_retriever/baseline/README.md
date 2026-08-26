# Baseline Retriever Evaluation

## Objective

Establish the baseline performance of the initial RAG retriever before optimization.

## Configuration

| Parameter | Value |
|---|---|
| Retriever | `base_k5` |
| Search Type | Similarity |
| Top K | 5 |
| Embedding Model | `sentence-transformers/all-MiniLM-L6-v2` |
| Chunk Size | 750 |
| Chunk Overlap | 100 |
| Test Cases | 15 |
| Threshold | 0.7 |
| Judge Model | `openai/gpt-oss-20b` |

## Results

| Metric | Score |
|---|---:|
| Contextual Recall | 80% |
| Contextual Precision | 80% |
| Average Score | 80% |

## Conclusion

The baseline retriever achieved 80% contextual recall and 80% contextual precision.

This baseline will be used to compare all subsequent optimization trials.

## Next Step

Run optimization trials and compare each configuration against this baseline.