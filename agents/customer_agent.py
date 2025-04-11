from sentence_transformers import SentenceTransformer
import numpy as np

class CustomerAgent:
    def __init__(self, db_agent):
        self.db_agent = db_agent
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")

    def process_customer_input(self, customer_id, query):
        # Convert the user query into a vector
        vector = self.embedder.encode(query)

        # Save the customer profile to the database
        self.db_agent.save_customer_profile(customer_id, query, vector)

        return vector
