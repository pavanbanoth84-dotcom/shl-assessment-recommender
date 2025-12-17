from fastapi import FastAPI
from pydantic import BaseModel
from retriever import SHLRetriever
from llm_reranker import LLMReranker

app = FastAPI(title="SHL Assessment Recommendation API")

retriever = SHLRetriever()
reranker = LLMReranker()

class RecommendRequest(BaseModel):
    query: str
    max_results: int = 10

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "SHL Recommendation API is running"
    }

@app.post("/recommend")
def recommend_assessments(request: RecommendRequest):
    retrieved = retriever.search(request.query, top_k=20)

    response = reranker.rerank(
        query=request.query,
        assessments=retrieved,
        top_n=request.max_results
    )

    return {
        "query": request.query,
        "recommendations": response
    }
  
