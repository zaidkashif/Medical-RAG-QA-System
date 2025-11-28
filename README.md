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

🛠️ Deep Dive: How It Works
1. Document Preparation
Loaded a dataset of 5,000+ medical transcription reports.
Performed data cleaning and text normalization.
Chunked documents using LangChain's RecursiveCharacterTextSplitter to maintain semantic context.
2. Embedding
Model: all-MiniLM-L6-v2.
Generates 384-dimensional dense vectors.
Selected for its high speed and performance in semantic similarity tasks.
3. Vector Store
FAISS (Facebook AI Similarity Search) creates a compressed, searchable index of the embeddings.
Allows for sub-millisecond retrieval of relevant medical contexts.
4. Retrieval Pipeline
When a user asks a question, it is converted into a vector.
FAISS retrieves the top-k most similar chunks.
A structured prompt is built containing the User Question and the Retrieved Context.
Gemini 2.5 Flash synthesizes the answer, citing sources explicitly.
👨‍💻 Technologies Used
Category	Technologies
Language	Python 3
Interface	Streamlit
Orchestration	LangChain Community
LLM	Google Gemini 2.5 Flash
Embeddings	Sentence Transformers (MiniLM)
Vector Store	FAISS
Data Proc	NumPy, Pandas
Environment	Kaggle Notebooks
📊 Evaluation
The system was rigorously evaluated on 30 diverse medical queries, covering topics such as:
Pneumonia & COPD
Myocardial Infarction & Stroke
Sepsis & Renal Failure
Postoperative Complications & Discharge Planning
Metrics Used:
Context Retrieval Accuracy (Did we find the right document?)
Groundedness (Is the answer supported by the text?)
Source Diversity
Safe Refusal Behavior (Does it refuse to answer out-of-scope questions?)
📄 Full Results: See rag_eval_results.csv in the repository.
⚙️ Local Installation
To run this project locally:
Clone the repository:
code
Bash
git clone https://github.com/your-username/medical-rag-system.git
cd medical-rag-system
Install dependencies:
code
Bash
pip install -r requirements.txt
Set up API Keys:
Create a .env file and add your Google Gemini API key:
code
Env
GOOGLE_API_KEY=your_api_key_here
Run the App:
code
Bash
streamlit run app.py
🚨 Disclaimer
[!WARNING]
This system is intended for Research, Education, and Demonstration purposes only.
This is NOT a medical device.
Do NOT use this system for diagnosis, treatment, or clinical decisions of any kind.
Always consult a qualified healthcare professional for medical advice.
📬 Contact
For discussions, feature suggestions, or collaborations, please open an issue in this repository.
