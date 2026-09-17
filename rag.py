import os

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

PDF_PATH = "que-ans.pdf"
INDEX_PATH = "faiss_index"

def get_embeddings():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


def create_vector():
    print("Loading PDF...")
    loader = PyPDFLoader(PDF_PATH)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=800,chunk_overlap=100)
    chunks = splitter.split_documents(documents)
    print(f"Loaded {len(documents)} pages")
    print(f"Created {len(chunks)} chunks")

    embeddings = get_embeddings()
    print("Creating FAISS index...")
    vectorstore = FAISS.from_documents(chunks,embeddings)

    vectorstore.save_local(INDEX_PATH)
    print("FAISS index saved!")

    return vectorstore


def load_vector():
    embeddings = get_embeddings()
    return FAISS.load_local(INDEX_PATH,embeddings,allow_dangerous_deserialization=True)


if __name__ == "__main__":
    if os.path.exists(INDEX_PATH):
        print("Loading existing FAISS index...")
        vectorstore = load_vector()

    else:
        vectorstore = create_vector()
    results = vectorstore.similarity_search("What is overfitting?",k=3)

    for result in results:
        print("\nRESULT")
        print(result.page_content)