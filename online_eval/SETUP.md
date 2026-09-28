# LangSmith Online Evaluation Setup

## Step 1: Create a LangSmith Project

1. Open LangSmith.
2. Sign in.
3. Create a new project.
4. Example project name:

   `rag-online-evaluation`

5. Use this project for RAG production traces.

## Step 2: Generate LangSmith API Key

Generate an API key from LangSmith.

Do not commit the API key to GitHub.

## Step 3: Add LangSmith Configuration to .env

Add the following to the root `.env` file:

LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=rag-online-evaluation

If required by the selected LangSmith environment, configure the appropriate endpoint as well.

## Step 4: Install LangSmith

Install the LangSmith SDK:

pip install -U langsmith

If the application uses LangChain, keep the existing LangChain dependencies.

## Step 5: Load Environment Variables

The application should load `.env` before the RAG pipeline starts.

Example:

from dotenv import load_dotenv
load_dotenv()

LangSmith tracing is enabled through the environment variables.

## Security

Never commit `.env` to Git.

The `.gitignore` should contain:

.env