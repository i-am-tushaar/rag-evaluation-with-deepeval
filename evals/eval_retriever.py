# eval_retriever.py

from dotenv import load_dotenv

from deepeval import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.metrics import (
    ContextualRecallMetric,
    ContextualPrecisionMetric,
)

from src.reranker import RerankingRetriever
from evals.harness import load_goldens, summarize_by_metric, print_summary
from evals.groq_judge import GroqJudge


load_dotenv()


GOLDEN_PATH = "goldens/retriever_goldens.json"
JUDGE_MODEL = "openai/gpt-oss-20b"
THRESHOLD = 0.7

# Use 5 for quick testing
# Change to 15 for the final trial
TEST_LIMIT = 1


def run(retriever):
    # 1. LOAD the golden set
    goldens = load_goldens(GOLDEN_PATH)

    # 2. RUN THE INJECTED RETRIEVER on each question
    #    and build one test case per golden.
    test_cases = []

    for g in goldens[:TEST_LIMIT]:
        retrieved = retriever.invoke(g["query"])

        retrieval_context = [
            doc.page_content
            for doc in retrieved
        ]

        test_cases.append(
            LLMTestCase(
                input=g["query"],
                expected_output=g["ideal_answer"],
                retrieval_context=retrieval_context,
                actual_output="(generator not evaluated in this run)",
            )
        )

    # 3. CREATE THE JUDGE
    judge_model = GroqJudge(model_name=JUDGE_MODEL)

    # 4. THE METRICS
    metrics = [
        ContextualRecallMetric(
            threshold=THRESHOLD,
            model=judge_model,
            include_reason=True,
        ),
        ContextualPrecisionMetric(
            threshold=THRESHOLD,
            model=judge_model,
            include_reason=True,
        ),
    ]

    # 5. EVALUATE
    result = evaluate(
        test_cases=test_cases,
        metrics=metrics,
        hyperparameters={
            "retriever": "reranker",
            "embedding_model": "BAAI/bge-base-en-v1.5",
            "chunk_size": 1000,
            "chunk_overlap": 150,
            "top_k": 3,
            "judge_model": JUDGE_MODEL,
            "golden_set": GOLDEN_PATH,
            "test_limit": TEST_LIMIT,
        },
    )

    return summarize_by_metric(result)


def run_local():
    """Standalone convenience: build the retriever, then run."""
    return run(RerankingRetriever())


if __name__ == "__main__":
    print_summary("retriever", run_local())