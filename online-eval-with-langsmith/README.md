# Online Evaluation with LangSmith

## Overview

This folder contains the implementation and documentation for monitoring and evaluating the RAG application using LangSmith.

The online evaluation system monitors the RAG application after deployment using production traces.

## Objectives

The online evaluation system monitors:

**Pipeline Execution**
- RAG pipeline execution
- Retriever performance
- Reranker execution
- LLM generation

**Operational Metrics**
- Latency
- Cost

**Safety Metrics**
- Toxicity

**Quality Metrics**
- Contextual Relevancy
- Faithfulness
- Answer Relevancy

**Supporting Systems**
- Production quality trends
- Alerts
- Evaluation datasets

## Online Evaluation Architecture

User Query
    ↓
RAG Pipeline
    ↓
Retriever
    ↓
Reranker
    ↓
LLM
    ↓
Response
    ↓
LangSmith Trace
    ↓
Online Evaluators
    ↓
Metrics
    ↓
Dashboard
    ↓
Alerts

## Main Components

### 1. Tracing

LangSmith traces the RAG pipeline and important components such as:

- RAG pipeline
- Retriever
- Reranker
- LLM

### 2. Monitoring

Operational metrics are monitored to track system performance and cost:

**Latency**
- P95 latency
- P99 latency

**Cost**
- Average cost
- P95 cost

### 3. Online Evaluation

Production traces are evaluated across two categories:

**Safety Metrics**
- Toxicity

**Quality Metrics**
- Contextual Relevancy
- Faithfulness
- Answer Relevancy

### 4. Dashboard

A LangSmith dashboard is used to visualize:

**Operational**
- Latency P95
- Cost P95

**Safety**
- Toxicity

**Quality**
- RAG Triad metrics (Contextual Relevancy, Faithfulness, Answer Relevancy)

### 5. Alerts

Alerts are configured for important operational, safety, or quality problems.

### 6. Dataset

Production examples can be converted into evaluation datasets for future offline evaluation and regression testing.

## Offline vs Online Evaluation

Offline evaluation:

- Uses a predefined dataset
- Usually performed before deployment
- Uses reference answers when available
- Used for benchmarking and regression testing

Online evaluation:

- Uses production traces
- Runs after deployment
- Usually does not require reference answers
- Used for monitoring and detecting problems

## Folder Structure

- `tracing/` - LangSmith tracing configuration
- `evaluations/` - Online evaluation definitions
- `monitoring/` - Metrics, dashboards and alerts
- `datasets/` - Dataset creation and growth
- `results/` - Results and observations