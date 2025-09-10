# HR-ChatBot
# HR Resource Query Chatbot

## Overview
This project is an AI-powered HR chatbot that helps HR teams quickly find and evaluate employees based on their skills, experience, projects, and availability. Users can ask queries like:

- "Find Python developers with 3+ years experience"
- "Who has worked on healthcare projects?"
- "Suggest people for a React Native project"
- "Find developers who know both AWS and Docker"

The chatbot combines **simple rule-based searches** for straightforward queries (like name or years of experience) and **semantic search** using embeddings for complex multi-skill queries. The system is designed to integrate with both **OpenAI** or **Google Gemini** LLMs.

---

## Features
- Conversational AI interface for HR queries.
- Simple search tools:
  - Search by employee name
  - Search by years of experience
- Semantic search using employee skills, projects, and experience embeddings.
- Clean, human-readable HR recommendation output.
- Web interface (HTML/CSS/JS) with Flask backend.

---

## Architecture
- **Frontend:** Simple HTML/CSS/JS chat interface.
- **Backend:** Flask API with `/chat` endpoint for queries.
- **Tools Layer:**  
  - `normalQueryTools.py` for basic searches (hand-written).  
  - `semanticSearchTool.py` for embedding-based searches.
- **LLM Agent:** Routes user queries to appropriate tools and formats final response.
- **Embeddings:** `sentence-transformers` used to embed employee data for semantic search.
- **FAISS:** Fast similarity search to retrieve top candidates.

---

## Setup & Installation

1. **Clone the repository:**
```bash
git clone <repository_url>
cd <repository_folder>
```

## Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows
```

## Install dependencies:
```bash
pip install -r requirements.txt
```

## Add your API keys:
Create a .env file in the root directory:
```bash
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_google_gemini_key_here
```

## Run the Flask app:

```bash
python app.py
```

## Access the frontend:
Open your browser at http://127.0.0.1:8000

## API Documentation
POST /chat

  -Description: Sends a user query to the HR agent and returns a response.

Request JSON:
```bash
{
  "message": "Find Python developers with 3+ years experience"
}
```

Response JSON:
```bash
{
  "reply": "Based on your requirements, I found 3 excellent candidates: ..."
}
```
## AI Development Process

AI Coding Assistants Used: ChatGPT

Usage:
  - Generated Flask boilerplate, agent setup, and semantic search embedding code. 
  - Hand-wrote normalQueryTools.py (name and experience search).
  - Architecture and flow designed manually from the start.
  - AI Assistance vs Manual:
  - ~50% code AI-assisted, ~50% hand-written.
  - Interesting AI Solutions: Fast semantic search integration using FAISS + embeddings.
  - Manual Work: Query routing, basic search tools, and system design.

## Technical Decisions

  - LLM Choice: Used ChatGPT due to stability, speed, and optimization.
  - Local vs Cloud LLM: Cloud APIs used to avoid local GPU requirements and speed up prototyping.

## Trade-offs:
  - Performance optimized via FAISS + embeddings.
  - Cost considered by using local caching of embeddings.
  - Privacy maintained as employee data remains local; only queries are sent to LLM.

## Future Improvements
  - Add more tools (search by skills, projects, availability).
  - Integrate feedback loop to improve semantic search ranking.
  - Enable multi-user sessions with memory tracking.
  - UI improvements with React for a richer experience.
