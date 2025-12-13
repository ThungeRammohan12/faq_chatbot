from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from sentence_transformers import SentenceTransformer
import chromadb
import pandas as pd
import uuid

from .embeddings import generate_embeddings
from .chroma_client import collection

@csrf_exempt
def upload_excel(request):
    if request.method != "POST":
        return JsonResponse(
            {"error": "Only POST method allowed"},
            status=405
        )

    file = request.FILES.get("file")

    if not file:
        return JsonResponse(
            {"error": "Excel file is required"},
            status=400
        )

    try:
        # Read Excel
        df = pd.read_excel(file, engine="openpyxl")

        documents = []
        metadatas = []
        ids = []

        for index, row in df.iterrows():
            text = " | ".join(row.astype(str))
            documents.append(text)
            metadatas.append({
                "row_number": index,
                "source_file": file.name
            })
            ids.append(str(uuid.uuid4()))

        # Generate embeddings
        embeddings = generate_embeddings(documents)

        # Push to Chroma Cloud
        collection.add(
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )

        return JsonResponse({
            "message": "Excel data successfully pushed to Chroma Cloud",
            "rows_ingested": len(documents)
        })

    except Exception as e:
        return JsonResponse(
            {"error": str(e)},
            status=500
        )
