import sys
import os
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich.spinner import Spinner
from rich.live import Live

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data.create_sample_pdf import generate_sample_pdf
from src.config import SAMPLE_PDF_PATH, GROQ_API_KEY
from src.rag import initialize_vectorstore
from src.agent import build_study_assistant_agent
from langchain_core.messages import HumanMessage

console = Console()

def display_banner():
    """Renders clean ASCII / Rich Banner for terminal interface."""
    banner_text = """
    [bold cyan]🎓 AI LEARNING & STUDY ASSISTANT[/bold cyan]
    [italic dim]Powered by LangGraph, ChromaDB RAG, and Groq LLM[/italic dim]
    -----------------------------------------------------
    [yellow]Features:[yellow]
    • 📚 Textbook Question Answering (RAG)
    • 📅 Personalized Study Plan Generator
    • 📝 Dynamic Practice Quiz Generator
    • 🤖 Encouraging Educational AI Companion
    """
    console.print(Panel(banner_text, expand=False, border_style="cyan"))

def initialize_system():
    """Initializes sample textbook PDF, ChromaDB vector store, and LangGraph Agent."""
    with console.status("[bold green]Initializing system & indexing textbook materials into ChromaDB...[/bold green]", spinner="dots"):
        # Ensure sample PDF exists
        if not os.path.exists(SAMPLE_PDF_PATH):
            generate_sample_pdf(SAMPLE_PDF_PATH)
        
        # Initialize RAG vectorstore
        initialize_vectorstore()
        
        # Build Agent
        agent, config = build_study_assistant_agent(thread_id="terminal_user_session")
        
    console.print("[bold green]✓ System Initialized Successfully![/bold green]\n")
    return agent, config

def main():
    console.clear()
    display_banner()

    # Check API key warning
    if not GROQ_API_KEY or GROQ_API_KEY == "gsk_your_key_here":
        console.print("[bold red]⚠️  WARNING: GROQ_API_KEY is missing in your .env file![/bold red]")
        console.print("[yellow]Please open your `.env` file and set your valid Groq API Key.[/yellow]\n")

    try:
        agent, config = initialize_system()
    except Exception as e:
        console.print(f"[bold red]Initialization Error:[/bold red] {e}")
        return

    console.print("[dim]Type your question or request below. Type 'exit' or 'quit' to end session.[/dim]\n")

    while True:
        try:
            user_input = Prompt.ask("[bold cyan]Student[/bold cyan]")
            if not user_input.strip():
                continue

            if user_input.lower().strip() in ["exit", "quit", "q"]:
                console.print("\n[bold yellow]Keep up the great study habits! Goodbye! 👋[/bold yellow]")
                break

            console.print("\n[bold green]AI Assistant[/bold green]:")
            
            with console.status("[italic green]Thinking & retrieving context...[/italic green]", spinner="earth"):
                # Run query through LangGraph Agent
                inputs = {"messages": [HumanMessage(content=user_input)]}
                response = agent.invoke(inputs, config=config)
                
                # Get last message output
                last_msg = response["messages"][-1].content

            console.print(Panel(Markdown(last_msg), border_style="green", expand=False))
            console.print()

        except KeyboardInterrupt:
            console.print("\n[bold yellow]Session ended by user. Goodbye! 👋[/bold yellow]")
            break
        except Exception as e:
            console.print(f"\n[bold red]An error occurred:[/bold red] {str(e)}\n")

if __name__ == "__main__":
    main()
