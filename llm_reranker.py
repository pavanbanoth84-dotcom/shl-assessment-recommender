import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class LLMReranker:

    def rerank(self, query, assessments, top_n=10):
        prompt = f"""
You are an AI assistant helping recruiters choose the most relevant SHL assessments.

User Query:
{query}

Candidate Assessments:
{assessments}

Task:
- Select the most relevant assessments
- Ensure balance between technical and behavioral tests
- Return only assessment names and URLs
- Maximum {top_n} results
"""

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)

        return response.text
