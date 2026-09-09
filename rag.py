import os
from typing import List
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.tools import tool
from src.config import (
    CHROMA_DIR,
    SAMPLE_PDF_PATH,
    EMBEDDING_MODEL_NAME,
    COLLECTION_NAME
)

_vectorstore_instance = None

def get_embeddings():
    """Returns local HuggingFace embeddings instance."""
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

def initialize_vectorstore(pdf_path: str = SAMPLE_PDF_PATH) -> Chroma:
    """
    Loads PDF, splits into text chunks, embeds, and stores in ChromaDB.
    Returns the Chroma vectorstore instance.
    """
    global _vectorstore_instance
    embeddings = get_embeddings()

    # If Chroma collection directory exists and has files, load existing store
    if os.path.exists(CHROMA_DIR) and len(os.listdir(CHROMA_DIR)) > 0:
        _vectorstore_instance = Chroma(
            persist_directory=CHROMA_DIR,
            embedding_function=embeddings,
            collection_name=COLLECTION_NAME
        )
        return _vectorstore_instance

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"Textbook PDF not found at {pdf_path}. Please run data/create_sample_pdf.py first.")

    # Load and split PDF document
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = text_splitter.split_documents(documents)

    # Store in ChromaDB
    _vectorstore_instance = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR,
        collection_name=COLLECTION_NAME
    )
    return _vectorstore_instance

def get_vectorstore() -> Chroma:
    """Gets or initializes the active vectorstore."""
    global _vectorstore_instance
    if _vectorstore_instance is None:
        _vectorstore_instance = initialize_vectorstore()
    return _vectorstore_instance

@tool
def rag_textbook_search(query: str) -> str:
    """
    Search the educational textbook / study material database for relevant facts, definitions, and concepts.
    Use this tool whenever a student asks a question about AI, Machine Learning, Deep Learning, Supervised Learning, or RAG.

    Args:
        query: The search query string describing the concept or question.

    Returns:
        Relevant textbook excerpts retrieved from ChromaDB vector database.
    """
    try:
        vectorstore = get_vectorstore()
        results = vectorstore.similarity_search(query, k=3)
        if not results:
            return "No specific matching section found in the textbook materials."

        formatted_excerpts = []
        for idx, doc in enumerate(results, start=1):
            source_file = os.path.basename(doc.metadata.get("source", "sample_textbook.pdf"))
            page_num = doc.metadata.get("page", 0) + 1
            formatted_excerpts.append(
                f"[Excerpt {idx} | Source File: {source_file}, Page: {page_num}]:\n{doc.page_content.strip()}"
            )
        
        return "\n\n".join(formatted_excerpts)
    except Exception as e:
        return f"Error retrieving context from textbook vector database: {str(e)}"

