# ITC-financial-ai-analysis

# 📊 ITC Financial Analysis with AI Scraping & LLM Integration

This project automates the extraction and analysis of ITC Ltd.'s financial performance using AI search, PDF parsing, and LLM-powered question answering.

---

## 🎯 Objective

To analyze ITC’s revenue trends, profitability, and financial health by:
- Scraping ITC’s Annual Reports and Investor Presentations using Tavily AI
- Processing financial documents into vector embeddings
- Using a Language Model (LLM) to answer finance-specific questions
- Presenting responses with document-based citations

---

## ✅ Features

- 🔍 AI-powered search (Tavily) for ITC’s official reports
- 📄 PDF text extraction and preprocessing
- 🧠 Google Gemini integration via LangChain for Q&A
- 🔎 FAISS vector store for fast document retrieval
- 💬 Streamlit app for interactive user queries (optional)

---

## 📁 Project Structure

itc-financial-analysis/
├── tavily_search/ # Tavily search and results processing
├── pdf_loader/ # Load and split ITC PDF reports
├── vectorstore/ # FAISS-based embedding storage
├── llm_chain/ # Google Gemini + LangChain pipeline
├── app.py # Streamlit-based question-answering interface
├── requirements.txt # Python dependencies
└── README.md # Project documentation

