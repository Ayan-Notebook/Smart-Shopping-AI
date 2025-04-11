# agents/db_agent.py
import sqlite3
import numpy as np
import os

class DBAgent:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id TEXT PRIMARY KEY,
                query TEXT,
                vector BLOB
            )
        """)
        self.conn.commit()

    def save_customer_profile(self, customer_id, query, vector):
        vec_blob = np.array(vector, dtype=np.float32).tobytes()
        self.conn.execute("""REPLACE INTO customers (id, query, vector)
                         VALUES (?, ?, ?)""", (customer_id, query, vec_blob))
        self.conn.commit()


    def get_customer_vector(self, customer_id):
        cursor = self.conn.execute("SELECT vector FROM customers WHERE id = ?", (customer_id,))
        result = cursor.fetchone()
        if result:
            return np.frombuffer(result[0], dtype=np.float32)
        return None
