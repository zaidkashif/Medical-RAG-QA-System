import os
import textwrap

import streamlit as st
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from google import genai


# -----------------------------
# 1. CONFIG & CACHED LOADERS
# -----------------------------

@st.cache_resource(show_spinner="Loading embedding model...")
def load_embeddings():
    """
    Load the Sentence-Transformers MiniLM embedding model.
    Runs on CPU by default; set device to 'cuda' if your deployment has GPU.
    """
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
    )


@st.cache_resource(show_spinner="Loading FAISS index...")
def load_vectorstore(embeddings):
    """
    Load the pre-built FAISS index from local directory.
    Make sure 'faiss_medical_index' is present next to app.py.
    """
    faiss_dir = "faiss_medical_index"
    vectorstore = FAISS.load_local(
        faiss_dir,
        embeddings=embeddings,
        allow_dangerous_deserialization=True,
    )
    return vectorstore


@st.cache_resource(show_spinner="Connecting to Gemini...")
def load_genai_client():
    """
    Initialize the Google GenAI client.

    Priority of API key:
    1. Streamlit secrets: st.secrets["GEMINI_API_KEY"]
    2. Environment variable: GEMINI_API_KEY or GOOGLE_API_KEY
    """
    api_key = None

    # Try Streamlit secrets first
    if "GEMINI_API_KEY" in st.secrets:
        api_key = st.secrets["GEMINI_API_KEY"]
    elif "GOOGLE_API_KEY" in st.secrets:
        api_key = st.secrets["GOOGLE_API_KEY"]

    # Fallback to environment variables
    if api_key is None:
        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise RuntimeError(
            "No Gemini API key found. "
            "Set GEMINI_API_KEY/GOOGLE_API_KEY in environment or Streamlit secrets."
        )

    client = genai.Client(api_key=api_key)
    return client


# -----------------------------
# 2. RAG ANSWER FUNCTION
# -----------------------------

def rag_answer(query: str, vectorstore, client, k: int = 4, model_name: str = "gemini-2.5-flash", temperature: float = 0.2):
    """
    End-to-end RAG step:
      1. Retrieve top-k similar chunks from FAISS.
      2. Build a context string.
      3. Ask Gemini to answer using ONLY that context.
      4. Return answer text + list of source docs.
    """
    # 1) Retrieve from FAISS
    docs = vectorstore.similarity_search(query, k=k)

    if not docs:
        return "No relevant documents found in the index.", []

    # 2) Build context
    context_blocks = []
    for i, d in enumerate(docs, start=1):
        block = f"[Source {i} | row_id={d.metadata.get('row_id')} | specialty={d.metadata.get('medical_specialty')}]\n{d.page_content}"
        context_blocks.append(block)

    context = "\n\n-----\n\n".join(context_blocks)

    # 3) Build prompt
    prompt = f"""
You are a cautious, evidence-based medical assistant.
Use ONLY the information given in the context below to answer the user's question.
If the answer is not clearly supported by the context, say:
"The dataset does not provide enough information to answer this safely."

Be concise, structured, and avoid hallucinating facts.

Context:
{context}

Question:
{query}

Answer:
""".strip()

    # 4) Call Gemini
    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
        config={"temperature": temperature},
    )

    answer_text = getattr(response, "text", "").strip()
    if not answer_text:
        answer_text = "No answer text returned by the model."

    return answer_text, docs


# -----------------------------
# 3. STREAMLIT UI
# -----------------------------

def main():
    st.set_page_config(
        page_title="Medical RAG QA System",
        page_icon="🩺",
        layout="wide",
    )

    st.title("🩺 Medical RAG QA System")
    st.caption(
        "Retrieval-Augmented Generation over medical transcription reports "
        "using MiniLM + FAISS + Gemini."
    )

    # Disclaimer
    st.markdown(
        """<div style="background-color:#fff3cd;padding:10px;border-radius:6px;border:1px solid #ffeeba;">
        <strong>Disclaimer:</strong> This application is for educational and demonstration purposes only.
        It is <strong>not</strong> a substitute for professional medical advice, diagnosis, or treatment.
        Do not use this system to make real clinical decisions.
        </div>""",
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # Sidebar controls
    st.sidebar.header("Settings")

    top_k = st.sidebar.slider("Top-k context chunks", min_value=1, max_value=8, value=4, step=1)
    temperature = st.sidebar.slider("LLM temperature", min_value=0.0, max_value=1.0, value=0.2, step=0.05)
    model_name = st.sidebar.text_input("Gemini model name", value="gemini-2.5-flash")

    st.sidebar.markdown("-----")
    st.sidebar.markdown("**API Key** must be set as `GEMINI_API_KEY` / `GOOGLE_API_KEY` in environment or Streamlit secrets.")

    # Load heavy stuff once
    try:
        embeddings = load_embeddings()
        vectorstore = load_vectorstore(embeddings)
        client = load_genai_client()
    except Exception as e:
        st.error(f"Initialization error: {e}")
        st.stop()

    # Main input
    st.subheader("Ask a medical question about the dataset")

    default_question = "What symptoms are commonly associated with pneumonia in these reports?"
    user_query = st.text_area("Your question:", value=default_question, height=100)

    if st.button("Get Answer", type="primary"):
        if not user_query.strip():
            st.warning("Please enter a question.")
            st.stop()

        with st.spinner("Retrieving context and querying Gemini..."):
            answer, docs = rag_answer(
                query=user_query.strip(),
                vectorstore=vectorstore,
                client=client,
                k=top_k,
                model_name=model_name.strip(),
                temperature=temperature,
            )

        st.markdown("### 🧾 Answer")
        st.write(answer)

        st.markdown("### 📚 Retrieved Sources")
        if not docs:
            st.info("No sources retrieved.")
        else:
            for i, d in enumerate(docs, start=1):
                with st.expander(f"Source {i} | row_id={d.metadata.get('row_id')} | {d.metadata.get('medical_specialty')}"):
                    st.write("**Sample name:**", d.metadata.get("sample_name"))
                    st.write("**Description:**", d.metadata.get("description"))
                    st.markdown("---")
                    snippet = d.page_content
                    st.text(snippet)


if __name__ == "__main__":
    main()
