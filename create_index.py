import json
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import os

class VectorDB:
    def __init__(self):
        # Small, lightweight model for low memory usage
        self.model = SentenceTransformer("paraphrase-MiniLM-L3-v2")  # tiny model (~384 dims)
        self.index = None
        self.metadata = []

    def embed_text(self, text):
        return self.model.encode(text, show_progress_bar=False)

    def add(self, texts, metadatas, batch_size=25):
        """Add vectors in small batches to avoid memory errors"""
        for i in range(0, len(texts), batch_size):
            batch_texts = texts[i:i+batch_size]
            batch_metadata = metadatas[i:i+batch_size]
            vectors = np.array([self.embed_text(t) for t in batch_texts], dtype='float32')

            if self.index is None:
                dim = vectors.shape[1]
                self.index = faiss.IndexFlatL2(dim)  # simple, memory-friendly index

            self.index.add(vectors)
            self.metadata.extend(batch_metadata)

    def save(self, index_file, metadata_file):
        faiss.write_index(self.index, index_file)
        with open(metadata_file, "wb") as f:
            pickle.dump(self.metadata, f)

def main():
    dataset_file = os.path.join("..", "data", "processed", "chapter1-22.json")
    if not os.path.exists(dataset_file):
        print(f"[ERROR] Dataset file not found: {dataset_file}")
        return

    with open(r"C:\Users\user1\Documents\LAB TASK 7\AI Theory\data\processed\chapter1-22.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    texts = [item.get("description", "") for item in data]
    metadatas = data

    vector_db = VectorDB()
    print("[INFO] Indexing records in small batches...")
    vector_db.add(texts, metadatas, batch_size=25)  # batch of 25 to save memory
    vector_db.save("vector.index", "metadata.pkl")
    print("[INFO] FAISS index and metadata saved successfully.")
    print(f"[INFO] Number of records indexed: {len(vector_db.metadata)}")

if __name__ == "__main__":
    main()
