import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

class SHLRetriever:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = faiss.read_index("data/shl_faiss.index")

        with open("data/metadata.pkl", "rb") as f:
            self.metadata = pickle.load(f)

    def search(self, query, top_k=20):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(
            np.array(query_embedding), top_k
        )

        results = []
        for idx in indices[0]:
            results.append(self.metadata[idx])

        return results
