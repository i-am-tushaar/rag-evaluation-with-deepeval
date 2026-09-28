# Toxicity Online Evaluation

## Objective

Monitor whether production RAG responses contain toxic or inappropriate content.

## Evaluation Flow

Production Request
        ↓
RAG Response
        ↓
Toxicity Evaluator
        ↓
Score
        ↓
LangSmith
        ↓
Dashboard / Alert

## Evaluator

Configure a LangSmith online evaluator for toxicity.

The evaluator should receive the generated answer from the trace.

## Input

Example:

User:

"Explain this topic."

RAG Output:

"Generated answer..."

## Evaluation

The evaluator checks the generated response for toxic content.

## Sampling

The evaluator can be applied to all matching traces or a selected sampling rate.

For example:

100% → evaluate every matching trace

10% → evaluate approximately 10% of matching traces

## Dashboard

Add the toxicity evaluation results to the LangSmith dashboard.

## Alert

Configure an alert if toxicity exceeds the acceptable threshold.

## Result

The system continuously monitors production responses for toxicity.