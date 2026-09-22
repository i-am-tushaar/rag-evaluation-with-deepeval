# eval_rag_pipeline.py
from dotenv import load_dotenv

from deepeval import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.metrics import (
    FaithfulnessMetric,
    AnswerRelevancyMetric,
    ContextualRelevancyMetric,
)

from src.rag_pipeline import RagPipeline
from evals.groq_judge import GroqJudge
from evals.harness import load_goldens, summarize_by_metric, print_summary

load_dotenv()

GOLDEN_PATH = "goldens/faithfulness_dataset.json"   # reuse the queries
JUDGE_MODEL = "openai/gpt-oss-20b"
THRESHOLD = 0.7

# Use 3 for quick testing
# Change to 15 for the final trial
TEST_LIMIT = 3


def run(rag):
    # 1. LOAD queries
    goldens = load_goldens(GOLDEN_PATH)

    # 2. RUN the injected pipeline
    test_cases = []

    for g in goldens[:TEST_LIMIT]:
        result = rag.invoke(g["query"])   # retrieve -> rerank -> generate

        test_cases.append(
            LLMTestCase(
                input=g["query"],
                actual_output=result["answer"],
                retrieval_context=result["context"],
            )
        )

    # 3. THE THREE TRIAD METRICS
    judge_model = GroqJudge(model_name=JUDGE_MODEL)

    metrics = [
        ContextualRelevancyMetric(
            threshold=THRESHOLD,
            model=judge_model,
            include_reason=True,
        ),
        FaithfulnessMetric(
            threshold=THRESHOLD,
            model=judge_model,
            include_reason=True,
        ),
        AnswerRelevancyMetric(
            threshold=THRESHOLD,
            model=judge_model,
            include_reason=True,
        ),
    ]

    # 4. EVALUATE
    result = evaluate(
        test_cases=test_cases,
        metrics=metrics,
        hyperparameters={
            "pipeline": "RagPipeline",
            "judge_model": JUDGE_MODEL,
            "golden_set": GOLDEN_PATH,
            "test_limit": TEST_LIMIT,
        },
    )

    return summarize_by_metric(result)


def run_local():
    """Standalone convenience: build the pipeline, then run."""
    return run(RagPipeline())


if __name__ == "__main__":
    print_summary("rag_pipeline", run_local())