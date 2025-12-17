from sentence_transformers import SentenceTransformer
import pandas as pd
import faiss
import numpy as np
import pickle

# Load dataset
df = pd.read_csv("data/shl_individual_assessments.csv")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings
texts = df["description"].fillna("").tolist()
embeddings = model.encode(texts, show_progress_bar=True)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# Save index and metadata
faiss.write_index(index, "data/shl_faiss.index")
with open("data/metadata.pkl", "wb") as f:
    pickle.dump(df.to_dict("records"), f)
