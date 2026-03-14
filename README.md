# LLM Chatbot with LangChain and Ollama

A simple AI chatbot built using **Python**, **LangChain**, and a locally hosted **Large Language Model (LLM)** using Ollama.

This project demonstrates how to integrate a local LLM with LangChain to create a conversational AI application that runs entirely on your local machine.

---

## Features

- Interactive command-line chatbot
- Uses LangChain for LLM orchestration
- Runs a local LLM using Ollama
- No external API or paid services required

---

## Tech Stack

- Python  
- LangChain  
- Ollama  
- Llama3 model  

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/nikithamarythomas/llm_chatbot_project.git
cd llm_chatbot_project
```

### 2. Install dependencies

```bash
pip install langchain langchain-community
```

### 3. Install Ollama

Download and install Ollama from:

https://ollama.com/download

### 4. Pull the LLM model

```bash
ollama pull llama3
```

---

## Running the Chatbot

Run the chatbot using:

```bash
python chatbot.py
```

Example interaction:

```
You: What is machine learning?
AI: Machine learning is a field of artificial intelligence that allows systems to learn from data...
```

---

## Project Structure

```
llm_chatbot_project
│
├── chatbot.py
└── README.md
```

---

## Future Improvements

- Add document-based Q&A using Retrieval Augmented Generation (RAG)
- Add conversation memory
- Build a web interface using Streamlit
- Support multiple LLM models

---

