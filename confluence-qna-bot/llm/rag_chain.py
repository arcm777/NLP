from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from retrieval.retriever import load_vectorstore
from dotenv import load_dotenv
import os

load_dotenv()



def build_rag_chain():
    llm = ChatOpenAI(temperature=0.2, model_name="gpt-3.5-turbo")
    vectorstore = load_vectorstore()
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(search_kwargs={"k": 4}),
        return_source_documents=True
    )
    return qa_chain

def ask_question(question):
    chain = build_rag_chain()
    result = chain({"query": question})
    return result["result"]