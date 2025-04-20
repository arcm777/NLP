import streamlit as st
from llm.rag_chain import ask_question

st.title("Confluence QnA Chatbot 🤖")
query = st.text_input("Ask a question based on your Confluence docs:")

if st.button("Ask") and query:
    with st.spinner("Getting answer..."):
        response = ask_question(query)
        st.markdown(f"**Answer:** {response}")