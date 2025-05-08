import streamlit as st
from llm.query_llm import run_query

st.set_page_config(page_title="ITC Financial Analysis AI", layout="centered")

st.title("ITC Financial Analysis with AI")
st.markdown("Ask questions about ITC’s financials (2023–2024), profitability, revenue trends and more.")

user_query = st.text_input("Enter your question :")

if st.button("Ask AI"):
    if user_query.strip():
        with st.spinner("Thinking..."):
            response = run_query(user_query)
            st.success("Answer:")
            st.write(response)
    else:
        st.warning("Please enter a question.")
