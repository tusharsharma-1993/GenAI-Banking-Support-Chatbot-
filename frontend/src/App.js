import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import { v4 as uuidv4 } from 'uuid';
import './App.css';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [sessionId] = useState(() => uuidv4());
  const [uploading, setUploading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSend = async () => {
    if (!input.trim() || loading) return;

    const userMessage = { role: 'user', content: input };
    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setLoading(true);

    try {
      const response = await axios.post(`${API_URL}/chat`, {
        message: input,
        session_id: sessionId,
        history: messages
      });

      const botMessage = {
        role: 'assistant',
        content: response.data.response,
        sources: response.data.sources
      };
      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      const errorMessage = {
        role: 'assistant',
        content: 'Sorry, I encountered an error. Please try again.',
        error: true
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setLoading(false);
    }
  };

  const handleFileUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    setUploading(true);
    const formData = new FormData();
    formData.append('file', file);

    try {
      await axios.post(`${API_URL}/upload`, formData);
      alert(`Document "${file.name}" uploaded successfully!`);
    } catch (error) {
      alert('Upload failed. Please try again.');
    } finally {
      setUploading(false);
      e.target.value = '';
    }
  };

  return (
    <div className="App">
      <div className="chat-container">
        <div className="chat-header">
          <label className="upload-btn">
            {uploading ? '⏳ Uploading...' : '📄 Upload'}
            <input
              type="file"
              accept=".pdf,.txt"
              onChange={handleFileUpload}
              disabled={uploading}
              style={{ display: 'none' }}
            />
          </label>
          <h1>Banking Assistant</h1>
          <div className="beta-badge">
            Beta ⓘ
          </div>
          <div className="header-subtitle">Our bot answers instantly</div>
        </div>

        <div className="messages">
          {messages.length === 0 && (
            <div className="welcome">
              <div className="welcome-icon">🏦</div>
              <h2>Hey there, thanks for visiting!</h2>
              <p>How can I help you?</p>
            </div>
          )}
          {messages.map((msg, idx) => (
            <div key={idx} className={`message ${msg.role}`}>
              {msg.role === 'assistant' && <div className="bot-avatar">🤖</div>}
              <div className="message-content">
                {msg.content}
                {msg.sources && msg.sources.length > 0 && (
                  <div className="sources">
                    📎 Sources: {msg.sources.join(', ')}
                  </div>
                )}
              </div>
            </div>
          ))}
          {loading && (
            <div className="message assistant">
              <div className="bot-avatar">🤖</div>
              <div className="typing">
                <span></span>
                <span></span>
                <span></span>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        <div className="input-area">
          <div className="input-wrapper">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && handleSend()}
              placeholder="Send a message..."
              disabled={loading}
            />
          </div>
          <button className="send-btn" onClick={handleSend} disabled={loading || !input.trim()}>
            ▶
          </button>
        </div>
        
        <div className="powered-by">
          Powered By <span>Banking AI</span>
        </div>
      </div>
      
      <button className="feedback-btn">Feedback</button>
    </div>
  );
}

export default App;
