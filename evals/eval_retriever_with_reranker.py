# eval_retriever.py

from dotenv import load_dotenv

from deepeval import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.metrics import (
    ContextualRecallMetric,
    ContextualPrecisionMetric,
)

from evals.groq_judge import GroqJudge
from evals.harness import (
    load_goldens,
    summarize_by_metric,
    print_summary,
)

from src.reranker import RerankingRetriever


load_dotenv()

GOLDEN_PATH = "goldens/retriever_goldens.json"
JUDGE_MODEL = "openai/gpt-oss-20b"
THRESHOLD = 0.7
TOP_K = 5

# Use 3 for quick testing
# Change to 15 for the final trial
TEST_LIMIT = 1


def run(retriever):
    """
    Evaluate the injected retriever.

    The retriever is responsible for:
        embedding → vector search → reranking
    """

    # 1. LOAD GOLDEN SET
    goldens = load_goldens(GOLDEN_PATH)

    # 2. CREATE GROQ JUDGE
    judge_model = GroqJudge(
        model_name=JUDGE_MODEL
    )

    # 3. CREATE TEST CASES
    test_cases = []

    for golden in goldens[:TEST_LIMIT]:

        query = golden["query"]

        retrieved = retriever.invoke(query)

        retrieval_context = [
            doc.page_content
            for doc in retrieved
        ]

        test_cases.append(
            LLMTestCase(
                input=query,
                expected_output=golden["ideal_answer"],
                actual_output="(generator not evaluated in this run)",
                retrieval_context=retrieval_context,
            )
        )

    # 4. DEEPEVAL METRICS
    metrics = [
        ContextualRecallMetric(
            threshold=THRESHOLD,
            model=judge_model,
            include_reason=True,
            async_mode=False,
        ),
        ContextualPrecisionMetric(
            threshold=THRESHOLD,
            model=judge_model,
            include_reason=True,
            async_mode=False,
        ),
    ]

    # 5. RUN EVALUATION
    result = evaluate(
        test_cases=test_cases,
        metrics=metrics,
        hyperparameters={
            "retriever": "reranker",
            "embedding_model": "BAAI/bge-base-en-v1.5",
            "chunk_size": 1000,
            "chunk_overlap": 150,
            "top_k": TOP_K,
            "judge_model": JUDGE_MODEL,
            "golden_set": GOLDEN_PATH,
            "test_limit": TEST_LIMIT,
        },
    )

    # 6. RETURN STANDARDIZED SUMMARY
    return summarize_by_metric(result)


def run_local():
    """Standalone convenience: build the retriever, then run."""
    return run(RerankingRetriever())


if __name__ == "__main__":
    print_summary("retriever", run_local())