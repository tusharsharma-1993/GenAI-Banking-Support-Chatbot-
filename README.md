# GenAI Banking Support Chatbot

An AI-powered banking support chatbot using Retrieval-Augmented Generation (RAG) to answer customer queries about loans, credit cards, and banking FAQs.

## Architecture

- **Frontend**: React with TypeScript
- **Backend**: FastAPI (Python)
- **Vector Database**: ChromaDB
- **LLM**: OpenAI GPT-3.5-turbo
- **Embeddings**: OpenAI text-embedding-ada-002

## Features

- ✅ RAG pipeline with document ingestion
- ✅ Vector database for semantic search
- ✅ Context-aware conversations
- ✅ PDF and TXT document support
- ✅ Session-based chat history
- ✅ REST APIs for chat and document upload
- ✅ Responsive UI with loading indicators

## Setup Instructions

### Prerequisites

- Python 3.9+
- Node.js 16+
- OpenAI API key

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Add your OPENAI_API_KEY to .env
python app.py
```

### Frontend Setup

```bash
cd frontend
npm install
npm start
```

### Environment Variables

Create `backend/.env`:
```
OPENAI_API_KEY=your_api_key_here
```

## API Endpoints

- `POST /chat` - Send chat messages
- `POST /upload` - Upload documents (PDF/TXT)
- `GET /health` - Health check

## Deployment

Deploy to Render, Railway, or AWS Free Tier. See deployment guide in docs.

## Demo

[Add deployment URL here]
