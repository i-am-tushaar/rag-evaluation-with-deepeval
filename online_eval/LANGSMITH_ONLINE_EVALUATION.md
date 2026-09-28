# LangSmith Online Evaluation Steps

1. Create a new project in LangSmith.

2. Create a LangSmith API key and add it to the `.env` file.

3. Run the RAG pipeline.

4. Install and configure LangSmith for the project.

5. Add `@traceable` to the RAG pipeline and required components such as the retriever/reranker.

6. Run the RAG pipeline and check the latency and cost in LangSmith.

7. Run the RAG pipeline 5 times and collect the trace data.

8. Create a LangSmith dashboard with Latency P95 and Cost P95.

9. Create an alert for the required operational metrics.

10. Create and run a Toxicity evaluation.

11. Add the Toxicity evaluation graph to the LangSmith dashboard.

12. Create and run the RAG Triad evaluation:
    - Contextual Relevancy
    - Faithfulness
    - Answer Relevancy

13. Add the RAG Triad evaluation graphs to the LangSmith dashboard.

14. Create and grow a LangSmith evaluation dataset.