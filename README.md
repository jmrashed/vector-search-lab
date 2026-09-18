# Vector Search Lab

> A small, open-source project for learning **vector databases, embeddings, semantic search, chunking, metadata filtering, and hybrid retrieval** through a practical developer-documentation search engine.

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-API-009688.svg)](https://fastapi.tiangolo.com/)
[![Qdrant](https://img.shields.io/badge/Qdrant-Vector%20DB-red.svg)](https://qdrant.tech/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Overview

**Vector Search Lab** is a lightweight semantic-search project built to understand how modern vector search systems work internally.

Instead of starting with a large RAG framework, this project keeps the architecture intentionally simple:

```text
Documents
    │
    ▼
Text Extraction
    │
    ▼
Chunking
    │
    ▼
Embedding Model
    │
    ▼
Qdrant Vector Database
    │
    ├── Vector
    ├── Metadata
    └── Document Reference
    │
    ▼
Semantic Search
    │
    ▼
Ranked Results
```

The initial use case is searching developer documentation using natural-language queries.

For example:

```text
Query:
"How do I authenticate an API request?"
```

The system can retrieve relevant documentation even when the exact words in the query do not appear in the documents.

---

## Why This Project?

Vector databases are becoming an important component of:

* AI applications
* RAG systems
* semantic search
* recommendation systems
* document retrieval
* code search
* knowledge bases
* AI agents

This project exists primarily as a **learning laboratory**.

The goal is to understand what happens between:

```text
User Query
    ↓
Embedding
    ↓
Vector Search
    ↓
Similarity Ranking
    ↓
Relevant Context
```

before introducing more complex AI/RAG abstractions.

---

## Learning Goals

This project covers the fundamentals of vector search step by step.

### Core concepts

* What embeddings are
* Vector dimensions
* Vector similarity
* Distance metrics
* Vector collections
* Vector indexing
* Metadata/payloads
* Similarity search
* Top-K retrieval
* Metadata filtering
* Chunking strategies
* Embedding models
* Hybrid search
* Reranking
* Retrieval evaluation
* RAG fundamentals

---

## Features

### Current

* [ ] Document ingestion
* [ ] Text extraction
* [ ] Document chunking
* [ ] Embedding generation
* [ ] Qdrant integration
* [ ] Semantic similarity search
* [ ] Document metadata
* [ ] Metadata filtering
* [ ] REST API
* [ ] Docker-based local development

### Planned

* [ ] Multiple embedding models
* [ ] Configurable chunk sizes
* [ ] Chunk overlap experiments
* [ ] Keyword search
* [ ] Hybrid search
* [ ] Reranking
* [ ] Search evaluation
* [ ] Query performance benchmarks
* [ ] Simple web UI
* [ ] Optional LLM-powered answers
* [ ] RAG mode
* [ ] Code/documentation search
* [ ] Search analytics

---

## Technology Stack

| Component         | Technology            |
| ----------------- | --------------------- |
| Language          | Python 3.11+          |
| API               | FastAPI               |
| Vector Database   | Qdrant                |
| Embeddings        | Sentence Transformers |
| Containerization  | Docker                |
| API Documentation | OpenAPI / Swagger     |
| Testing           | Pytest                |
| Configuration     | Environment variables |

The project deliberately avoids a large AI framework in the initial stages so that the underlying vector-search workflow remains visible.

---

## Architecture

```text
                         ┌─────────────────────┐
                         │   Developer Docs    │
                         │ Markdown / TXT / PDF│
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Text Extraction   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      Chunking       │
                         │  size + overlap     │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Embedding Model   │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │       Qdrant        │
                         │                     │
                         │ Vector + Payload    │
                         └──────────┬──────────┘
                                    │
                                    │
 User Query ────────► Embedding ────┤
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Similarity Search   │
                         │       Top-K         │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Search Results    │
                         └─────────────────────┘
```

---

## Example Document

A document may contain:

```text
Title:
Laravel Authentication

Content:
Laravel provides several authentication mechanisms...
```

After processing, it becomes a chunk:

```json
{
  "text": "Laravel provides several authentication mechanisms...",
  "metadata": {
    "title": "Laravel Authentication",
    "framework": "laravel",
    "version": "11",
    "language": "php",
    "source": "laravel-auth.md"
  }
}
```

The text is converted into an embedding:

```text
[0.0231, -0.1842, 0.7742, ...]
```

The vector and metadata are stored in Qdrant.

---

## Semantic Search Example

### Query

```text
How can I authenticate API requests?
```

Traditional keyword search may look for:

```text
authenticate
API
requests
```

Vector search instead compares the semantic meaning of the query against document embeddings.

Possible results:

```text
1. API Authentication
   Score: 0.91

2. JWT Authentication Middleware
   Score: 0.87

3. OAuth Authentication
   Score: 0.82
```

The exact score depends on the embedding model and distance metric.

---

## Metadata Filtering

Vector similarity can be combined with structured filtering.

Example metadata:

```json
{
  "framework": "laravel",
  "version": "11",
  "language": "php",
  "type": "documentation"
}
```

Search:

```text
Query:
"How do I create middleware?"

Filter:
framework = laravel
version = 11
```

Conceptually:

```text
Semantic Similarity
        +
Metadata Filter
        ↓
Relevant Results
```

This is an important Vector DB concept that pure semantic search examples often overlook.

---

## Chunking Experiments

One of the goals of this project is to understand how chunk size affects retrieval quality.

Experiments can use:

```text
Chunk Size     Overlap
-----------    -------
200 tokens     40
500 tokens     100
800 tokens     150
1000 tokens    200
```

The project should allow these values to be configured rather than hard-coded.

Example:

```env
CHUNK_SIZE=500
CHUNK_OVERLAP=100
```

Search quality can then be compared between configurations.

---

## Embedding Experiments

The embedding layer should remain replaceable.

Initial implementation:

```text
Sentence Transformers
        ↓
Local Embedding Model
```

Later experiments can compare different embedding models.

The goal is to understand:

* embedding dimensions
* model quality
* semantic similarity
* inference speed
* storage requirements
* retrieval quality

---

## Vector Database

The initial Vector DB is **Qdrant**.

Qdrant is used because it provides:

* vector collections
* similarity search
* metadata/payload storage
* filtering
* configurable distance metrics
* Docker support
* self-hosted deployment

The application should keep the vector-store layer behind a small interface so another database can be added later.

Potential future backends:

```text
Qdrant
Chroma
pgvector
Weaviate
Milvus
```

---

## Distance Metrics

The project will experiment with common similarity approaches such as:

### Cosine Similarity

Measures the angle between vectors.

```text
similar direction
       ↓
higher similarity
```

### Euclidean Distance

Measures the geometric distance between vectors.

```text
smaller distance
       ↓
more similar
```

### Dot Product

Measures the product of vector components.

The exact metric should be selected based on the embedding model and retrieval requirements.

---

## API

The planned API structure is intentionally small.

### Health Check

```http
GET /health
```

### Create / Ingest Document

```http
POST /api/documents
```

### List Documents

```http
GET /api/documents
```

### Search

```http
POST /api/search
```

Example:

```json
{
  "query": "How do I authenticate an API request?",
  "limit": 5
}
```

Example response:

```json
{
  "query": "How do I authenticate an API request?",
  "results": [
    {
      "score": 0.91,
      "text": "API authentication...",
      "metadata": {
        "framework": "laravel",
        "version": "11"
      }
    }
  ]
}
```

---

## Local Development

### Requirements

Install:

* Python 3.11+
* Docker
* Docker Compose
* Git

### Clone

```bash
git clone https://github.com/jmrashed/vector-search-lab.git

cd vector-search-lab
```

### Environment

```bash
cp .env.example .env
```

Configure the required values.

Example:

```env
APP_ENV=local
APP_HOST=0.0.0.0
APP_PORT=8000

QDRANT_HOST=localhost
QDRANT_PORT=6333
QDRANT_COLLECTION=documents

EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

CHUNK_SIZE=500
CHUNK_OVERLAP=100
```

### Start Qdrant

```bash
docker compose up -d qdrant
```

Check the service:

```bash
docker compose ps
```

### Install Python dependencies

```bash
python -m venv .venv

source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Start API

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/docs
```

---

## Docker Development

Run the complete local environment:

```bash
docker compose up -d
```

Stop:

```bash
docker compose down
```

Remove local Qdrant data:

```bash
docker compose down -v
```

---

## Project Structure

```text
vector-search-lab/
│
├── app/
│   ├── api/
│   │   ├── documents.py
│   │   ├── search.py
│   │   └── health.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── logging.py
│   │
│   ├── embeddings/
│   │   └── service.py
│   │
│   ├── chunking/
│   │   └── service.py
│   │
│   ├── vectorstore/
│   │   ├── base.py
│   │   └── qdrant.py
│   │
│   ├── models/
│   │   └── schemas.py
│   │
│   └── main.py
│
├── data/
│   └── documents/
│
├── scripts/
│   ├── ingest.py
│   └── search.py
│
├── tests/
│   ├── test_chunking.py
│   ├── test_embeddings.py
│   └── test_search.py
│
├── docs/
│   ├── 01-embeddings.md
│   ├── 02-vector-db-basics.md
│   ├── 03-similarity-search.md
│   ├── 04-chunking.md
│   ├── 05-metadata-filtering.md
│   ├── 06-hybrid-search.md
│   ├── 07-reranking.md
│   └── 08-rag.md
│
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Learning Roadmap

The project should evolve in small stages.

### Phase 1 — Vector Basics

```text
Document
   ↓
Embedding
   ↓
Vector
   ↓
Qdrant
```

Learn:

* vectors
* dimensions
* embeddings
* collections
* points
* similarity

### Phase 2 — Semantic Search

```text
Query
 ↓
Embedding
 ↓
Vector Search
 ↓
Top-K Results
```

Learn:

* cosine similarity
* Top-K
* similarity scores
* result ranking

### Phase 3 — Document Processing

Add:

```text
PDF
Markdown
TXT
HTML
```

Learn:

* extraction
* cleaning
* chunking
* overlap
* metadata

### Phase 4 — Filtering

Add:

```text
Vector similarity
+
Metadata filtering
```

Learn how structured and semantic retrieval work together.

### Phase 5 — Hybrid Search

Implement:

```text
Keyword Search
       +
Vector Search
       ↓
Combined Ranking
```

Learn why semantic search does not completely replace traditional search.

### Phase 6 — Reranking

```text
Vector Search
      ↓
Top 50 candidates
      ↓
Reranker
      ↓
Top 5 results
```

Learn how a two-stage retrieval system works.

### Phase 7 — RAG

Only after understanding retrieval:

```text
User Query
    ↓
Vector Search
    ↓
Relevant Chunks
    ↓
LLM
    ↓
Answer
```

The RAG layer should be optional.

---

## Experiments

This repository is intended to contain measurable experiments.

Example:

| Experiment | Variable    | Result |
| ---------- | ----------- | ------ |
| Chunking   | 200 tokens  | TBD    |
| Chunking   | 500 tokens  | TBD    |
| Chunking   | 1000 tokens | TBD    |
| Embedding  | Model A     | TBD    |
| Embedding  | Model B     | TBD    |
| Retrieval  | Top-K 5     | TBD    |
| Retrieval  | Top-K 10    | TBD    |
| Search     | Vector      | TBD    |
| Search     | Hybrid      | TBD    |

The objective is not simply to make search work.

The objective is to understand **why one configuration behaves differently from another**.

---

## Performance Metrics

Future experiments can measure:

### Ingestion

```text
Documents / second
Chunks / second
Embedding latency
```

### Search

```text
Query latency
Vector DB latency
Embedding latency
Total response time
```

### Retrieval Quality

Possible metrics:

```text
Precision@K
Recall@K
MRR
nDCG
```

A small manually labeled evaluation dataset can be added under:

```text
tests/evaluation/
```

---

## What This Project Is Not

This is intentionally **not**:

* a full enterprise RAG platform
* an AI agent framework
* a production knowledge-management system
* a replacement for Elasticsearch/OpenSearch
* a wrapper around a single LLM API

The primary objective is learning and experimentation.

---

## Future Ideas

Once the fundamentals are understood, the project can evolve into:

### Developer Documentation Search

```text
Laravel
React
Next.js
Docker
AWS
PostgreSQL
Redis
```

### Code Search

Search source code using natural language:

```text
"Where is JWT authentication implemented?"
```

### Personal Knowledge Base

```text
Notes
Documents
README files
Technical articles
Architecture documents
```

### AI Knowledge Assistant

```text
Documents
    ↓
Vector DB
    ↓
Retriever
    ↓
LLM
    ↓
Answer + Sources
```

---

## Design Principles

### 1. Understand before abstracting

Avoid hiding Vector DB operations behind a large framework.

### 2. Keep components replaceable

Embedding providers and vector databases should be replaceable.

### 3. Measure experiments

Do not rely only on subjective search quality.

### 4. Start local

The complete learning environment should run locally with Docker.

### 5. Keep the MVP small

Every feature should contribute to understanding search, retrieval, or vector databases.

---

## Contributing

Contributions are welcome.

Good contributions include:

* new embedding experiments
* new chunking strategies
* vector database adapters
* retrieval benchmarks
* documentation improvements
* test datasets
* search-quality experiments

For larger changes, open an issue first to discuss the approach.

---

## License

This project is licensed under the MIT License.

See [LICENSE](LICENSE) for details.

---

## Author

**Rashed Zaman**

Technical Project Manager · Tech Lead · Full-Stack Developer

* GitHub: https://github.com/jmrashed
* LinkedIn: https://linkedin.com/in/jmrashed
* Portfolio: https://jmrashed.github.io

---

## Learning Resources

* [Qdrant Documentation](https://qdrant.tech/documentation/)
* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [Sentence Transformers Documentation](https://sbert.net/)
* [Docker Documentation](https://docs.docker.com/)

---

## Status

🚧 **Learning / Experimental**

The project is intentionally evolving as new Vector DB and retrieval concepts are explored.
