import os

LLM_API_PORT = os.getenv("LLM_API_PORT", "8080")
LLM_MAX_NEW_TOKEN = os.getenv("LLM_MAX_NEW_TOKEN", 2000)
LLM_MIN_LENGTH = os.getenv("min_length", 100)
LLM_HOST = os.getenv("LLM_HOST", "localhost")
LLM_PORT = os.getenv("LLM_PORT", "8080")
CHROMA_DB_COLLECTION = os.getenv("CHROMA_DB_COLLECTION", "my_collection")
CHROMA_EMBEDDING_MODEL = os.getenv("CHROMA_EMBEDDING_MODEL", "all-MiniLM-L6-v2")
CHROMA_DB_HOST = os.getenv("CHROMA_DB_HOST", "localhost")
CHROMA_DB_PORT = os.getenv("CHROMA_DB_PORT", "8000")
