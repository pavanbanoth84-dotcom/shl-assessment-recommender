import streamlit as st
import requests

st.set_page_config(page_title="SHL Assessment Recommender", layout="centered")

st.title("SHL Assessment Recommendation System")
st.write("Enter a job description or hiring requirement to get relevant SHL assessments.")

API_URL = "https://YOUR_API_URL/recommend"

query = st.text_area("Job Description / Query", height=150)

max_results = st.slider("Number of recommendations", 5, 10, 5)

if st.button("Get Recommendations"):
    if not query.strip():
        st.warning("Please enter a query.")
    else:
        payload = {
            "query": query,
            "max_results": max_results
        }

        with st.spinner("Finding best assessments..."):
            response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            data = response.json()
            st.subheader("Recommended Assessments")
            st.write(data["recommendations"])
        else:
            st.error("Error fetching recommendations. Please try again.")
          
