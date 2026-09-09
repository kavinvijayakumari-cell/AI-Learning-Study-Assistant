from typing import TypedDict, Annotated, List, Optional
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver

class StudentState(TypedDict):
    """
    LangGraph State definition for tracking conversation history
    and student progress details across interactions.
    """
    messages: Annotated[List[BaseMessage], add_messages]
    student_name: str
    completed_topics: List[str]
    current_goal: str
    quiz_scores: List[str]

def create_memory_saver() -> MemorySaver:
    """Returns an in-memory checkpointer for session state persistence."""
    return MemorySaver()
