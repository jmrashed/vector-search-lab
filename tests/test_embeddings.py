import numpy as np
import pytest
from app.embeddings.service import EmbeddingService

MODEL = "sentence-transformers/all-MiniLM-L6-v2"


@pytest.fixture(scope="module")
def embedder():
    return EmbeddingService(MODEL)


def test_embed_single_text_shape(embedder):
    result = embedder.embed(["Hello world"])
    assert len(result) == 1
    assert len(result[0]) == 384


def test_embed_multiple_texts_shape(embedder):
    result = embedder.embed(["Hello", "World", "Foo"])
    assert len(result) == 3
    assert all(len(v) == 384 for v in result)


def test_embed_returns_floats(embedder):
    result = embedder.embed(["Hello world"])
    assert all(isinstance(x, float) for x in result[0])


def test_similar_texts_score_higher_than_unrelated(embedder):
    v_docker = np.array(embedder.embed(["Docker volumes persist data between container restarts"])[0])
    v_storage = np.array(embedder.embed(["Container storage is preserved using named volumes"])[0])
    v_weather = np.array(embedder.embed(["The weather is sunny today in the park"])[0])

    def cosine(a, b):
        return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

    assert cosine(v_docker, v_storage) > cosine(v_docker, v_weather)
