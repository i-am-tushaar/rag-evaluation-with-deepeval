import json
from dotenv import load_dotenv

from deepeval import evaluate
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from deepeval.metrics import GEval

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
        "Compare the actual output against the key facts in the expected output.",
        "Heavily penalize statements in the actual output that contradict the expected output.",
        "Reward statements that match the expected output in meaning, regardless of wording.",
        "Do NOT penalize the actual output for omitting information - only wrong statements.",
    ],
    evaluation_params=[
        LLMTestCaseParams.INPUT,
        LLMTestCaseParams.ACTUAL_OUTPUT,
        LLMTestCaseParams.EXPECTED_OUTPUT,
    ],
    threshold=THRESHOLD,
    model=judge_model,
    strict_mode=False,  # graded scale; strict_mode=True would collapse it to 0/1
)


# 4. EVALUATE
evaluate(test_cases=test_cases, metrics=[correctness])