from app.chunking.service import chunk
from app.models.schemas import Chunk


def test_chunk_returns_list_of_chunks():
    text = " ".join(f"word{i}" for i in range(100))
    result = chunk(text, "test.md", size=50, overlap=10)
    assert all(isinstance(c, Chunk) for c in result)


def test_chunk_count():
    # 1000 words, size=200, overlap=40 → step=160
    # starts: 0,160,320,480,640,800,960 → 7 chunks
    text = " ".join(f"word{i}" for i in range(1000))
    result = chunk(text, "test.md", size=200, overlap=40)
    assert len(result) == 7


def test_chunk_size_not_exceeded():
    text = " ".join(f"word{i}" for i in range(1000))
    result = chunk(text, "test.md", size=200, overlap=40)
    for c in result[:-1]:
        assert len(c.text.split()) <= 200


def test_chunk_overlap():
    text = " ".join(f"word{i}" for i in range(300))
    result = chunk(text, "test.md", size=100, overlap=20)
    last_20_of_chunk0 = result[0].text.split()[-20:]
    first_20_of_chunk1 = result[1].text.split()[:20]
    assert last_20_of_chunk0 == first_20_of_chunk1


def test_chunk_sets_source():
    text = " ".join(f"word{i}" for i in range(100))
    result = chunk(text, "my-file.md", size=50, overlap=10)
    assert all(c.source == "my-file.md" for c in result)


def test_chunk_sets_index():
    text = " ".join(f"word{i}" for i in range(300))
    result = chunk(text, "test.md", size=100, overlap=20)
    assert [c.chunk_index for c in result] == list(range(len(result)))


def test_empty_text_returns_empty_list():
    result = chunk("", "test.md", size=200, overlap=40)
    assert result == []


def test_overlap_equals_size_raises():
    import pytest
    with pytest.raises(ValueError):
        chunk("word " * 100, "test.md", size=100, overlap=100)
