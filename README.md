# 🩺 Medical RAG QA System
### Retrieval-Augmented Generation over Medical Transcription Reports

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-RAG-1C3C3C?logo=langchain&logoColor=white)
![Gemini](https://img.shields.io/badge/AI-Gemini%202.5%20Flash-8E75B2?logo=google&logoColor=white)

## 🚀 Overview
The **Medical RAG QA System** is a retrieval-augmented question-answering application built over a corpus of **5,000+ real-world medical transcription reports**. 

Unlike standard LLMs which may hallucinate medical facts, this system generates evidence-grounded answers using **retrieved context only**—ensuring transparency, safety, and explainability.

### 🌐 [Click Here to Try the Live Demo](https://medical-rag-app-systemgit-asvs2mfkqpo9vp6yuguptq.streamlit.app/)

---

## 🧠 Key Features

*   **🔹 Retrieval-Augmented Generation (RAG):** All answers are strictly backed by retrieved evidence—no free-form hallucination.
*   **🔹 High-Performance Embeddings:** Utilizes `sentence-transformers/all-MiniLM-L6-v2` for lightweight, accurate semantic mapping.
*   **🔹 FAISS Vector Indexing:** Enables lightning-fast nearest-neighbor search over thousands of medical text chunks.
*   **🔹 Gemini-Powered Reasoning:** Leverages **Google Gemini 2.5 Flash** for grounded, structured, and clinically relevant responses.
*   **🔹 Transparent Evidence:** Every response cites specific source chunks and metadata used to generate the answer.
*   **🔹 Interactive UI:** A clean, user-friendly Streamlit interface.

---

## 🔍 System Architecture

The pipeline follows a standard RAG workflow optimized for medical text:

```mermaid
graph TD
    A[📂 Medical Documents CSV] -->|Cleaning + Preprocessing| B(📝 Text Chunking)
    B -->|MiniLM Encoding| C[🔢 Embeddings]
    C -->|Indexing| D[(🗂️ FAISS Vector Store)]
    
    E[👤 User Question] -->|Vectorize| F(🔎 Similarity Search)
    D --> F
    F -->|Top-k Retrieved Chunks| G[📄 Context Block]
    
    G -->|Context + Prompt| H[🤖 Google Gemini 2.5 Flash]
    H --> I[✅ Evidence-Backed Answer]

