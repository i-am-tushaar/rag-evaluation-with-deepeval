
"""
groq_judge.py

Purpose:
Use Groq LLMs as an LLM-as-a-Judge evaluator for the End-to-End LLMOps project.

Features:
1. Single-answer evaluation with a score from 1 to 5.
2. Pairwise comparison of two answers.
3. Batch evaluation of multiple test cases.
4. Summary statistics including mean score and pass rate.
5. Deterministic judging using temperature=0.
6. Integration with the GROQ_API_KEY environment variable.
"""

import os
import json
import time
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv
from groq import Groq


# Load environment variables from the project's .env file.
load_dotenv()

# Default and faster Groq models.
DEFAULT_MODEL = "openai/gpt-oss-120b"
FAST_MODEL = "openai/gpt-oss-20b"


class GroqJudge:
    """Evaluate LLM responses using a Groq-powered judge."""

    def __init__(
        self,
        model_name: str = DEFAULT_MODEL,
        pass_threshold: int = 4,
        max_retries: int = 3,
        request_delay: float = 0.5,
    ):
        """Initialize the Groq client and evaluation settings."""

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError(
                "GROQ_API_KEY is missing. Add it to your .env file."
            )

        self.client = Groq(api_key=api_key)
        self.model_name = model_name
        self.pass_threshold = pass_threshold
        self.max_retries = max_retries
        self.request_delay = request_delay

    def _call_model(self, prompt: str) -> str:
        """Call Groq with retries for transient failures."""

        for attempt in range(self.max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are an impartial LLM evaluator. "
                                "Follow the evaluation criteria carefully. "
                                "Return valid JSON when requested."
                            ),
                        },
                        {"role": "user", "content": prompt},
                    ],
                    temperature=0,
                )

                if self.request_delay > 0:
                    time.sleep(self.request_delay)

                return response.choices[0].message.content or ""

            except Exception:
                if attempt == self.max_retries - 1:
                    raise
                time.sleep(2 ** attempt)

        raise RuntimeError("Groq request failed.")

    @staticmethod
    def _parse_json(text: str) -> Dict[str, Any]:
        """Parse JSON, including JSON enclosed in Markdown fences."""

        text = text.strip()

        if text.startswith("```"):
            lines = text.splitlines()
            if lines and lines[0].startswith("```"):
                lines = lines[1:]
            if lines and lines[-1].strip() == "```":
                lines = lines[:-1]
            text = "\n".join(lines).strip()

        try:
            result = json.loads(text)
        except json.JSONDecodeError:
            start = text.find("{")
            end = text.rfind("}")

            if start == -1 or end == -1:
                raise ValueError(
                    f"Judge did not return valid JSON: {text}"
                )

            result = json.loads(text[start : end + 1])

        if not isinstance(result, dict):
            raise ValueError("Judge output must be a JSON object.")

        return result

    def judge(
        self,
        question: str,
        answer: str,
        context: Optional[str] = None,
        reference: Optional[str] = None,
        criteria: str = (
            "Evaluate correctness, relevance, completeness, "
            "and faithfulness to the provided context."
        ),
    ) -> Dict[str, Any]:
        """
        Score one answer from 1 to 5.

        A score equal to or greater than pass_threshold passes.
        """

        prompt = f"""
Evaluate the answer using the criteria below.

Question:
{question}

Reference answer:
{reference or "Not provided"}

Retrieved context:
{context or "Not provided"}

Candidate answer:
{answer}

Evaluation criteria:
{criteria}

Scoring rubric:
1 = Completely incorrect or irrelevant
2 = Mostly incorrect or seriously incomplete
3 = Partially correct
4 = Correct with minor omissions
5 = Accurate, relevant, complete, and well-supported

Return ONLY a JSON object with these keys:
{{
    "score": 1,
    "reason": "Brief explanation",
    "strengths": ["Strength"],
    "weaknesses": ["Weakness"]
}}

The score must be an integer from 1 to 5.
"""

        result = self._parse_json(self._call_model(prompt))

        score = int(result["score"])

        if not 1 <= score <= 5:
            raise ValueError("Judge score must be between 1 and 5.")

        return {
            "question": question,
            "answer": answer,
            "score": score,
            "passed": score >= self.pass_threshold,
            "reason": str(result.get("reason", "")),
            "strengths": result.get("strengths", []),
            "weaknesses": result.get("weaknesses", []),
            "model": self.model_name,
        }

    def compare(
        self,
        question: str,
        answer_a: str,
        answer_b: str,
        context: Optional[str] = None,
        criteria: str = (
            "Compare correctness, relevance, completeness, "
            "and faithfulness to the context."
        ),
    ) -> Dict[str, Any]:
        """Compare two answers and identify the better answer."""

        prompt = f"""
Compare two answers to the same question.

Question:
{question}

Context:
{context or "Not provided"}

Answer A:
{answer_a}

Answer B:
{answer_b}

Criteria:
{criteria}

Choose the better answer based on the criteria, not its length.

Return ONLY this JSON structure:
{{
    "winner": "A",
    "reason": "Explanation",
    "score_a": 4,
    "score_b": 3
}}

winner must be A, B, or Tie.
Both scores must be integers from 1 to 5.
"""

        first = self._parse_json(self._call_model(prompt))

        # Reverse the answer order to reduce positional bias.
        reversed_prompt = f"""
Compare two answers to the same question.

Question:
{question}

Context:
{context or "Not provided"}

Answer A:
{answer_b}

Answer B:
{answer_a}

Criteria:
{criteria}

Return ONLY JSON:
{{
    "winner": "A",
    "reason": "Explanation",
    "score_a": 4,
    "score_b": 3
}}

winner must be A, B, or Tie.
"""

        second = self._parse_json(self._call_model(reversed_prompt))

        first_winner = str(first.get("winner", "Tie")).strip()
        second_winner = str(second.get("winner", "Tie")).strip()

        # Reverse the second result back to the original answer order.
        reverse_mapping = {"A": "B", "B": "A", "Tie": "Tie"}
        second_winner = reverse_mapping.get(second_winner, "Tie")

        if first_winner not in {"A", "B", "Tie"}:
            first_winner = "Tie"

        # Report a decisive winner only when both calls agree.
        winner = (
            first_winner
            if first_winner == second_winner
            else "Tie"
        )

        return {
            "question": question,
            "winner": winner,
            "reason": str(first.get("reason", "")),
            "score_a": first.get("score_a"),
            "score_b": first.get("score_b"),
            "consistent": first_winner == second_winner,
            "model": self.model_name,
        }

    def judge_batch(
        self,
        test_cases: List[Dict[str, Any]],
        criteria: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        """Evaluate multiple question-answer test cases."""

        results = []

        for index, case in enumerate(test_cases, start=1):
            print(f"Evaluating test case {index}/{len(test_cases)}")

            results.append(
                self.judge(
                    question=case["question"],
                    answer=case["answer"],
                    context=case.get("context"),
                    reference=case.get("reference"),
                    criteria=criteria or case.get("criteria") or (
                        "Evaluate correctness, relevance, completeness, "
                        "and faithfulness to the provided context."
                    ),
                )
            )

        return results

    def summarize(
        self,
        results: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """Calculate aggregate evaluation statistics."""

        if not results:
            return {
                "total": 0,
                "mean_score": 0.0,
                "passed": 0,
                "failed": 0,
                "pass_rate": 0.0,
            }

        scores = [float(result["score"]) for result in results]
        passed = sum(
            bool(result.get("passed", False)) for result in results
        )
        total = len(results)

        return {
            "total": total,
            "mean_score": round(sum(scores) / total, 2),
            "passed": passed,
            "failed": total - passed,
            "pass_rate": round(passed / total, 4),
        }


if __name__ == "__main__":
    # Smoke test: verify that the Groq judge can evaluate an answer.
    judge = GroqJudge(model_name=DEFAULT_MODEL)

    question = "What is RAG in an LLM application?"
    context = (
        "Retrieval-Augmented Generation retrieves relevant external "
        "information and provides it to an LLM to generate a grounded answer."
    )
    answer = (
        "RAG retrieves relevant information and supplies it to an LLM "
        "to help generate a context-grounded response."
    )

    single_result = judge.judge(
        question=question,
        answer=answer,
        context=context,
    )
    print("\nSingle-answer evaluation:")
    print(json.dumps(single_result, indent=2))

    comparison = judge.compare(
        question=question,
        answer_a=answer,
        answer_b="RAG is a method for training a model from scratch.",
        context=context,
    )
    print("\nPairwise comparison:")
    print(json.dumps(comparison, indent=2))

    batch_results = judge.judge_batch(
        [
            {
                "question": question,
                "answer": answer,
                "context": context,
            },
            {
                "question": question,
                "answer": "RAG trains an LLM from scratch.",
                "context": context,
            },
        ]
    )

    print("\nBatch summary:")
    print(json.dumps(judge.summarize(batch_results), indent=2))
