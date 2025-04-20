from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def load_vectorstore():
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local("embeddings/vectorstore_index", embeddings, allow_dangerous_deserialization=True)