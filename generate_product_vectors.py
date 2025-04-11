# generate_product_vectors.py (Updated for metadata)

import pandas as pd
import pickle
from sentence_transformers import SentenceTransformer
import os

df = pd.read_csv(r"D:\Hachathon\smart_shopping_project\Data\product_recommendation_data.csv")

# Composite product description
product_texts = (
    "Category: " + df["Category"].astype(str) +
    ", Subcategory: " + df["Subcategory"].astype(str) +
    ", Brand: " + df["Brand"].astype(str) +
    ", Price: $" + df["Price"].astype(str) +
    ", Rating: " + df["Product_Rating"].astype(str) +
    ", Sentiment Score: " + df["Customer_Review_Sentiment_Score"].astype(str)
).tolist()

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(product_texts)

# Combine vectors + metadata
product_vectors = {}
for i in range(len(product_texts)):
    product_vectors[product_texts[i]] = {
        "embedding": embeddings[i],
        "price": df["Price"].iloc[i],
        "brand": df["Brand"].iloc[i],
        "category": df["Category"].iloc[i],
        "rating": df["Product_Rating"].iloc[i],
        "sentiment": df["Customer_Review_Sentiment_Score"].iloc[i],
    }

# Save
os.makedirs("embeddings", exist_ok=True)
with open("embeddings/product_vectors.pkl", "wb") as f:
    pickle.dump(product_vectors, f)

print(f"✅ Saved {len(product_vectors)} vectors with metadata.")
