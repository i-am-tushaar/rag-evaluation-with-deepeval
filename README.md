# RAG Evaluation with DeepEval

An end-to-end evaluation framework for measuring the quality, safety, performance, and cost of a Retrieval-Augmented Generation (RAG) application.

## Project Overview

This project evaluates a RAG application at three levels:

1. **Component Level**
   - Retriever evaluation
   - Generator evaluation

2. **Pipeline Level**
   - RAG Triad evaluation

3. **Application Level**
   - Answer quality
   - Safety
   - Scope adherence
   - Latency
   - Cost

The evaluation framework uses DeepEval metrics and custom evaluation scripts.

## Main Features

- Retriever quality evaluation
- Generator quality evaluation
- RAG Triad evaluation
- Application correctness evaluation
- Completeness and style evaluation
- Toxicity detection
- Prompt leakage detection
- Course content leakage detection
- PII leakage detection
- Scope adherence evaluation
- Mixed-query handling
- Latency and Time to First Token measurement
- P50, P95, and P99 latency analysis
- Token usage and cost estimation
- JSON-based evaluation reports

## Project Structure

```text
rag-evaluation-with-deepeval/
├── README.md
├── FINAL_RESULTS.md
├── requirements.txt
├── pyproject.toml
├── .env
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── config/
│   ├── ingestion/
│   ├── retrieval/
│   ├── generation/
│   └── pipeline/
│
├── goldens/
│   ├── retriever_goldens.json
│   ├── faithfulness_dataset.json
│   ├── correctness_goldens.json
│   ├── leakage_goldens.json
│   ├── scope_goldens.json
│   └── toxicity_goldens.json
│
├── evals/
│   ├── README.md
│   ├── __init__.py
│   ├── groq_judge.py
│   │
│   ├── component/
│   │   ├── __init__.py
│   │   ├── eval_retriever.py
│   │   └── eval_generator.py
│   │
│   ├── pipeline/
│   │   ├── __init__.py
│   │   └── eval_rag_triad.py
│   │
│   └── application/
│       ├── __init__.py
│       ├── quality/
│       │   ├── __init__.py
│       │   └── eval_application.py
│       ├── safety/
│       │   ├── __init__.py
│       │   ├── eval_toxicity.py
│       │   ├── eval_leakage.py
│       │   └── eval_scope_safety.py
│       └── operations/
│           ├── __init__.py
│           ├── eval_latency.py
│           └── eval_cost.py
│
├── results/
│   ├── component/
│   ├── pipeline/
│   └── application/
│       ├── quality/
│       ├── safety/
│       └── operations/
│
├── notebooks/
│   └── experimentation.ipynb
│
└── tests/
    └── test_pipeline.py
```

> The folder names may be adjusted to match the actual project structure.

## Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd rag-evaluation-with-deepeval
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If the project uses `pyproject.toml`, install it with:

```bash
pip install -e .
```

## Environment Configuration

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key
```

Do not commit the `.env` file to GitHub.

Add this to `.gitignore`:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

## Golden Datasets

Golden datasets are stored inside the `goldens/` directory.

| Dataset | Purpose |
|---|---|
| `retriever_goldens.json` | Retriever recall and precision evaluation |
| `faithfulness_dataset.json` | Generator faithfulness evaluation |
| `correctness_goldens.json` | Application correctness evaluation |
| `leakage_goldens.json` | Prompt, course, and PII leakage evaluation |
| `scope_goldens.json` | Scope adherence and mixed-query evaluation |
| `toxicity_goldens.json` | Toxicity and harmful-response evaluation |

## Evaluation Modules

### Component Evaluation

Component evaluation checks individual RAG components.

#### Retriever

Metrics:

- Contextual Recall
- Contextual Precision

Run:

```bash
python -m evals.component.eval_retriever
```

#### Generator

Metrics:

- Faithfulness
- Answer Relevancy

Run:

```bash
python -m evals.component.eval_generator
```

### Pipeline Evaluation

The RAG Triad evaluates the complete RAG pipeline.

Metrics:

- Contextual Relevancy
- Faithfulness
- Answer Relevancy

Run:

```bash
python -m evals.pipeline.eval_rag_triad
```

### Application Evaluation

Application evaluation checks the complete user-facing system.

#### Quality

Metrics:

- Correctness
- Completeness
- Style

Run:

```bash
python -m evals.application.quality.eval_application
```

#### Safety

Toxicity evaluation:

```bash
python -m evals.application.safety.eval_toxicity
```

Leakage evaluation:

```bash
python -m evals.application.safety.eval_leakage
```

Scope adherence evaluation:

```bash
python -m evals.application.safety.eval_scope_safety
```

#### Operations

Latency evaluation:

```bash
python -m evals.application.operations.eval_latency
```

Cost evaluation:

```bash
python -m evals.application.operations.eval_cost
```

## Run All Evaluations

Run all evaluations from the project root:

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

1. Retriever evaluation
2. Generator evaluation
3. RAG Triad evaluation
4. Application quality evaluation
5. Toxicity evaluation
6. Leakage evaluation
7. Scope adherence evaluation
8. Latency evaluation
9. Cost evaluation

## Results

Evaluation outputs are stored inside the `results/` directory.

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

| Evaluation | Metrics |
|---|---|
| Retriever | Contextual Recall, Contextual Precision |
| Generator | Faithfulness, Answer Relevancy |
| RAG Triad | Contextual Relevancy, Faithfulness, Answer Relevancy |
| Application Quality | Correctness, Completeness, Style |
| Toxicity | Toxicity Detection |
| Leakage | Course, Prompt, and PII Leakage |
| Scope Adherence | In-Scope, Out-of-Scope, Mixed Queries |
| Latency | E2E, TTFT, Retrieval, Generation, P50, P95, P99 |
| Cost | Input Tokens, Cached Tokens, Output Tokens, Estimated Cost |

## Viewing JSON Results

### Windows

```bash
type results\component\retriever_results.json
```

### Linux/macOS

```bash
cat results/component/retriever_results.json
```

You can also open the JSON files directly in Visual Studio Code.

## Running the Application

If the project contains a Streamlit application, run:

```bash
streamlit run src/app.py
```

If the application file is located somewhere else, update the path accordingly.

## Troubleshooting

### ModuleNotFoundError

Run commands from the project root:

```bash
python -m evals.component.eval_retriever
```

Make sure the virtual environment is activated.

### API Key Error

Check the `.env` file and verify that the required API keys are present.

### Dataset Not Found

Verify that the required JSON files exist in the `goldens/` directory.

### Result Directory Not Found

Create the required directories:

```text
results/component/
results/pipeline/
results/application/quality/
results/application/safety/
results/application/operations/
```

### Streamlit Not Recognized

Install Streamlit:

```bash
pip install streamlit
```

Then run:

```bash
streamlit run src/app.py
```

## Development Guidelines

- Keep evaluation scripts separated by category.
- Use module-based execution with `python -m`.
- Store golden datasets inside `goldens/`.
- Store generated reports inside `results/`.
- Keep API keys inside `.env`.
- Do not commit secrets or generated virtual-environment files.
- Update `FINAL_RESULTS.md` after completing evaluation experiments.
- Add new evaluation scripts inside the appropriate `evals/` subfolder.
- Update this README when adding new evaluation modules.

## License

Add the project license information here.
