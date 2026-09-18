from abc import ABC, abstractmethod

from app.models.schemas import Chunk, SearchResult


class VectorStore(ABC):
    @abstractmethod
    def create_collection(self, name: str, vector_size: int) -> None: ...

    @abstractmethod
    def upsert(self, chunks: list[Chunk], vectors: list[list[float]]) -> None: ...

    @abstractmethod
    def search(self, vector: list[float], k: int) -> list[SearchResult]: ...
