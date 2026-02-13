from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline

# Load Data
loader = TextLoader("dbms_faq.txt")
documents = loader.load()

#  Chunking
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)

#  Create Embeddings
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

#  Store in FAISS
vectorstore = FAISS.from_documents(docs, embedding)

# Load Generator Model
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=256
)

print("DBMS FAQ Chatbot (Type 'exit' to quit)\n")

# Chat Loop (Manual RAG)
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break

    # Retrieve relevant documents
    results = vectorstore.similarity_search(query, k=2)

    context = "\n".join([doc.page_content for doc in results])

    prompt = f"""
    Use the following context to answer the question.

    Context:
    {context}

    Question:
    {query}

    Answer:
    """

    response = generator(prompt)[0]['generated_text']

    print("Bot:", response)
    print()
