**Medical RAG QA System

Retrieval-Augmented Generation over Medical Transcription Reports**

🚀 Overview

The Medical RAG QA System is a retrieval-augmented question-answering application designed to provide evidence-grounded responses from a collection of 5,000+ real-world medical transcription reports.

The system uses:

MiniLM Sentence Embeddings

FAISS Similarity Search

Google Gemini 2.5 Flash

Streamlit (for a clean, interactive UI)

LangChain Community Components

Together, they form a lightweight yet powerful RAG pipeline that allows users to explore medical narratives in a controlled, safe, and explainable manner.

This project does not attempt to replace medical expertise — instead, it demonstrates how modern retrieval-enhanced LLMs can be paired with domain-specific datasets to surface relevant medical insights responsibly.

🧠 Key Features
1. Retrieval-Augmented Generation (RAG)

Queries are answered using only the retrieved evidence from the FAISS vector store, ensuring transparency and grounding.

2. High-Performance Embeddings

Uses sentence-transformers/all-MiniLM-L6-v2 to convert medical text into dense vectors.

3. FAISS Vector Indexing

FAISS enables fast, scalable similarity search across thousands of medical records.

4. Gemini-Powered Answers

Gemini 2.5 Flash is used for generation, with strict prompting to avoid hallucination.

5. Interactive Web App

Built with Streamlit and deployed via Streamlit Community Cloud.

6. Transparent Source Attribution

Every answer includes a list of source documents used for reasoning.

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
              ┌──────────────────────────┐
              │  Evidence-Backed Answer   │
              └──────────────────────────┘

🌐 Live Demo

Streamlit App: https://medical-rag-app-systemgit-asvs2mfkqpo9vp6yuguptq.streamlit.app/

🛠️ How It Works (Deep Dive)
1. Document Preparation

Extracted medical transcription reports

Cleaned text

Split using RecursiveCharacterTextSplitter for optimal chunk size

2. Embedding

MiniLM (all-MiniLM-L6-v2) encodes each chunk into a 384-dimensional vector.

3. Vector Store

FAISS stores vectors efficiently and supports high-speed nearest-neighbor search.

4. RAG Retrieval

For every user query:

Convert query to vector

Retrieve Top-k most relevant chunks

Format them into a context block

Feed to Gemini with a grounding-aware prompt

Display answer + source documents

📊 Evaluation

RAG system was evaluated over 30 diverse medical questions, covering:

Pneumonia

COPD

Myocardial infarction

Stroke

Sepsis

Renal failure

Discharge instructions

Postoperative complications

Evaluation metrics included:

Context retrieval success

Answer groundedness

Source diversity

Model refusal for insufficient evidence

Results show that the system:

Retrieves highly relevant chunks consistently

Avoids hallucinations due to strict context-only prompting

Returns professional, structured answers

The full evaluation is available in:

rag_eval_results.csv


🚨 Disclaimer

This system is strictly for educational, research, and demonstration use.
It is not a medical device.
It must not be used for diagnosis, treatment, or clinical decision-making.

👨‍💻 Technologies Used

Python 3

Streamlit

LangChain Community

Sentence Transformers

FAISS

Google Gemini 2.5 Flash

Pandas / NumPy

Kaggle Notebook Environment

📬 Contact

For discussions, collaborations, or academic use, feel free to create an issue in the repo.
