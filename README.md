# 🎓 AI Learning & Study Assistant

An intelligent, encouraging study companion for students built with **LangGraph**, **LangChain**, **Groq API** (`llama-3.3-70b-versatile`), and **ChromaDB Vector Store (RAG)**.

Developed as part of the **IBM Internship / Naan Mudhalvan 5-Day LangChain & Agent Workflow Training Session**.

---

## 🌟 Key Features

1. **📚 Textbook RAG (Retrieval-Augmented Generation)**:
   - Loads educational textbook materials (`.pdf`).
   - Splits text into optimal chunks and embeds them locally using `sentence-transformers/all-MiniLM-L6-v2`.
   - Stores vectors in **ChromaDB** for fast, precise similarity search when answering factual academic queries.
   - Automatically appends a dedicated `📌 Source: <pdf_name> (Page X)` field to factual answers.

2. **🛠️ Custom Agent Tools**:
   - **`generate_study_plan`**: Creates structured, daily/weekly personalized study plans based on topic, timeframe, and study hours.
   - **`generate_quiz`**: Dynamically generates practice quizzes (Multiple Choice Questions and Short Answer) with answer keys directly from textbook subjects.
   - **`rag_textbook_search`**: Automatically queries ChromaDB vector store for textbook references.

3. **🧠 State Management & Memory (LangGraph)**:
   - Powered by **LangGraph State Graph** and `MemorySaver`.
   - Remembers student chat history, completed topics, and quiz interactions across multi-turn conversations.

4. **✨ Empathetic & Educational Persona**:
   - System prompt tuned to deliver encouraging, positive, and structured educational guidance.

5. **💻 Terminal Interactive CLI Interface**:
   - Styled with `rich` library (colorized panels, spinners, and markdown formatting). Ideal for capturing clean terminal screenshots for submission reports.

---

## 📁 Repository Structure

```
AI-Learning-Study-Assistant/
├── .env.example                # Environment variables template
├── .env                        # Local environment configuration (Groq API Key)
├── .gitignore                  # Git ignore specifications (ignores secrets & local cache)
├── requirements.txt            # Package dependencies
├── data/
│   ├── create_sample_pdf.py    # Script to generate sample textbook PDF
│   └── sample_textbook.pdf     # Sample AI/ML Textbook PDF for RAG
├── src/
│   ├── __init__.py
│   ├── config.py               # API & path configurations
│   ├── rag.py                  # PyPDF loader, ChromaDB indexer, RAG retriever tool
│   ├── tools.py                # Study Plan & Quiz Generator tools
│   ├── memory.py               # LangGraph state schema & memory checkpointer
│   └── agent.py                # LangGraph ReAct agent initialization & system prompt
├── main.py                     # Interactive Terminal CLI Application
└── README.md                   # Complete project documentation
```

---

## 🚀 How to Clone & Run This Project (Step-by-Step Guide)

Follow these step-by-step instructions to clone, setup, and run the project locally on your machine.

### Step 1: Clone the Repository
Open your terminal/command prompt and run:
```bash
git clone https://github.com/vishal-ai-user/AI-Learning_and_Study_Assistant.git
cd AI-Learning_and_Study_Assistant
```


### Step 2: Create & Activate Virtual Environment
Using `uv` (Recommended):
```bash
# Create virtual environment
uv venv .venv

# Activate virtual environment
# Windows (CMD):
.venv\Scripts\activate
# Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
# Linux / macOS:
source .venv/bin/activate
```

*(Alternative using standard python `venv`)*:
```bash
python -m venv .venv
.venv\Scripts\activate
```

### Step 3: Install Required Dependencies
```bash
# Using uv (Fast):
uv pip install -r requirements.txt

# Or using standard pip:
pip install -r requirements.txt
```

### Step 4: Configure Groq API Key
1. Get a free API Key from [Groq Console](https://console.groq.com/keys).
2. Copy `.env.example` to create a `.env` file:
   ```bash
   cp .env.example .env
   ```
3. Open `.env` and paste your key:
   ```env
   GROQ_API_KEY=gsk_your_actual_groq_api_key_here
   GROQ_MODEL=qwen/qwen3.8-27b
   ```

### Step 5: Launch the Interactive Assistant
On Windows (CMD / PowerShell):
```cmd
.venv\Scripts\python.exe main.py
```

Or if your virtual environment is activated:
```bash
python main.py
```


---

## 🧪 Sample Prompts for Testing & Screenshots

1. **Textbook Q&A (RAG Search with Source Citation)**:
   > **Prompt**: `What is Retrieval-Augmented Generation (RAG) and why is ChromaDB used?`
   > **Output**: Detailed answer retrieved from `sample_textbook.pdf` with `📌 Source: sample_textbook.pdf (Page 1)`.

2. **Personalized Study Schedule Generator**:
   > **Prompt**: `Create a 3-day study plan for Deep Learning and Neural Networks.`
   > **Output**: Structured daily study roadmap with Pomodoro learning tips.

3. **Dynamic Practice Quiz Generator**:
   > **Prompt**: `Give me a practice quiz on Supervised Learning.`
   > **Output**: Multiple-Choice Questions (MCQs) and Short Answer questions with answer explanations.

---

## 📜 Submission Details
- **Project Name**: AI Learning & Study Assistant
- **Program**: IBM Internship / Naan Mudhalvan 5-Day Training Session
- **Tech Stack**: Python, LangChain, LangGraph, Groq API, ChromaDB Vector Store, Rich CLI
"# AI-Learning-and-Study-Assistant" 
