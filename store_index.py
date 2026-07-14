from dotenv import load_dotenv
import os

from src.helper import (
    load_pdf_file,
    text_split,
    download_hugging_face_embeddings,
)

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from langchain_qdrant import QdrantVectorStore

# Load Environment Variables

load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

if not QDRANT_URL:
    raise ValueError("QDRANT_URL not found in .env")

if not QDRANT_API_KEY:
    raise ValueError("QDRANT_API_KEY not found in .env")

print("Qdrant URL:", QDRANT_URL)
print("Connecting to Qdrant...")

# Connect to Qdrant

client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
    check_compatibility=False,
)

collection_name = "MedicBot"

# Create Collection (if not exists)

try:
    collections = [
        collection.name
        for collection in client.get_collections().collections
    ]

    if collection_name not in collections:
        print("Creating Collection...")

        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE,
            ),
        )

        print("Collection Created Successfully!")

    else:
        print("Collection Already Exists!")

except Exception as e:
    print("Error while connecting to Qdrant")
    print(e)
    exit()

# Load Documents

print("Loading PDF files...")

documents = load_pdf_file(data="Data/")

print("Splitting Documents...")

text_chunks = text_split(documents)

print(f"Total Chunks : {len(text_chunks)}")

# Load Embeddings

print("Loading Embedding Model...")

embeddings = download_hugging_face_embeddings()

print("Embedding Model Loaded!")

# Upload to Qdrant

print("Uploading Embeddings...")

docsearch = QdrantVectorStore.from_documents(
    documents=text_chunks,
    embedding=embeddings,
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
    collection_name=collection_name,
    prefer_grpc=False,
)

print("MedicBot Vector Database Created Successfully!")
