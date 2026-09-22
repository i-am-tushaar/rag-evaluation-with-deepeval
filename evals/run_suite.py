# evals/run_suite.py

import argparse, hashlib, json, os, subprocess, time
from datetime import datetime, timezone
from dotenv import load_dotenv

from src.rag_pipeline import RagPipeline
from evals import eval_retriever, eval_generator, eval_rag_pipeline, eval_application, eval_safety, eval_ops
from evals.metric_registry import rule_for

load_dotenv()

BASELINE_PATH = "baselines/baseline.json"
CANDIDATE_PATH = "baselines/candidate.json"


def _slug(name):
    return name.strip().lower().replace(" ", "_")


def flatten_nested(namespace, summary):
    return {
        f"{namespace}.{_slug(metric)}.{stat}": value
        for metric, stats in summary.items()
        for stat, value in stats.items()
    }


def prefix_flat(namespace, flat):
    return {f"{namespace}.{key}": value for key, value in flat.items()}


def _git_sha():
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            text=True, stderr=subprocess.DEVNULL
        ).strip()
    except Exception:
        return "unknown"


def _prompt_hash():
    try:
        from src.generator import prompt
        return hashlib.sha256(str(prompt).encode()).hexdigest()[:12]
    except Exception:
        return "unknown"


def build_metadata(label):
    return {
        "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "git_sha": _git_sha(),
        "prompt_hash": _prompt_hash(),
        "label": label,
    }


def run_suite(label="", quiet=False, full=False):
    start_time = time.perf_counter()
    verbose = not quiet

    print("Building RAG pipeline...")
    rag = RagPipeline()
    retriever = rag.retriever
    metrics = {}

    print("\n[1/6] Retriever evaluation...")
    metrics.update(flatten_nested("retriever", eval_retriever.run(retriever)))

    print("\n[2/6] Generator evaluation...")
    metrics.update(flatten_nested("generator", eval_generator.run()))

    print("\n[3/6] RAG pipeline evaluation...")
    metrics.update(flatten_nested("pipeline", eval_rag_pipeline.run(rag)))

    print("\n[4/6] Application evaluation...")
    metrics.update(flatten_nested("application", eval_application.run(rag)))

    print("\n[5/6] Safety evaluation...")
    metrics.update(prefix_flat("safety", eval_safety.run_safety(rag, verbose=verbose)))

    print("\n[6/6] Operational evaluation...")
    metrics.update(prefix_flat("ops", eval_ops.run_ops(rag, verbose=verbose)))

    if not full:
        metrics = {
            mid: value for mid, value in metrics.items()
            if rule_for(mid)["kind"] != "info"
        }

    elapsed = time.perf_counter() - start_time

    return {
        "metadata": {
            **build_metadata(label),
            "suite_seconds": round(elapsed, 1),
            "full": full,
            "n_metrics": len(metrics),
        },
        "metrics": metrics,
    }


def write_snapshot(snapshot, path):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as file:
        json.dump(snapshot, file, indent=2, sort_keys=True)
    return path


def print_snapshot(snapshot):
    meta, metrics = snapshot["metadata"], snapshot["metrics"]

    print("\n" + "=" * 74)
    print("EVALUATION SNAPSHOT")
    print("=" * 74)
    print(f"label       : {meta.get('label') or '(none)'}")
    print(f"created_at  : {meta['created_at']}")
    print(f"git_sha     : {meta['git_sha']}")
    print(f"prompt_hash : {meta['prompt_hash']}")
    print(f"suite_time  : {meta['suite_seconds']}s")
    print(f"metrics     : {meta['n_metrics']}")
    print("-" * 74)

    for key in sorted(metrics):
        value = metrics[key]
        shown = f"{value:.4f}" if isinstance(value, float) else str(value)
        print(f"  {key:<44} {shown}")

    print("=" * 74)


def main():
    parser = argparse.ArgumentParser(
        description="Run the complete RAG evaluation suite and write a snapshot."
    )
    parser.add_argument(
        "--baseline", action="store_true",
        help=f"write baseline to {BASELINE_PATH}"
    )
    parser.add_argument("--out", default=None, help="custom snapshot output path")
    parser.add_argument("--label", default="", help="description of the pipeline change")
    parser.add_argument("--quiet", action="store_true", help="suppress safety and ops chatter")
    parser.add_argument(
        "--full", action="store_true",
        help="include info metrics such as avg/min/max/n"
    )

    args = parser.parse_args()

    output_path = (
        args.out
        or BASELINE_PATH if args.baseline
        else CANDIDATE_PATH
    )

    snapshot = run_suite(
        label=args.label,
        quiet=args.quiet,
        full=args.full,
    )

    print_snapshot(snapshot)
    path = write_snapshot(snapshot, output_path)
    print(f"\nSnapshot written to: {path}")


if __name__ == "__main__":
    main()