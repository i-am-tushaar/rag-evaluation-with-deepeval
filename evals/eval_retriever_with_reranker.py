import json

from dotenv import load_dotenv

from deepeval import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.metrics import (
    ContextualRecallMetric,
    ContextualPrecisionMetric,
)

from evals.groq_judge import GroqJudge
from src.reranker import RerankingRetriever


load_dotenv()


# ============================================================
# CONFIGURATION
# ============================================================

GOLDEN_PATH = "goldens/retriever_goldens.json"

JUDGE_MODEL = "openai/gpt-oss-20b"

THRESHOLD = 0.7
TOP_K = 5

# Use 3 for quick testing
# Change to 15 for the final trial
TEST_LIMIT = 3


# ============================================================
# LOAD GOLDEN SET
# ============================================================

with open(
    GOLDEN_PATH,
    "r",
    encoding="utf-8",
) as f:
    goldens = json.load(f)

goldens = goldens[:TEST_LIMIT]

print(
    f"Running evaluation on {len(goldens)} test cases..."
)


# ============================================================
# CREATE GROQ JUDGE
# ============================================================

judge_model = GroqJudge(
    model_name=JUDGE_MODEL
)


# ============================================================
# BUILD RERANKING RETRIEVER
# ============================================================

retriever = RerankingRetriever()


# ============================================================
# CREATE TEST CASES
# ============================================================

test_cases = []

for index, golden in enumerate(goldens, 1):

    query = golden["query"]

    print(
        f"\nRetrieving test case {index}: {query}"
    )

    retrieved = retriever.invoke(query)

    retrieval_context = [
        doc.page_content
        for doc in retrieved
    ]

    test_cases.append(
        LLMTestCase(
            input=query,
            expected_output=golden["ideal_answer"],
            actual_output=(
                "(generator not evaluated in this run)"
            ),
            retrieval_context=retrieval_context,
        )
    )


# ============================================================
# DEEPEVAL METRICS
# ============================================================

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


# ============================================================
# RUN EVALUATION
# ============================================================

print("\nStarting DeepEval...\n")

evaluate(
    test_cases=test_cases,
    metrics=metrics,

    hyperparameters={

        "retriever": "reranker",

        "embedding_model":
            "sentence-transformers/all-MiniLM-L6-v2",

        "chunk_size": 1000,

        "chunk_overlap": 150,

        "top_k": TOP_K,

        "judge_model": JUDGE_MODEL,

        "golden_set": GOLDEN_PATH,
    },
)