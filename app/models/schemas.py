from pydantic import BaseModel


class Document(BaseModel):
    source: str
    text: str


class Chunk(BaseModel):
    source: str
    chunk_index: int
    text: str


class SearchResult(BaseModel):
    score: float
    source: str
    chunk_index: int
    text: str
