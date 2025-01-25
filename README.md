# AI-Powered_Chatbot
# Product and Supplier Chatbot

This is a chatbot application that allows users to query a product and supplier database using natural language. It uses an open-source Large Language Model (LLM) and the LangGraph framework for agent workflows to fetch relevant information from a MySQL/PostgreSQL database and summarize the data using the LLM.

## Project Structure

## Tech Stack

## folder Strucher
/chatbot-project
  /backend
    /app
      app.py
      requirements.txt
      database.py
    /models
      lang_model.py
  /frontend
    /src
      /components
        Chatbot.js
      /redux
        actions.js
        reducers.js
        store.js
      App.js
      index.js
      package.json
  .gitignore
  README.md


### Backend
- **Python** (FastAPI)
- **LangGraph** (For agent workflows)
- **Open-source LLM** (e.g., Hugging Face or LLaMA)
- **MySQL/PostgreSQL** (Database)

### Frontend
- **React** (With Material UI or Tailwind CSS)
- **Axios** (For API calls)
- **Redux** or **Context API** (For state management)

## Setup Instructions

### 1. Backend Setup

1. Install Python dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt


