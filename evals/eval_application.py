import json
from dotenv import load_dotenv

from deepeval import evaluate
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from deepeval.metrics import GEval
from deepeval.metrics.g_eval import Rubric

from evals.groq_judge import GroqJudge
from src.rag_pipeline import RagPipeline


load_dotenv()

GOLDEN_PATH = "goldens/correctness_goldens.json"  # question + ideal_answer
JUDGE_MODEL = "openai/gpt-oss-20b"
THRESHOLD = 0.7

# Use 3 for quick testing
# Change to 15 for the final trial
TEST_LIMIT = 10


# 1. LOAD queries + ideal answers
# ideal_answer is the CORRECT answer, our reference
with open(GOLDEN_PATH,"r",encoding="utf-8") as f:
    goldens = json.load(f)

goldens = goldens[:TEST_LIMIT]

print(f"Running evaluation on {len(goldens)} test cases...")

# Create Groq judge
judge_model = GroqJudge(model_name=JUDGE_MODEL)


# 2. RUN THE FULL PIPELINE per query, build a test case from LIVE output
rag = RagPipeline()
test_cases = []

for g in goldens:
    result = rag.invoke(g["question"])  # retrieve -> rerank -> generate

    test_cases.append(
        LLMTestCase(
            input=g["question"],
            actual_output=result["answer"],
            expected_output=g["ideal_answer"],
        )
    )


# 3. THE CORRECTNESS METRIC
# graded G-Eval - partial credit, not pass/fail
correctness = GEval(
    name="Correctness",
    evaluation_steps=[
        "Compare only the factual claims in the actual output against the expected output.",
        "A claim is wrong only if it CONTRADICTS the expected output or is factually false. Judge truth, not completeness.",
        "A factually accurate answer must score at least 0.9 even if it is shorter or covers fewer points than the expected output.",
        "Do NOT deduct for brevity, missing elaboration, or omitted points — omissions are not errors here.",
        "Additional correct information must NEVER lower the score.",
    ],
    rubric=[
        Rubric(score_range=(9, 10), expected_outcome="All stated claims are factually correct and consistent. No contradictions. Brevity is fine."),
        Rubric(score_range=(5, 8),  expected_outcome="Mostly correct but one minor inaccuracy."),
        Rubric(score_range=(0, 4),  expected_outcome="Contains a clear factual error or a claim that contradicts the expected output."),
    ],
    evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT, LLMTestCaseParams.EXPECTED_OUTPUT],
    threshold=THRESHOLD,
    model=judge_model,
    strict_mode=False,
)


# 4. EVALUATE
evaluate(test_cases=test_cases, metrics=[correctness])