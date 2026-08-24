import os
import json

from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel

from deepeval.models import DeepEvalBaseLLM


load_dotenv()


class GroqJudge(DeepEvalBaseLLM):

    def __init__(self, model_name):
        self.model_name = model_name

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def load_model(self):
        return self.client

    def generate(
        self,
        prompt: str,
        schema: BaseModel | None = None,
    ):

        # -----------------------------------------
        # Normal generation
        # -----------------------------------------
        if schema is None:

            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                temperature=0,
                reasoning_effort="low",
            )

            return response.choices[0].message.content

        # -----------------------------------------
        # DeepEval structured generation
        # -----------------------------------------

        schema_text = json.dumps(
            schema.model_json_schema(),
            indent=2,
        )

        json_prompt = f"""
{prompt}

IMPORTANT OUTPUT INSTRUCTIONS:

Return ONLY one valid JSON object.

Do NOT return:
- markdown
- ```json
- explanations
- comments
- extra text

Your response must follow this schema:

{schema_text}

Return only the JSON object.
"""

        response = self.client.chat.completions.create(
            model=self.model_name,

            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a JSON-only evaluation judge. "
                        "Return exactly one valid JSON object "
                        "and nothing else."
                    ),
                },
                {
                    "role": "user",
                    "content": json_prompt,
                },
            ],

            temperature=0,
            reasoning_effort="low",
        )

        output = response.choices[0].message.content

        if not output:
            raise ValueError(
                "Groq returned an empty response."
            )

        # -----------------------------------------
        # Clean accidental markdown
        # -----------------------------------------

        output = output.strip()

        if output.startswith("```json"):
            output = output[7:]

        elif output.startswith("```"):
            output = output[3:]

        if output.endswith("```"):
            output = output[:-3]

        output = output.strip()

        # -----------------------------------------
        # Parse JSON
        # -----------------------------------------

        try:
            data = json.loads(output)

        except json.JSONDecodeError as e:
            raise ValueError(
                f"Groq returned invalid JSON:\n{output}"
            ) from e

        # -----------------------------------------
        # Convert into DeepEval schema
        # -----------------------------------------

        return schema.model_validate(data)

    async def a_generate(
        self,
        prompt: str,
        schema: BaseModel | None = None,
    ):
        return self.generate(
            prompt,
            schema,
        )

    def get_model_name(self):
        return self.model_name