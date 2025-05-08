import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load the vectorstore
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = FAISS.load_local("itc_vectorstore", embedding_model, allow_dangerous_deserialization=True)

with open("API_key.txt", "r") as f:
    api_key = f.read().strip()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0)
qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())

def run_query(question):
    return qa.run(question)
