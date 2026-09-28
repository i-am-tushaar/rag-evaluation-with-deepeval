# RAG Triad Online Evaluation

## Objective

Monitor the quality of the RAG system using three important metrics.

## RAG Triad

1. Contextual Relevancy
2. Faithfulness
3. Answer Relevancy

## 1. Contextual Relevancy

Question:

Did the retriever return useful context for the user's question?

Example:

Question:

"What is supervised learning?"

Retrieved context:

"Supervised learning uses labeled training data..."

This is relevant context.

## 2. Faithfulness

Question:

Is the generated answer supported by the retrieved context?

Example:

Context:

"Python was created by Guido van Rossum."

Answer:

"Python was created by Guido van Rossum."

High faithfulness.

If the answer adds unsupported information, faithfulness can decrease.

## 3. Answer Relevancy

Question:

Does the answer actually address the user's question?

Example:

Question:

"What is RAG?"

Answer:

"RAG combines retrieval with generation..."

This is relevant.

## Evaluation Flow

Production Trace
      ↓
Context + Question + Answer
      ↓
RAG Triad Evaluators
      ↓
Scores
      ↓
LangSmith Dashboard

## Dashboard

Add:

- Contextual Relevancy
- Faithfulness
- Answer Relevancy

## Monitoring

Track these scores over time to identify quality degradation.