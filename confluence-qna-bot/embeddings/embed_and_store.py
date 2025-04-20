from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from dotenv import load_dotenv
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname('__file__'), "..")))

from ingestion.confluence_scraper import fetch_confluence_pages
load_dotenv()

def create_vector_store(space_key="DOC"):
    documents = fetch_confluence_pages(space_key)
    texts = [doc["content"] for doc in documents]

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.create_documents(texts)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local("vectorstore_index")

if __name__ == "__main__":
    create_vector_store("DOC")