import chromadb
from chromadb.config import Settings
from langchain.vectorstores import Chroma
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from insightsGPT.lib.config import CHROMA_DB_COLLECTION, CHROMA_EMBEDDING_MODEL


def getDB():
    client = chromadb.HttpClient(settings=Settings())
    embedding_function = SentenceTransformerEmbeddings(model_name=CHROMA_EMBEDDING_MODEL)
    langchain_chroma = Chroma(
        client=client,
        collection_name=CHROMA_DB_COLLECTION,
        embedding_function=embedding_function,
    )
    return langchain_chroma
