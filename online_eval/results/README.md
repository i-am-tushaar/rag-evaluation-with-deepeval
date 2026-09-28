# Online Evaluation Results

This folder contains the results, observations, screenshots, and monitoring
records from the LangSmith Online Evaluation setup for the RAG application.

***

## LangSmith Project

**Project Name:**

`Customer_Doubt_Solver_RAG_Project`

***

## Initial Traffic Simulation

The RAG pipeline was executed approximately **7 to 8 times** with different
representative queries to simulate multiple real world requests.

The generated LangSmith traces were collected and used to validate:

* RAG pipeline execution
* Retriever execution
* Reranker execution
* LLM generation
* Latency
* Cost
* Trace logging

### Number of Test Runs

**7 to 8 runs**

***

## LangSmith Traces

Each RAG pipeline execution generated a trace in the
`Customer_Doubt_Solver_RAG_Project` LangSmith project.

The traces were used to inspect:

* Input query
* Retrieved context
* Reranking
* LLM execution
* Final response
* Execution latency
* Token usage
* Cost

***

## Monitoring Records

* [Dashboard](monitoring/dashboard.md)
* [Metrics](monitoring/metrics.md)
* [Alerts](monitoring/alerts.md)