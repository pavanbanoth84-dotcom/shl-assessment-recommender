# SHL Assessment Recommendation System

This project implements a GenAI-powered SHL Assessment Recommendation System using a Retrieval-Augmented Generation (RAG) approach.

## Features
- Scrapes SHL Individual Test Solutions from the official catalog
- Uses semantic embeddings and FAISS for retrieval
- Applies LLM-based re-ranking for better relevance
- Balances technical and behavioral assessments
- Exposes recommendations via FastAPI
- Provides a Streamlit web interface
- Evaluated using Mean Recall@10

## Tech Stack
- Python
- SentenceTransformers
- FAISS
- Gemini LLM
- FastAPI
- Streamlit

## Project Structure
- data/ : scraped SHL dataset
- evaluation/ : evaluation scripts
- api.py : backend API
- app.py : frontend web app

## How to Run
Refer to the source code for setup and deployment steps.
