import os
import re
import glob

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


# ============================================================
# CONFIGURATION
# ============================================================

DATA_DIR = "data"
DB_DIR = "chroma_store"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

COLLECTION_NAME = "rag_documents"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150

TOP_K = 5


# ============================================================
# 1. LOAD
# Read VTT transcripts and remove timestamps
# ============================================================

def load_transcripts():

    documents = []

    for path in glob.glob(f"{DATA_DIR}/*.vtt"):

        lines = []

        with open(path, "r", encoding="utf-8") as file:

            for line in file:

                line = line.strip()

                # Remove empty lines, WEBVTT and timestamps
                if not line or line == "WEBVTT" or "-->" in line:
                    continue

                lines.append(line)

        text = " ".join(lines)

        # Extract session number
        match = re.search(r"Session[ _]*(\d+)", path)

        session = match.group(1) if match else "unknown"

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "session": session,
                    "source": path,
                },
            )
        )

    return documents


# ============================================================
# 2. BUILD
# Create embeddings and Chroma vector store
# ============================================================

def load_store():

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    # If Chroma already exists, load it
    if os.path.exists(DB_DIR):

        return Chroma(
            collection_name=COLLECTION_NAME,
            persist_directory=DB_DIR,
            embedding_function=embeddings,
        )

    # Otherwise load documents
    documents = load_transcripts()

    # Create chunks
    chunks = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    ).split_documents(documents)

    print(f"Total chunks created: {len(chunks)}")

    # Create Chroma database
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        persist_directory=DB_DIR,
    )

    return vector_store


# ============================================================
# 3. RETRIEVER
# ============================================================

def build_retriever():

    return load_store().as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": TOP_K
        },
    )


# ============================================================
# 4. TEST
# Run:
# python -m src.retrieval.retriever
# ============================================================

if __name__ == "__main__":

    print("Building retriever...")

    retriever = build_retriever()

    query = "What is RAG?"

    print(f"\nQuery: {query}")

    results = retriever.invoke(query)

    print(f"\nRetrieved chunks: {len(results)}")

    for i, doc in enumerate(results, 1):

        print(f"\n--- Result {i} ---")

        print(
            f"[Session {doc.metadata.get('session')}]"
        )

        print(
            f"Source: {doc.metadata.get('source')}"
        )

        print(
            f"{doc.page_content[:300]}..."
        )


# ============================================================
# WORKFLOW
# ============================================================
#
# VTT Files
#      ↓
# load_transcripts()
#      ↓
# Clean transcript
#      ↓
# Create Documents
#      ↓
# RecursiveCharacterTextSplitter
#      ↓
# chunk_size = 750
# chunk_overlap = 100
#      ↓
# Document Chunks
#      ↓
# Hugging Face Embeddings
#      ↓
# Chroma Vector Store
#      ↓
# Save to chroma_store/
#      ↓
# build_retriever()
#      ↓
# Similarity Search
#      ↓
# top_k = 5
#      ↓
# Retrieved Chunks
#
# ============================================================
# IMPORTANT
# ============================================================
#
# First run:
#
#     python -m src.retrieval.retriever
#
# This creates chroma_store/ if it doesn't exist.
#
# Later runs:
#
#     python -m src.retrieval.retriever
#
# Existing Chroma is loaded instead of re-embedding
# the documents.
#
# If you change:
#
#     chunk_size
#     chunk_overlap
#     embedding_model
#     source documents
#
# delete chroma_store/ and rebuild it.
#
# If you only change:
#
#     TOP_K
#
# you do NOT need to delete Chroma.
#
# ============================================================