import json
from dotenv import load_dotenv

from deepeval import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.metrics import (
    FaithfulnessMetric,
    AnswerRelevancyMetric,
    ContextualRelevancyMetric,
)

from evals.groq_judge import GroqJudge
from src.rag_pipeline import RagPipeline

load_dotenv()

GOLDEN_PATH = "goldens/faithfulness_dataset.json"   # reuse the queries
JUDGE_MODEL = "openai/gpt-oss-20b"
THRESHOLD = 0.7

# Use 3 for quick testing
# Change to 15 for the final trial
TEST_LIMIT = 3


# 1. LOAD queries (we only need the queries — context comes from the pipeline now)
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
    result = rag.invoke(g["query"])          # retrieve → rerank → generate

    test_cases.append(
        LLMTestCase(
            input=g["query"],
            actual_output=result["answer"],       # what the generator produced
            retrieval_context=result["context"],  # what the RETRIEVER returned
        )
    )


# 3. THE THREE TRIAD METRICS
metrics = [
    ContextualRelevancyMetric(threshold=THRESHOLD, model=judge_model, include_reason=True),
    FaithfulnessMetric(threshold=THRESHOLD, model=judge_model, include_reason=True),
    AnswerRelevancyMetric(threshold=THRESHOLD, model=judge_model, include_reason=True),
]


# 4. EVALUATE
evaluate(test_cases=test_cases, metrics=metrics)