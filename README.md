🩺 Medical RAG QA System
Retrieval-Augmented Generation over Medical Transcription Reports
🚀 Overview

The Medical RAG QA System is a retrieval-augmented question-answering application built over a corpus of 5,000+ real-world medical transcription reports.
It generates evidence-grounded answers using retrieved context only — ensuring transparency and reducing hallucinations.

Technologies Used

MiniLM Sentence Embeddings

FAISS Similarity Search

Google Gemini 2.5 Flash

LangChain Community Components

Streamlit Web Interface

This project demonstrates how modern retrieval-enhanced LLMs can surface insights from domain-specific datasets in a safe, explainable, and responsible manner.

🧠 Key Features
🔹 Retrieval-Augmented Generation (RAG)

All answers are backed by retrieved evidence — not free-form hallucination.

🔹 High-Performance Embeddings

Uses sentence-transformers/all-MiniLM-L6-v2 for lightweight and accurate semantic embeddings.

🔹 FAISS Vector Indexing

Enables high-speed nearest-neighbor search over thousands of medical chunks.

🔹 Gemini-Powered Reasoning

Gemini 2.5 Flash provides grounded and structured responses.

🔹 Interactive Web App

User-friendly Streamlit UI with clear source attribution.

🔹 Transparent Evidence

Every answer includes its source chunks and metadata.

🔍 System Architecture
┌────────────────────────────────────────┐
│          Medical Documents (CSV)        │
└────────────────────────────────────────┘
                 │  Cleaning + Preprocessing
                 ▼
      ┌────────────────────────┐
      │  MiniLM Embeddings     │
      └────────────────────────┘
                 │
                 ▼
      ┌────────────────────────┐
      │      FAISS Index        │
      └────────────────────────┘
                 │
                 ▼  Top-k retrieved chunks
      ┌────────────────────────┐
      │      Gemini LLM        │
      └────────────────────────┘
                 │
                 ▼
      ┌────────────────────────────┐
      │   Evidence-Backed Answer    │
      └────────────────────────────┘

🌐 Live Demo

Streamlit App:
👉 https://medical-rag-app-systemgit-asvs2mfkqpo9vp6yuguptq.streamlit.app/

🛠️ How It Works (Deep Dive)
1. Document Preparation

Loaded 5,000+ medical reports

Cleaned and normalized text

Chunked using RecursiveCharacterTextSplitter

2. Embedding

MiniLM (all-MiniLM-L6-v2) generates 384-dimensional embeddings

Highly efficient for semantic similarity tasks

3. Vector Store

FAISS stores embeddings in a compressed, searchable index

Enables fast similarity search for every query

4. Retrieval Pipeline

For each user question:

Convert question → vector

Retrieve top-k similar chunks from FAISS

Build structured context block

Provide context + question to Gemini

Display grounded answer + exact sources

📊 Evaluation

The system was evaluated on 30 diverse medical queries, including:

Pneumonia

COPD

Myocardial infarction

Stroke

Sepsis

Postoperative complications

Renal failure

Discharge planning

And more…

Evaluation Metrics

Context retrieval accuracy

Groundedness

Source diversity

Safe refusal behavior

Findings

Retrieval quality is consistently high

The model avoids hallucination due to strict prompting

Answers are structured and transparent

Sources are always attached

Full evaluation results:

rag_eval_results.csv

🚨 Disclaimer

This system is intended only for:

Research

Education

Demonstration

This is NOT a medical device.
Do NOT use it for diagnosis, treatment, or clinical decisions of any kind.

👨‍💻 Technologies Used

Python 3

Streamlit

LangChain Community

Sentence Transformers

FAISS

Google Gemini 2.5 Flash

NumPy / Pandas

Kaggle Notebook Environment

📬 Contact

For discussions, feature suggestions, or collaborations, please create an issue in the repository.
