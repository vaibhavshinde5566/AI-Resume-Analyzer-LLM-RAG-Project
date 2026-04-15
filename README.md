# 🤖 AI Resume Analyzer (LLM + RAG)

## 🚀 Overview

AI Resume Analyzer is an intelligent application that analyzes resumes using Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG).
It allows users to upload their resume and interact with it through natural language queries.

---

## ✨ Features

* 📄 Upload Resume (PDF)
* 🤖 AI-based Question Answering
* 🔍 Semantic Search using Vector Embeddings
* 💡 Resume Insights & Suggestions
* 🎯 Skill Extraction
* 🧠 Context-aware responses using RAG

---

## 🧠 How It Works

1. Resume PDF is loaded and parsed
2. Text is split into smaller chunks
3. Embeddings are created for each chunk
4. Stored in Vector Database (FAISS)
5. User query → relevant chunks retrieved
6. LLM generates intelligent response

---

## 🛠️ Tech Stack

* Python
* LangChain
* Groq API (LLM - LLaMA 3)
* FAISS (Vector Database)
* Streamlit (UI)

---

## 📂 Project Structure

```
AI Resume Analyzer/
│
├── app.py
├── app_ui.py
├── pdf_loader.py
├── vector_store.py
├── rag_pipeline.py
├── llm.py
├── requirements.txt
└── README.md
```
