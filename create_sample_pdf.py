import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_sample_pdf(output_path="data/sample_textbook.pdf"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontSize=20,
        leading=24,
        spaceAfter=12
    )

    heading_style = ParagraphStyle(
        'DocHeading',
        parent=styles['Heading2'],
        fontSize=14,
        leading=18,
        spaceBefore=10,
        spaceAfter=6
    )

    body_style = ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        spaceAfter=8
    )

    content = []
    content.append(Paragraph("Fundamentals of Artificial Intelligence & Machine Learning", title_style))
    content.append(Paragraph("Unit 1: Introduction to Artificial Intelligence", heading_style))
    content.append(Paragraph(
        "Artificial Intelligence (AI) is the simulation of human intelligence processes by machines, especially computer systems. "
        "These processes include learning (the acquisition of information and rules for using the information), reasoning "
        "(using rules to reach approximate or definite conclusions), and self-correction. AI applications include advanced web search engines, "
        "recommendation systems, understanding human speech, autonomous vehicles, and generative AI.",
        body_style
    ))

    content.append(Paragraph("Unit 2: Supervised vs Unsupervised Learning", heading_style))
    content.append(Paragraph(
        "Machine Learning (ML) is a subset of AI focused on building applications that learn from data and improve accuracy over time without being explicitly programmed. "
        "Supervised learning algorithms are trained using labeled datasets where the input data is paired with the correct output label. Examples include Linear Regression, Logistic Regression, Decision Trees, and Support Vector Machines (SVM). "
        "Unsupervised learning deals with unlabeled data where the algorithm attempts to discover underlying patterns, groupings, or structures. Examples include K-Means Clustering and Principal Component Analysis (PCA).",
        body_style
    ))

    content.append(Paragraph("Unit 3: Deep Learning and Neural Networks", heading_style))
    content.append(Paragraph(
        "Deep Learning is a specialized subfield of machine learning based on Artificial Neural Networks (ANNs) with multiple layers (hence 'deep'). "
        "A neural network consists of an input layer, hidden layers, and an output layer. Nodes or artificial neurons transmit signals between layers. "
        "Convolutional Neural Networks (CNNs) are predominantly used for computer vision and image processing tasks, while Recurrent Neural Networks (RNNs) and Transformers are widely used for Natural Language Processing (NLP).",
        body_style
    ))

    content.append(Paragraph("Unit 4: Large Language Models and RAG Architecture", heading_style))
    content.append(Paragraph(
        "Large Language Models (LLMs) are deep learning models trained on vast amounts of text data to generate human-like text and perform NLP tasks. "
        "Retrieval-Augmented Generation (RAG) is an architectural framework that optimizes LLM output by referencing an authoritative external knowledge base (such as ChromaDB vector stores) outside of its training data before generating a response. "
        "RAG reduces hallucination and provides up-to-date, factual domain-specific answers.",
        body_style
    ))

    doc.build(content)
    print(f"Sample textbook PDF successfully created at: {output_path}")

if __name__ == "__main__":
    generate_sample_pdf()
