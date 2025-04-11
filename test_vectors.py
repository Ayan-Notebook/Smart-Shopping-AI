# test_vectors.py
import pickle

with open("D:\Hachathon\embeddings\product_vectors.pkl", "rb") as f:

    vectors = pickle.load(f)

print(f"✅ Loaded {len(vectors)} products")
sample = list(vectors.items())[0]
print("📦 Sample product:", sample[0])
print("🧠 Sample vector shape:", len(sample[1]['embedding']))
