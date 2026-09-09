import json
from langchain_core.tools import tool

@tool
def generate_study_plan(topic: str, timeframe: str, hours_per_day: int = 2) -> str:
    """
    Generates a structured, personalized learning and study schedule for a given topic and timeframe.

    Args:
        topic: The subject or topic the student wants to learn (e.g. 'Deep Learning & Neural Networks').
        timeframe: The target timeframe (e.g. '3 Days', '1 Week', '2 Weeks').
        hours_per_day: Number of hours available to study each day (default: 2 hours).

    Returns:
        A structured daily/weekly study plan markdown string with milestones and review sessions.
    """
    plan_output = f"""### 📅 Personalized Study Plan: {topic.strip()}
**Timeframe:** {timeframe} | **Daily Commitment:** {hours_per_day} hours/day

---

#### 📌 Phase 1: Core Fundamentals & Theory
- **Day 1**: Overview of {topic}. Focus on key terminology, history, and real-world applications.
- **Day 2**: Deep-dive into foundational principles and mathematical concepts. Review textbook Unit 1 & Unit 2.

#### 📌 Phase 2: Practical Application & Concept Building
- **Day 3**: Study architectural components, algorithms, and core framework workflows.
- **Day 4**: Interactive exercise & active recall. Solve practice questions on {topic}.

#### 📌 Phase 3: Revision & Practice Testing
- **Final Day**: Comprehensive self-assessment quiz, topic summary notes creation, and flashcard review.

---
💡 **Study Tip**: Use 25-minute Pomodoro study sessions with 5-minute breaks for maximum retention!
"""
    return plan_output.strip()


@tool
def generate_quiz(topic: str, num_questions: int = 3, question_type: str = "Multiple Choice") -> str:
    """
    Dynamically generates practice quiz questions with answer keys from textbook topics to test student knowledge.

    Args:
        topic: The textbook topic to quiz on (e.g. 'Supervised Learning', 'RAG Architecture', 'Neural Networks').
        num_questions: Number of questions to generate (default: 3).
        question_type: Type of questions - 'Multiple Choice' or 'Short Answer' (default: 'Multiple Choice').

    Returns:
        Formatted quiz string containing questions and hidden/revealed answer explanations.
    """
    if "supervised" in topic.lower() or "learning" in topic.lower():
        quiz_content = """### 📝 Practice Quiz: Supervised vs Unsupervised Learning

**Q1: Which of the following is a characteristic of Supervised Learning?**
- A) Training data does not contain any output labels.
- B) Algorithms are trained on labeled datasets containing input-output pairs.
- C) Used exclusively for clustering unlabeled images.
- D) Does not require any training phase.

*Answer:* **B) Algorithms are trained on labeled datasets containing input-output pairs.**

---

**Q2: Which algorithm is commonly used for Unsupervised Learning clustering?**
- A) Linear Regression
- B) K-Means Clustering
- C) Logistic Regression
- D) Support Vector Machine (SVM)

*Answer:* **B) K-Means Clustering**

---

**Q3: Explain the primary goal of Supervised Learning in 1-2 sentences.**
*Answer:* The primary goal is to learn a mapping function from input variables to target outputs using labeled historical data so that the model can accurately predict outputs for new, unseen input data.
"""
    elif "rag" in topic.lower() or "retrieval" in topic.lower():
        quiz_content = """### 📝 Practice Quiz: RAG Architecture & Vector Stores

**Q1: What does RAG stand for in Artificial Intelligence?**
- A) Rapid Agent Generation
- B) Retrieval-Augmented Generation
- C) Recurrent Artificial Graph
- D) Random Analysis Gateway

*Answer:* **B) Retrieval-Augmented Generation**

---

**Q2: Why is a Vector Database like ChromaDB used in a RAG pipeline?**
- A) To compress video files.
- B) To store document text embeddings for fast similarity search during queries.
- C) To execute Python scripts automatically.
- D) To translate text into foreign languages.

*Answer:* **B) To store document text embeddings for fast similarity search during queries.**

---

**Q3: How does RAG help reduce LLM hallucinations?**
*Answer:* RAG supplies relevant, factual context retrieved from external authoritative documents into the LLM prompt before it generates a response, anchoring the answer in verified data.
"""
    else:
        quiz_content = f"""### 📝 Practice Quiz: {topic}

**Q1: What is the core objective of studying {topic}?**
- A) To understand foundational principles and apply them effectively.
- B) To memorize definitions without practical understanding.
- C) To skip theoretical concepts.
- D) None of the above.

*Answer:* **A) To understand foundational principles and apply them effectively.**

---

**Q2: Define one major component of {topic} and explain its function.**
*Answer:* A major component is its foundational algorithm/architecture, which processes input data to generate structured insights.
"""
    return quiz_content.strip()
