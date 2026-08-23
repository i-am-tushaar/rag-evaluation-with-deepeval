import os

import instructor
from dotenv import load_dotenv
from pydantic import BaseModel

from deepeval.models import DeepEvalBaseLLM


load_dotenv()


class GroqJudge(DeepEvalBaseLLM):
    """Groq model wrapper for DeepEval."""

    def __init__(self, model_name):
        self.model_name = model_name

        self.client = instructor.from_provider(
            f"groq/{model_name}",
            api_key=os.getenv("GROQ_API_KEY"),
        )

    def load_model(self):
        return self.client

    def generate(
        self,
        prompt: str,
        schema: BaseModel | None = None,
    ):

        # Normal text generation
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
            )

            return response.choices[0].message.content

        # Structured generation required by DeepEval
        return self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            response_model=schema,
            temperature=0,
            max_retries=3,
        )

    async def a_generate(
        self,
        prompt: str,
        schema: BaseModel | None = None,
    ):
        return self.generate(
            prompt=prompt,
            schema=schema,
        )

    def get_model_name(self):
        return self.model_name