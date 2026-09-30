# Dataset Creation

This file documents how production traces are converted into evaluation
datasets for future offline evaluation and regression testing.

***

## Purpose

Production traces that show interesting behavior, whether good or bad,
are saved into a dataset. This dataset grows over time and is later
used offline to check for regressions before shipping changes to the
RAG pipeline.

***

## Selection Criteria

Traces are added to the dataset when they meet any of these conditions:

**Failure Cases**
- Contextual Relevancy score below 0.7
- Faithfulness score below 0.7
- Answer Relevancy score below 0.7
- Toxicity score at or above 0.5
- Latency above the 7 second P95 threshold
- Cost outliers relative to the average

**Edge Cases**
- Ambiguous or unusual user queries
- Queries where retrieval returned few or no relevant chunks

**Good Examples**
- High scoring traces kept as reference examples for regression testing

***

## Dataset Growth

| Field | Value |
| --- | --- |
| Current Dataset Size | Not yet created |
| Last Updated | N/A |
| Source | Production traces from `Customer_Doubt_Solver_RAG_Project` in LangSmith |

*No dataset has been exported from production traces yet. This section
should be updated once the first batch of traces is added.*

***

## Process

Traces are reviewed manually in the LangSmith UI under the Tracing tab,
filtered by evaluator score (for example Faithfulness below 0.7), and
added to a LangSmith dataset using the "Add to Dataset" action on each
selected trace.