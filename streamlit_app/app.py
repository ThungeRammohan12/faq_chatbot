import streamlit as st
from chroma_client import collection
from embeddings import generate_embedding
from llm import rephrase_answer



st.set_page_config(page_title="RAG Assistant", layout="centered")

st.title("📄 RAG Chatbot (Gemini Flash)")

query = st.text_input("Ask a question from uploaded documents")

if st.button("Search") and query.strip():
    with st.spinner("Searching knowledge base..."):

        # 1️⃣ Create embedding for query
        query_embedding = generate_embedding(query)

        # 2️⃣ Search Chroma Cloud
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=3
        )

        documents = results.get("documents", [[]])[0]

        if not documents:
            st.warning("No relevant data found.")
        else:
            # 3️⃣ Combine retrieved chunks
            context = "\n\n".join(documents)

            # 4️⃣ Gemini Flash rephrasing
            answer = rephrase_answer(context, query)

            st.subheader("Answer")
            st.write(answer)
