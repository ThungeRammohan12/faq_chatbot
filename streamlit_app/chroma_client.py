import os
from dotenv import load_dotenv
import chromadb

# Load environment variables
load_dotenv()

CHROMA_API_KEY = os.getenv("CHROMA_API_KEY")
CHROMA_TENANT = os.getenv("CHROMA_TENANT")
CHROMA_DATABASE = os.getenv("CHROMA_DATABASE")

if not CHROMA_API_KEY or not CHROMA_TENANT or not CHROMA_DATABASE:
    raise ValueError("Chroma Cloud environment variables are missing")

# Create Chroma Cloud client
client = chromadb.CloudClient(
    api_key=CHROMA_API_KEY,
    tenant=CHROMA_TENANT,
    database=CHROMA_DATABASE
)

# Collection MUST be at top-level
collection = client.get_or_create_collection(
    name="excel_documents"
)
