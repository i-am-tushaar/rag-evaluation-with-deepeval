import os
from dotenv import load_dotenv

load_dotenv()


def validate_langsmith_config():
    """Validate LangSmith configuration."""

    required_variables = [
        "LANGSMITH_API_KEY",
        "LANGSMITH_TRACING",
        "LANGSMITH_PROJECT",
    ]

    missing = [
        variable
        for variable in required_variables
        if not os.getenv(variable)
    ]

    if missing:
        raise EnvironmentError(
            f"Missing LangSmith environment variables: {missing}"
        )


if __name__ == "__main__":
    validate_langsmith_config()
    print("LangSmith configuration is valid.")