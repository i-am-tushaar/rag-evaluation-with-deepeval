import glob
import re

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


DATA_DIR = "data"


def load_transcripts():
    """Load and clean VTT transcript files."""

    documents = []

    for path in glob.glob(f"{DATA_DIR}/*.vtt"):

        lines = []

        with open(path, "r", encoding="utf-8") as file:

            for line in file:

                # Remove VTT timestamps and WEBVTT line
                if "WEBVTT" in line or "-->" in line:
                    continue

                line = line.strip()

                if line:
                    lines.append(line)

        text = " ".join(lines)

        # Extract session number from filename
        match = re.search(r"Session[_ ](\d+)", path)

        session = match.group(1) if match else "unknown"

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "session": session,
                    "source": path
                }
            )
        )

    return documents


def create_chunks(documents):
    """Split documents into smaller chunks."""

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=750,
        chunk_overlap=100
    )

    return splitter.split_documents(documents)


def ingest_data():
    """Complete ingestion pipeline."""

    documents = load_transcripts()

    chunks = create_chunks(documents)

    return chunks


if __name__ == "__main__":

    chunks = ingest_data()

    print(f"Total chunks created: {len(chunks)}")

    for chunk in chunks[:3]:
        print("\n--- CHUNK ---")
        print(chunk.page_content[:500])
        print(chunk.metadata)