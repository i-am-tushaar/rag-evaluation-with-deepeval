# RAG Evaluation Suite

This folder contains evaluation scripts for testing the quality, safety, performance, and cost of the RAG application.

## Evaluation Categories

- **Component Evaluation:** Retriever and generator evaluation.
- **Pipeline Evaluation:** Complete RAG Triad evaluation.
- **Application Evaluation:** Quality, safety, scope, latency, and cost evaluation.

## Project Structure

```text
evals/
├── __init__.py
├── groq_judge.py
├── component/
│   ├── __init__.py
│   ├── eval_retriever.py
│   └── eval_generator.py
├── pipeline/
│   ├── __init__.py
│   └── eval_rag_triad.py
└── application/
    ├── __init__.py
    ├── quality/
    │   ├── __init__.py
    │   └── eval_application.py
    ├── safety/
    │   ├── __init__.py
    │   ├── eval_toxicity.py
    │   ├── eval_leakage.py
    │   └── eval_scope_safety.py
    └── operations/
        ├── __init__.py
        ├── eval_latency.py
        └── eval_cost.py
```

## Setup

Run commands from the project root.

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key
```

## Golden Datasets

```text
goldens/
├── retriever_goldens.json
├── faithfulness_dataset.json
├── correctness_goldens.json
├── leakage_goldens.json
└── scope_goldens.json
```

## Run Each Evaluation

### 1. Retriever Evaluation

**Metrics:**

- Contextual Recall
- Contextual Precision

**Dataset:**

```text
goldens/retriever_goldens.json
```

**Run:**

```bash
python -m evals.component.eval_retriever
```

**Result:**

```text
results/component/retriever_results.json
```

### 2. Generator Evaluation

**Metrics:**

- Faithfulness
- Answer Relevancy

**Dataset:**

```text
goldens/faithfulness_dataset.json
```

**Run:**

```bash
python -m evals.component.eval_generator
```

**Result:**

```text
results/component/generator_results.json
```

### 3. RAG Triad Evaluation

**Metrics:**

- Contextual Relevancy
- Faithfulness
- Answer Relevancy

**Run:**

```bash
python -m evals.pipeline.eval_rag_triad
```

**Result:**

```text
results/pipeline/rag_pipeline_results.json
```

### 4. Application Quality Evaluation

**Metrics:**

- Correctness
- Completeness
- Style

**Dataset:**

```text
goldens/correctness_goldens.json
```

**Run:**

```bash
python -m evals.application.quality.eval_application
```

**Result:**

```text
results/application/quality/application_results.json
```

### 5. Toxicity Evaluation

Checks whether the application generates toxic, abusive, or harmful responses.

**Run:**

```bash
python -m evals.application.safety.eval_toxicity
```

**Result:**

```text
results/application/safety/toxicity_results.json
```

### 6. Leakage Evaluation

Checks:

- Course content leakage
- Prompt leakage
- PII leakage

**Dataset:**

```text
goldens/leakage_goldens.json
```

**Run:**

```bash
python -m evals.application.safety.eval_leakage
```

**Result:**

```text
results/application/safety/leakage_results.json
```

### 7. Scope Adherence Evaluation

Checks:

- Allowed questions
- Out-of-scope questions
- Mixed queries
- Partially relevant queries

**Dataset:**

```text
goldens/scope_goldens.json
```

**Run:**

```bash
python -m evals.application.safety.eval_scope_safety
```

**Result:**

```text
results/application/safety/scope_results.json
```

### 8. Latency Evaluation

Measures:

- End-to-end latency
- Time to First Token
- Retrieval latency
- Generation latency
- P50 latency
- P95 latency
- P99 latency
- SLO compliance

Latency evaluation does not require a golden dataset or an LLM judge.

**Run:**

```bash
python -m evals.application.operations.eval_latency
```

**Result:**

```text
results/application/operations/latency_results.json
```

### 9. Cost Evaluation

Measures:

- Input tokens
- Cached input tokens
- Output tokens
- Total tokens
- Estimated cost

**Run:**

```bash
python -m evals.application.operations.eval_cost
```

**Result:**

```text
results/application/operations/cost_results.json
```

## Run All Evaluations

```bash
python -m evals.component.eval_retriever
python -m evals.component.eval_generator
python -m evals.pipeline.eval_rag_triad
python -m evals.application.quality.eval_application
python -m evals.application.safety.eval_toxicity
python -m evals.application.safety.eval_leakage
python -m evals.application.safety.eval_scope_safety
python -m evals.application.operations.eval_latency
python -m evals.application.operations.eval_cost
```

## Recommended Evaluation Order

1. Retriever Evaluation
2. Generator Evaluation
3. RAG Triad Evaluation
4. Application Quality Evaluation
5. Toxicity Evaluation
6. Leakage Evaluation
7. Scope Adherence Evaluation
8. Latency Evaluation
9. Cost Evaluation

## Results Structure

```text
results/
├── component/
│   ├── retriever_results.json
│   └── generator_results.json
├── pipeline/
│   └── rag_pipeline_results.json
└── application/
    ├── quality/
    │   └── application_results.json
    ├── safety/
    │   ├── toxicity_results.json
    │   ├── leakage_results.json
    │   └── scope_results.json
    └── operations/
        ├── latency_results.json
        └── cost_results.json
```

## Evaluation Summary

| Evaluation | Main Metrics |
|---|---|
| Retriever | Contextual Recall, Contextual Precision |
| Generator | Faithfulness, Answer Relevancy |
| RAG Triad | Contextual Relevancy, Faithfulness, Answer Relevancy |
| Application Quality | Correctness, Completeness, Style |
| Toxicity | Toxicity Detection |
| Leakage | Course, Prompt, and PII Leakage |
| Scope Adherence | In-Scope, Out-of-Scope, Mixed Queries |
| Latency | E2E, TTFT, P50, P95, P99 |
| Cost | Input, Cached, Output Tokens, Estimated Cost |

## Viewing Results

### Windows

```bash
type results\component\retriever_results.json
```

### Linux/macOS

```bash
cat results/component/retriever_results.json
```

You can also open the JSON result files directly in Visual Studio Code.

## Troubleshooting

### Module Not Found Error

Run evaluations from the project root:

```bash
python -m evals.component.eval_retriever
```

### API Key Error

Check that the `.env` file exists and contains valid API keys.

### Dataset Not Found Error

Verify that the required files exist inside the `goldens/` directory.

### Result Directory Not Found Error

Create the following directories:

```text
results/component/
results/pipeline/
results/application/quality/
results/application/safety/
results/application/operations/
```

### Virtual Environment Error

Activate the virtual environment before running evaluations:

```bash
venv\Scripts\activate
```

## Notes

- Run all evaluations from the project root.
- Activate the correct virtual environment.
- Configure the required API keys.
- Verify that golden datasets are available.
- Review the generated JSON files after each evaluation.
- Latency and cost evaluations do not require golden datasets.
