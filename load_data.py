import os
from langchain.document_loaders import JSONLoader
from langchain.vectorstores import Chroma
import chromadb
from chromadb.config import Settings
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from insightsGPT.lib.config import CHROMA_DB_HOST, CHROMA_DB_PORT


def load_kcs_article(f):
    loader = JSONLoader(
        file_path='./docs/kcs/'+f,
        jq_schema='" Title = " + .title + " Issue = " + .issue.text + " Resolution = " + .resolution.text + " Root Cause = " + .rootCause.text')  # noqa: E501

    data = loader.load()
    return data


def main():
    files = [f for f in os.listdir("./docs/kcs/")]
    for f in files:
        documents = load_kcs_article(f)
        # print(documents)
        # print(len(documents[0].page_content))
        # print("==============================")
        client = chromadb.HttpClient(host=CHROMA_DB_HOST, port=CHROMA_DB_PORT, settings=Settings())
        embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        langchain_chroma = Chroma(
            client=client,
            collection_name="my_collection",
            embedding_function=embedding_function,
        )

        langchain_chroma.add_documents(documents)


if __name__ == '__main__':
    main()
