import pytest

from src.ingestion.data_ingestion import ingest_data
from src.retrieval.retriever import (
    create_vector_store,
    retrieve_documents,
    retrieve_with_scores,
)


@pytest.fixture(scope="session")
def vector_store():
    """
    Create the Chroma vector store once for the entire test session.
    """

    chunks = ingest_data()

    assert len(chunks) > 0

    return create_vector_store(chunks)


def test_create_vector_store(vector_store):
    """Test that the Chroma vector store is created successfully."""

    assert vector_store is not None


def test_retrieve_documents(vector_store):
    """Test retrieval of relevant documents."""

    query = "What is the Document-ID flaw?"

    results = retrieve_documents(
        vector_store=vector_store,
        query=query,
        top_k=5,
    )

    assert results
    assert len(results) <= 5

    for document in results:
        assert document.page_content
        assert "source" in document.metadata
        assert "session" in document.metadata


def test_retrieve_with_scores(vector_store):
    """Test retrieval with similarity scores."""

    query = "What is the Document-ID flaw?"

    results = retrieve_with_scores(
        vector_store=vector_store,
        query=query,
        top_k=5,
    )

    assert results
    assert len(results) <= 5

    for document, score in results:
        assert document.page_content
        assert isinstance(score, float)