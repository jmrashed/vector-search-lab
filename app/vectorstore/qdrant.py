import uuid

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams

from app.models.schemas import Chunk, SearchResult
from app.vectorstore.base import VectorStore


class QdrantVectorStore(VectorStore):
    def __init__(self, collection: str):
        self._client = QdrantClient(path="./.qdrant")
        self._collection = collection

    def create_collection(self, name: str, vector_size: int) -> None:
        existing = [c.name for c in self._client.get_collections().collections]
        if name not in existing:
            self._client.create_collection(
                collection_name=name,
                vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
            )

    def upsert(self, chunks: list[Chunk], vectors: list[list[float]]) -> None:
        points = [
            PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload={
                    "text": chunk.text,
                    "source": chunk.source,
                    "chunk_index": chunk.chunk_index,
                },
            )
            for chunk, vector in zip(chunks, vectors)
        ]
        self._client.upsert(collection_name=self._collection, points=points)

    def search(self, vector: list[float], k: int) -> list[SearchResult]:
        response = self._client.query_points(
            collection_name=self._collection,
            query=vector,
            limit=k,
        )
        return [
            SearchResult(
                score=hit.score,
                source=hit.payload["source"],
                chunk_index=hit.payload["chunk_index"],
                text=hit.payload["text"],
            )
            for hit in response.points
        ]
