from app.models.schemas import Chunk


def chunk(text: str, source: str, size: int, overlap: int) -> list[Chunk]:
    if overlap >= size:
        raise ValueError(f"overlap ({overlap}) must be less than size ({size})")

    words = text.split()
    if not words:
        return []

    step = size - overlap
    chunks = []
    start = 0
    index = 0

    while start < len(words):
        end = start + size
        chunk_text = " ".join(words[start:end])
        chunks.append(Chunk(source=source, chunk_index=index, text=chunk_text))
        index += 1
        start += step

    return chunks
