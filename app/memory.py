
import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("memory")

def save_memory(text):
    collection.add(documents=[text], ids=[str(hash(text))])

def get_memory(query):
    results = collection.query(query_texts=[query], n_results=3)
    return results.get("documents", [])
