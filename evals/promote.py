import argparse
import json
import sys
from pathlib import Path

from evals.compare import compare
from evals.metric_registry import kind_for


BASELINE_PATH = "baselines/baseline.json"
CANDIDATE_PATH = "baselines/candidate.json"


EXIT_CODE = {
    "PROMOTE": 0,
    "REVIEW": 1,
    "BLOCK": 2,
}


def load(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def decide(rows):
    blocked = []
    review = []

    for r in rows:
        if r["status"] != "regressed":
            continue

        kind = kind_for(r["id"])

        if kind == "gate":
            blocked.append(r["id"])

        elif kind == "guardrail":
            review.append(r["id"])

    if blocked:
        verdict = "BLOCK"

    elif review:
        verdict = "REVIEW"

    else:
        verdict = "PROMOTE"

    return verdict, blocked, review


def main():
    ap = argparse.ArgumentParser(
        description="Promotion gate: regression -> promote/review/block"
    )

    ap.add_argument(
        "--baseline",
        default=BASELINE_PATH
    )

    ap.add_argument(
        "--candidate",
        default=CANDIDATE_PATH
    )

    args = ap.parse_args()

    baseline = load(args.baseline)
    candidate = load(args.candidate)

    # LAYER 1: regression — what changed?
    result, rows = compare(baseline, candidate)

    # LAYER 2: promotion — what do we do about it?
    verdict, blocked, review = decide(rows)

    print("=" * 92)
    print(f"regression result : {result}")

    if blocked:
        print(f"BLOCKED by (gates) : {', '.join(blocked)}")

    if review:
        print(f"REVIEW (guardrails) : {', '.join(review)}")

    print("=" * 92)

    banner = {
        "PROMOTE": "PROMOTE — no gate or guardrail regressed. Safe to proceed.",
        "REVIEW": "REVIEW — a guardrail regressed. A human should review.",
        "BLOCK": "BLOCK — a gate regressed. Stop.",
    }[verdict]

    print(f"VERDICT: {banner}")
    print("=" * 92)

    sys.exit(EXIT_CODE[verdict])


if __name__ == "__main__":
    main()