import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.core.config import settings
from app.models.schemas import Document
from app.chunking.service import chunk
from app.embeddings.service import EmbeddingService
from app.vectorstore.qdrant import QdrantVectorStore

DOCS_DIR = Path(__file__).parent.parent / "data" / "documents"


def main() -> None:
    md_files = sorted(DOCS_DIR.glob("*.md"))
    if not md_files:
        print(f"No .md files found in {DOCS_DIR}. Nothing to ingest.")
        sys.exit(0)

    embedder = EmbeddingService(settings.embedding_model)
    store = QdrantVectorStore(settings.qdrant_collection)

    sample_vector = embedder.embed(["probe"])[0]
    store.create_collection(settings.qdrant_collection, len(sample_vector))

    total_chunks = 0

    for path in md_files:
        doc = Document(source=path.name, text=path.read_text(encoding="utf-8"))
        chunks = chunk(doc.text, doc.source, settings.chunk_size, settings.chunk_overlap)
        vectors = embedder.embed([c.text for c in chunks])
        store.upsert(chunks, vectors)
        total_chunks += len(chunks)
        print(f"  {path.name}: {len(chunks)} chunk(s)")

    print(f"\nDone. {total_chunks} total chunks from {len(md_files)} files.")


if __name__ == "__main__":
    main()
