# Agentic Workflow
This project is a RAG-based ReAct AI agent system.

The system allows a client to upload PDF documents to a server.
The server processes the PDFs and uses them as external knowledge for Retrieval-Augmented Generation (RAG).

The system combines:
- Vector Database
- Memory
- ReAct Agent Pattern
- LangChain Orchestration
- LangSmith Monitoring
- LLM Reasoning
- Database Storage

The goal is to create an intelligent AI assistant capable of reasoning, retrieving knowledge, and interacting conversationally.

# System Architecture

Client
   ↓
PDF Upload
   ↓
Server
   ↓
PDF Processing
   ↓
Chunking
   ↓
Embedding Model
   ↓
Vector Database
   ↓
Retriever
   ↓
ReAct Agent
   ↓
LLM (ChatGPT)
   ↓
Memory
   ↓
Final Response


The client uploads PDF documents and sends user questions.


The server orchestrates the entire AI workflow.

RAG (Retrieval-Augmented Generation) retrieves relevant PDF content before generating responses.

The vector database stores embeddings of PDF chunks for semantic search.

Memory stores previous interactions for conversational continuity.

The ReAct agent follows the Reason + Act pattern:

Thought → Action → Observation → Final Answer

LangChain orchestrates tools, memory, retrieval, and agent execution.

LangSmith monitors and traces the execution flow of the agent system.

# ReAct Workflow

User Question
    ↓
Thought
    ↓
Retrieve PDF Context
    ↓
Observation
    ↓
Reasoning
    ↓
Generate Answer

# Technologies

- Python
- LangChain
- LangSmith
- OpenAI
- ChromaDB / FAISS
- FastAPI
- ReAct Agent Pattern
- RAG Pipeline