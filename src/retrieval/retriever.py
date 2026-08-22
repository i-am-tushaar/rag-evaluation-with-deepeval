import os

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from src.ingestion.data_ingestion import ingest_data


# Load environment variables
load_dotenv()

# Chroma database directory
DB_DIR = "chroma_store"

# Hugging Face token
HF_TOKEN = os.getenv("HF_TOKEN")

# Embedding model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Chroma collection
COLLECTION_NAME = "rag_documents"


def create_embeddings():
    """
    Create the Hugging Face embedding model.
    """

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    return embeddings


def create_vector_store(documents):
    """
    Create Chroma vector store and add document chunks.
    """

    if not documents:
        raise ValueError("No documents provided.")

    embeddings = create_embeddings()

    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=DB_DIR,
    )

    vector_store.add_documents(documents)

    return vector_store


def retrieve_documents(vector_store, query, top_k=5):
    """
    Retrieve the top-k relevant document chunks.
    """

    if not query.strip():
        raise ValueError("Query cannot be empty.")

    results = vector_store.similarity_search(
        query,
        k=top_k
    )

    return results


def retrieve_with_scores(vector_store, query, top_k=5):
    """
    Retrieve relevant chunks with similarity scores.
    """

    if not query.strip():
        raise ValueError("Query cannot be empty.")

    results = vector_store.similarity_search_with_score(
        query,
        k=top_k
    )

    return results


if __name__ == "__main__":

    print("Loading transcript chunks...")

    # Use existing data ingestion pipeline
    chunks = ingest_data()

    print(f"Total chunks: {len(chunks)}")

    # Create Chroma vector store
    print("Creating Chroma vector store...")

    vector_store = create_vector_store(chunks)

    print(f"Chroma database created at: {DB_DIR}")

    # Test query
    query = "What is RAG Triad?"

    print(f"\nQuery: {query}")

    results = retrieve_documents(
        vector_store=vector_store,
        query=query,
        top_k=5
    )

    print(f"Retrieved chunks: {len(results)}")

    for index, document in enumerate(results, start=1):

        print(f"\n--- Result {index} ---")

        print(
            "Source:",
            document.metadata.get("source")
        )

        print(
            "Session:",
            document.metadata.get("session")
        )

        print(
            "Content:",
            document.page_content[:500]
        )