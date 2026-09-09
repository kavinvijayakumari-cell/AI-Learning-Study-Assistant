import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Groq API Settings
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")


# RAG & Chroma Vector Database Configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
CHROMA_DIR = os.path.join(BASE_DIR, "chroma_db")
SAMPLE_PDF_PATH = os.path.join(DATA_DIR, "sample_textbook.pdf")

EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
COLLECTION_NAME = "study_assistant_textbook"

def validate_config():
    """Validates essential runtime configuration."""
    if not GROQ_API_KEY or GROQ_API_KEY == "gsk_your_key_here":
        print("[WARNING] GROQ_API_KEY is not set or using placeholder. Please set your actual API key in .env")
