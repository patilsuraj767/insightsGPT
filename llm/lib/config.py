import os

LLM_API_PORT = os.getenv("LLM_API_PORT", "8080")
LLM_MAX_NEW_TOKEN = os.getenv("LLM_MAX_NEW_TOKEN", 512)
LLM_MIN_LENGTH = os.getenv("min_length", 5)
