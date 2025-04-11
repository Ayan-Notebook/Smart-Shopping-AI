# recommender_agent.py (corrected structure)

from sklearn.metrics.pairwise import cosine_similarity
import pickle
import numpy as np
import os

class RecommenderAgent:
    def __init__(self, db_agent):
        self.db = db_agent
        self.product_embeddings = {}

        embedding_file = "embeddings/product_vectors.pkl"
        if os.path.exists(embedding_file):
            with open(embedding_file, "rb") as f:
                self.product_embeddings = pickle.load(f)
        else:
            print(f"⚠️ Warning: Embeddings file not found at '{embedding_file}'. Please run generate_product_vectors.py.")

    def recommend_products(self, customer_id):
        profile_vector = self.db.get_customer_vector(customer_id)
        if profile_vector is None or not self.product_embeddings:
            return []

        similarities = []
        for desc, item in self.product_embeddings.items():
            vec = item["embedding"]
            sim = cosine_similarity([profile_vector], [vec])[0][0]
            similarities.append((desc, sim, item))

        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities
