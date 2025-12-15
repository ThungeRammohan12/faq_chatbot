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
You are a RAG-based assistant.

Your task:
- The knowledge provided comes from a database.
- Use ONLY the given knowledge to answer.
- Rephrase the answer clearly based on the user's question.
- Do NOT add new information.
- If the knowledge does NOT contain an answer related to the question,
  respond exactly with: "Please enter a valid question"

Knowledge from database:
{context}

User Question:
{question}

Final Answer:
"""
    response = model.generate_content(prompt)
    return response.text.strip()

