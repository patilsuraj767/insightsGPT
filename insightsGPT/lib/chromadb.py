import chromadb
from chromadb.config import Settings
from langchain.vectorstores import Chroma
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from insightsGPT.lib.config import CHROMA_DB_COLLECTION, CHROMA_EMBEDDING_MODEL, CHROMA_DB_HOST, CHROMA_DB_PORT


def getDB():
    client = chromadb.HttpClient(host=CHROMA_DB_HOST, port=CHROMA_DB_PORT, settings=Settings())
    embedding_function = SentenceTransformerEmbeddings(model_name=CHROMA_EMBEDDING_MODEL)
    langchain_chroma = Chroma(
        client=client,
        collection_name=CHROMA_DB_COLLECTION,
        embedding_function=embedding_function,
    )
    return langchain_chroma
