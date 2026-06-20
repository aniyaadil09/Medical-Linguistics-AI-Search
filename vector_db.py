# app/vector_db.py
import faiss
import pickle
from sentence_transformers import SentenceTransformer
import numpy as np

class VectorDB:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.metadata = []

    def add_vectors(self, texts, metadata):
        embeddings = self.model.encode(texts, convert_to_numpy=True, normalize_embeddings=True).astype('float32')
        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)
        self.metadata = metadata

    def save(self, index_file="vector.index", metadata_file="metadata.pkl"):
        faiss.write_index(self.index, index_file)
        with open(metadata_file, "wb") as f:
            pickle.dump(self.metadata, f)

    def load(self, index_file="vector.index", metadata_file="metadata.pkl"):
        self.index = faiss.read_index(index_file)
        with open(metadata_file, "rb") as f:
            self.metadata = pickle.load(f)

    def search(self, query_text, top_k=5):
        # Ensure input is a list for the model
        if isinstance(query_text, str):
            query_text = [query_text]
        query_vector = self.model.encode(query_text, convert_to_numpy=True, normalize_embeddings=True).astype('float32')
        distances, indices = self.index.search(query_vector, top_k)
        results = [self.metadata[i] for i in indices[0]]
        return results
