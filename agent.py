import os
from typing import List, Dict, Any
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

from src.config import GROQ_API_KEY, GROQ_MODEL, validate_config
from src.rag import rag_textbook_search
from src.tools import generate_study_plan, generate_quiz

SYSTEM_PROMPT = """You are an enthusiastic, highly encouraging, and empathetic AI Study & Learning Assistant. 
Your goal is to empower students, boost their confidence, and help them master educational subjects.

CORE RESPONSIBILITIES:
1. Answer student questions using facts retrieved from the textbook using `rag_textbook_search`.
2. Generate structured, actionable study plans using `generate_study_plan` when asked for study schedules, roadmaps, or timeframes.
3. Dynamically create interactive practice quizzes using `generate_quiz` when the student asks for practice questions, self-assessment, or testing on a topic.
4. Maintain a warm, supportive, and motivating tone (use positive affirmations like "Great question!", "You're making fantastic progress!", "Let me break that down simply for you!").

IMPORTANT INSTRUCTIONS:
- Whenever answering academic or textbook concepts (AI, Machine Learning, RAG, Neural Networks), ALWAYS use `rag_textbook_search` to verify facts from the textbook.
- ALWAYS include a dedicated **Source:** field at the end of your response specifying the exact PDF source name and page number provided by the search tool (e.g., `**Source:** sample_textbook.pdf (Page 1)`).
- Keep answers clear, structured, and easy to read using markdown bullet points and bold headers.
- If a student feels overwhelmed, offer words of encouragement and suggest breaking down their study goals into smaller 20-minute daily steps.
"""


def build_study_assistant_agent(thread_id: str = "session_1"):
    """
    Constructs and compiles the LangGraph ReAct Agent with state memory and tools.
    """
    validate_config()
    
    # Initialize Groq LLM (with max_tokens limit to prevent OTPM rate limit errors)
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name=GROQ_MODEL,
        temperature=0.3,
        max_tokens=600
    )


    # Register agent tools
    tools = [
        rag_textbook_search,
        generate_study_plan,
        generate_quiz
    ]

    # Initialize Memory Checkpointer
    checkpointer = MemorySaver()

    # Create LangGraph ReAct agent workflow
    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=SYSTEM_PROMPT,
        checkpointer=checkpointer
    )

    return agent, {"configurable": {"thread_id": thread_id}}
