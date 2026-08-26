import json

from dotenv import load_dotenv

from deepeval import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.metrics import (
    ContextualRecallMetric,
    ContextualPrecisionMetric,
)

from src.reranker import RerankingRetriever
from evals.groq_judge import GroqJudge


load_dotenv()


# ============================================================
# CONFIGURATION
# ============================================================

GOLDEN_PATH = "goldens/retriever_goldens.json"

JUDGE_MODEL = "openai/gpt-oss-20b"

THRESHOLD = 0.7
TOP_K = 5

# Final benchmark uses all test cases
TEST_LIMIT = 15


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
    f"Running final benchmark on {len(goldens)} test cases..."
)


# ============================================================
# CREATE GROQ JUDGE
# ============================================================

judge_model = GroqJudge(
    model_name=JUDGE_MODEL
)


# ============================================================
# BUILD FINAL RERANKER
# ============================================================

retriever = RerankingRetriever(
    fetch_k=10,
    top_k=TOP_K,
)


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
                "(generator not evaluated in this benchmark)"
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
# FINAL BENCHMARK
# ============================================================

print("\nStarting final DeepEval benchmark...\n")


evaluate(
    test_cases=test_cases,
    metrics=metrics,

    hyperparameters={

        "experiment": "final_benchmark",

        "retriever": "cross_encoder_reranker",

        "embedding_model":
            "BAAI/bge-base-en-v1.5",

        "reranker":
            "cross-encoder/ms-marco-MiniLM-L-6-v2",

        "search_type":
            "similarity + cross_encoder_reranking",

        "fetch_k": 10,

        "top_k": TOP_K,

        "chunk_size": 1000,

        "chunk_overlap": 150,

        "judge_model": JUDGE_MODEL,

        "golden_set": GOLDEN_PATH,
    },
)