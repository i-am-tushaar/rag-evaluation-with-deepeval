from src.ingestion.data_ingestion import (
    load_transcripts,
    create_chunks,
    ingest_data,
)


def test_load_transcripts():
    documents = load_transcripts()

    assert len(documents) > 0

    for document in documents:
        assert document.page_content
        assert "session" in document.metadata
        assert "source" in document.metadata


def test_create_chunks():
    documents = load_transcripts()
    chunks = create_chunks(documents)

    assert len(chunks) > 0

    for chunk in chunks:
        assert chunk.page_content


def test_ingest_data():
    chunks = ingest_data()

    assert len(chunks) > 0