from app.core.config import Settings


def test_settings_defaults():
    s = Settings()
    assert s.qdrant_collection == "documents"
    assert s.embedding_model == "sentence-transformers/all-MiniLM-L6-v2"
    assert s.chunk_size == 500
    assert s.chunk_overlap == 100
    assert s.default_top_k == 5
    assert s.max_top_k == 20


def test_settings_from_env(monkeypatch):
    monkeypatch.setenv("QDRANT_COLLECTION", "my_collection")
    monkeypatch.setenv("CHUNK_SIZE", "200")
    s = Settings(_env_file=None)
    assert s.qdrant_collection == "my_collection"
    assert s.chunk_size == 200
