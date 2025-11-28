🩺 Medical RAG QA System
Retrieval-Augmented Generation over Medical Transcription Reports
🚀 Overview

The Medical RAG QA System is a retrieval-augmented question-answering application designed to provide evidence-grounded responses from a collection of 5,000+ real-world medical transcription reports.

It combines powerful modern components:

MiniLM Sentence Embeddings

FAISS Similarity Search

Google Gemini 2.5 Flash

Streamlit Web Interface

LangChain Community Components

Together, these create a lightweight yet robust RAG pipeline that enables users to explore medical narratives in a controlled, transparent, and explainable manner.

This project is not intended to replace medical expertise—it is a demonstration of how retrieval-enhanced LLMs can support knowledge exploration responsibly.

🧠 Key Features
1. Retrieval-Augmented Generation (RAG)

Answers are grounded in retrieved evidence, reducing hallucinations.

2. High-Performance Embeddings

Uses sentence-transformers/all-MiniLM-L6-v2 for efficient 384-dimensional embeddings.

3. FAISS Vector Indexing

Provides fast similarity search across thousands of medical chunks.

4. Gemini-Powered Answers

Gemini 2.5 Flash generates explanations constrained by retrieved context.

5. Interactive Streamlit Web App

User-friendly interface with clean UX and live querying.

6. Transparent Source Attribution

Every answer cites the exact medical chunks used.

🔍 System Architecture
          ┌────────────────────────────────────────┐
          │          Medical Documents (CSV)        │
          └────────────────────────────────────────┘
                           │ Cleaning + Preprocessing
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
                           ▼  Top-k relevant chunks
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
https://medical-rag-app-systemgit-asvs2mfkqpo9vp6yuguptq.streamlit.app/

🛠️ How It Works (Deep Dive)
1. Document Preparation

Medical transcription reports loaded from dataset

Text cleaning and normalization

Chunking using RecursiveCharacterTextSplitter

2. Embeddings

MiniLM (all-MiniLM-L6-v2)

384-dimensional dense vectors

Optimized for semantic similarity tasks

3. Vector Store (FAISS)

Stores embeddings in an efficient index

Enables instant retrieval of nearest neighbors

4. RAG Retrieval Pipeline

For every user question:

Encode the query into an embedding

Retrieve top-k relevant chunks

Build a structured context block

Provide context + question to Gemini

Display model answer + exact sources

📊 Evaluation

The system was evaluated on 30 diverse medical questions, covering:

Pneumonia

COPD

Myocardial infarction

Stroke

Sepsis

Renal failure

Postoperative complications

Discharge instructions

And more...

Evaluation Metrics

Context retrieval accuracy

Grounded reasoning

Source diversity

Safe refusal on insufficient evidence

Key Findings

Strong retrieval performance

Minimal hallucination due to strict prompting

Clear, structured responses

Consistent attribution of sources

Full evaluation is available in:

rag_eval_results.csv

🚨 Disclaimer

This system is strictly for:

Educational use

Research

Demonstration

It is not a medical device.
Do not use it for diagnosis, treatment, or any real clinical decisions.

👨‍💻 Technologies Used

Python 3

Sentence Transformers

FAISS

LangChain Community

Google Gemini 2.5 Flash

Streamlit

Pandas / NumPy

Kaggle Notebook Environment

📬 Contact

For discussions, feature suggestions, or collaborations, please open an issue in the repository.
