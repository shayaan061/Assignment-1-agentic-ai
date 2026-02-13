1️⃣ Project Overview

The DBMS FAQ Chatbot is a Retrieval-Augmented Generation (RAG) based system designed to answer frequently asked questions related to Database Management Systems (DBMS).

The system retrieves relevant information from a structured DBMS FAQ dataset using semantic similarity search and generates context-aware answers using a local open-source language model.

This project demonstrates the implementation of a complete RAG pipeline including:

Text preprocessing and chunking

Embedding generation

Vector storage and similarity search

Context-aware answer generation

The chatbot runs entirely on local resources using free AI models without relying on paid APIs.

2️⃣ Tools & Libraries Used
Programming Language

Python 3.11

Libraries & Frameworks

LangChain (Community Modules)
Used for document loading, text splitting, and vector store integration.

Sentence Transformers
Model used: all-MiniLM-L6-v2
Generates semantic embeddings for text chunks.

FAISS (Facebook AI Similarity Search)
Used as the vector database for efficient similarity search.

Transformers (Hugging Face)
Model used: google/flan-t5-base
Used for answer generation.

Torch
Backend framework required for running transformer models.

VS Code
Used as the development environment.

3️⃣ Instructions to Run the Notebook / Project
Step 1: Create a Virtual Environment
python3.11 -m venv venv
source venv/bin/activate

Step 2: Install Required Libraries
pip install langchain langchain-community langchain-huggingface faiss-cpu sentence-transformers transformers torch

Step 3: Ensure Dataset File Exists

Make sure the file:

dbms_faq.txt


is present in the project directory.

Step 4: Run the Application
python main.py


The chatbot will start in the terminal.
Type a question and press Enter.
Type exit to quit.# Assignment-1-agentic-ai
