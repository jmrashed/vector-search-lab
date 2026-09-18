import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.core.config import settings
from app.embeddings.service import EmbeddingService
from app.vectorstore.qdrant import QdrantVectorStore


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python scripts/search.py \"your query here\"")
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    embedder = EmbeddingService(settings.embedding_model)
    store = QdrantVectorStore(settings.qdrant_collection)

    vector = embedder.embed([query])[0]
    try:
        results = store.search(vector, settings.default_top_k)
    except Exception:
        print("Error: collection not found. Run scripts/ingest.py first.")
        sys.exit(1)

    print(f"\nQuery: {query}\n")
    for i, result in enumerate(results, 1):
        preview = result.text[:120].replace("\n", " ")
        print(f"{i}. [{result.score:.4f}] {result.source}  (chunk {result.chunk_index})")
        print(f"   {preview}...")
        print()

    if not results:
        print("No results found. Run scripts/ingest.py first.")


if __name__ == "__main__":
    main()
