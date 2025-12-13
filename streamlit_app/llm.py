import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash-lite")

def rephrase_answer(context, question):
    prompt = f"""
You are a helpful assistant.

Answer the question ONLY using the context below.
If the answer is not present in the context, say "I don't know".

Context:
{context}

Question:
{question}
"""

    response = model.generate_content(prompt)
    return response.text
