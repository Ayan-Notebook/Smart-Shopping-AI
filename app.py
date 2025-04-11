# app.py

import streamlit as st
from agents.customer_agent import CustomerAgent
from agents.recommender_agent import RecommenderAgent
from agents.db_agent import DBAgent

# Initialize agents
db_agent = DBAgent("database/memory.db")
customer_agent = CustomerAgent(db_agent)
recommender_agent = RecommenderAgent(db_agent)

# Streamlit page config
st.set_page_config(page_title="Smart Shopping", layout="centered")
st.title("🛍️ Smart Shopping – Personalized Product Recommender")

# User inputs
user_id = st.text_input("Enter Customer ID", value="C001")
query = st.text_area("What are you looking for today?", height=100)

# Initialize results
results = []

if st.button("🔍 Get Recommendations"):
    if query.strip():
        customer_agent.process_customer_input(user_id, query)
        results = recommender_agent.recommend_products(user_id)
        st.session_state["results"] = results  # optional persistence
    else:
        st.warning("Please enter a valid shopping query.")

# ⬇️ This part runs after button click
if results:
    st.subheader("Recommendations")
    for i, (desc, score, meta) in enumerate(results, 1):
        st.markdown(f"**{i}.** {meta['brand']} | ${meta['price']} | Score: `{score:.3f}`")
else:
    if query.strip():
        st.warning("No recommendations found.")

