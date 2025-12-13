from sentence_transformers import SentenceTransformer

# Load once (important for performance)
model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embedding(text: str):
    """
    Converts input text into a vector embedding.
    """
    return model.encode([text]).tolist()[0]
