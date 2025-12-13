import chromadb

client = chromadb.CloudClient(
    api_key="ck-6UALWqytpjaiAG7KW4o2dhagVTQgH7VvEhtKGscjqkc8",
    tenant="5dcdb837-1e31-4764-a4c1-5cf27b6ecef7",
    database="rag_model"
)

collection = client.get_or_create_collection(
    name="excel_documents"
)
