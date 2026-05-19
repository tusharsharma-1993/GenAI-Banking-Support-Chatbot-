import os
from typing import List, Tuple
import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter
from PyPDF2 import PdfReader
import io

class RAGEngine:
    def __init__(self):
        # Simple in-memory embeddings (no API key needed for demo)
        self.embeddings = None
        self.llm = None
        
        self.client = chromadb.PersistentClient(path="./chroma_db")
        
        try:
            self.collection = self.client.get_collection("banking_docs")
        except:
            self.collection = self.client.create_collection("banking_docs")
        
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        
        self.sessions = {}
    
    def ingest_document(self, content: bytes, filename: str) -> int:
        if filename.endswith('.pdf'):
            text = self._extract_pdf(content)
        else:
            text = content.decode('utf-8')
        
        chunks = self.text_splitter.split_text(text)
        
        for i, chunk in enumerate(chunks):
            # Use ChromaDB's default embeddings
            self.collection.add(
                documents=[chunk],
                metadatas=[{"source": filename, "chunk": i}],
                ids=[f"{filename}_{i}"]
            )
        
        return len(chunks)
    
    def _extract_pdf(self, content: bytes) -> str:
        pdf_file = io.BytesIO(content)
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    
    def query(self, message: str, session_id: str, history: List[dict]) -> Tuple[str, List[str]]:
        if session_id not in self.sessions:
            self.sessions[session_id] = []
        
        # Use ChromaDB's default query
        results = self.collection.query(
            query_texts=[message],
            n_results=3
        )
        
        context = "\n\n".join(results['documents'][0]) if results['documents'] else ""
        sources = [m['source'] for m in results['metadatas'][0]] if results['metadatas'] else []
        
        history_text = ""
        if history:
            for msg in history[-4:]:
                role = msg.get('role', 'user')
                content = msg.get('content', '')
                history_text += f"{role}: {content}\n"
        
        # Simple rule-based response (no LLM needed for demo)
        if context:
            answer = f"Based on the documents, here's what I found:\n\n{context[:500]}..."
        else:
            answer = "I don't have specific information about that in my knowledge base. Please upload relevant documents or ask about loans, credit cards, or banking services."
        
        self.sessions[session_id].append({"role": "user", "content": message})
        self.sessions[session_id].append({"role": "assistant", "content": answer})
        
        return answer, list(set(sources))
