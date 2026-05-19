from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv
from rag_engine import RAGEngine

load_dotenv()

app = FastAPI(title="Banking Support Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

rag_engine = RAGEngine()

class ChatRequest(BaseModel):
    message: str
    session_id: str
    history: Optional[List[dict]] = []

class ChatResponse(BaseModel):
    response: str
    sources: List[str]

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "banking-chatbot"}

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    try:
        content = await file.read()
        filename = file.filename
        
        if not filename.endswith(('.pdf', '.txt')):
            raise HTTPException(400, "Only PDF and TXT files supported")
        
        result = rag_engine.ingest_document(content, filename)
        return {"message": "Document uploaded successfully", "filename": filename, "chunks": result}
    except Exception as e:
        raise HTTPException(500, f"Upload failed: {str(e)}")

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        response, sources = rag_engine.query(
            request.message,
            request.session_id,
            request.history
        )
        return ChatResponse(response=response, sources=sources)
    except Exception as e:
        import traceback
        print(f"Error in chat endpoint: {str(e)}")
        print(traceback.format_exc())
        raise HTTPException(500, f"Chat failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
