"""
evals/eval_generator.py
=======================
Component-level evaluation of the GENERATOR, in isolation.

Faithfulness: of the claims in the generated answer, how many are supported
by the context it was given? (Did the generator make things up?)

ISOLATION: we feed the generator the GOLDEN context (the known-good chunks
from the faithfulness dataset), NOT the retriever's output. So a low score
is purely the generator's fault --- the context was already correct.

    python -m evals.eval_generator
"""

from dotenv import load_dotenv

from deepeval import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.metrics import FaithfulnessMetric, AnswerRelevancyMetric

from src.generator import generate
from evals.groq_judge import GroqJudge
from evals.harness import load_goldens, summarize_by_metric, print_summary

load_dotenv()

GOLDEN_PATH = "goldens/faithfulness_dataset.json"
JUDGE_MODEL = "openai/gpt-oss-20b"
THRESHOLD = 0.7

# Use 5 for quick testing
# Change to 15 for the final trial
TEST_LIMIT = 3


def run():
    # 1. LOAD the faithfulness golden set
    goldens = load_goldens(GOLDEN_PATH)

    # 2. CREATE THE JUDGE
    judge_model = GroqJudge(model_name=JUDGE_MODEL)

    # 3. RUN THE GENERATOR on the GOLDEN context
    test_cases = []

    for g in goldens[:TEST_LIMIT]:
        context = g["ideal_context"]
        answer = generate(g["query"], context)

        test_cases.append(
            LLMTestCase(
                input=g["query"],
                actual_output=answer,
                retrieval_context=context,
                # no expected_output --- faithfulness never reads it
            )
        )

    # 4. THE METRICS
    metrics = [
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

    # 5. EVALUATE
    result = evaluate(
        test_cases=test_cases,
        metrics=metrics,
        hyperparameters={
            "generator": "generate",
            "judge_model": JUDGE_MODEL,
            "golden_set": GOLDEN_PATH,
            "test_limit": TEST_LIMIT,
        },
    )

    return summarize_by_metric(result)


def run_local():
    """Standalone convenience function."""
    return run()


if __name__ == "__main__":
    print_summary("generator", run_local())