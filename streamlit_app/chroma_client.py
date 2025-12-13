import chromadb
import streamlit as st

CHROMA_API_KEY = st.secrets["CHROMA_API_KEY"]
CHROMA_TENANT = st.secrets["CHROMA_TENANT"]
CHROMA_DATABASE = st.secrets["CHROMA_DATABASE"]

client = chromadb.CloudClient(
    api_key=CHROMA_API_KEY,
    tenant=CHROMA_TENANT,
    database=CHROMA_DATABASE
)

collection = client.get_or_create_collection(
    name="excel_documents"
)
