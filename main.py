# smart_shopping_project/main.py
from agents.customer_agent import CustomerAgent
from agents.recommender_agent import RecommenderAgent
from agents.session_agent import SessionAgent
from agents.db_agent import DBAgent

# Initialize agents
db = DBAgent("database/memory.db")
session = SessionAgent()
customer_agent = CustomerAgent(db)
recommender_agent = RecommenderAgent(db)

# Simulated user interaction
customer_id = "C123"
user_query = "I need something trendy and affordable in electronics."

# Customer agent updates profile
profile = customer_agent.process_customer_input(customer_id, user_query)

# Recommender agent generates recommendations
recommendations = recommender_agent.recommend_products(customer_id)

# Display results
print("User Profile:", profile)
print("Recommendations:", recommendations)