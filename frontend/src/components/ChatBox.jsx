import React, { useState } from "react";
import axios from "axios";

export default function ChatBox({ sessionId, onResetChat, onNewDocument }) {
  const [query, setQuery] = useState("");
  const [messages, setMessages] = useState([]); // Chat history
  const [loading, setLoading] = useState(false);

  const handleResetChat = () => {
    setMessages([]);
    onResetChat();
  }
  const handleAsk = async () => {
    if (!query.trim()) return;

    const userMessage = { type: "user", text: query };
    setMessages((prev) => [...prev, userMessage]);
    setQuery(""); // Clear input
    setLoading(true);

    try {
      const response = await axios.post("http://127.0.0.1:8000/ask", {
        question: query,
        session_id: sessionId,
      });

      const aiMessage = { type: "ai", text: response.data.answer };
      setMessages((prev) => [...prev, aiMessage]);
    } catch (error) {
      console.error("Error fetching answer:", error);
      const errorMessage = {
        type: "ai",
        text: "⚠️ Failed to fetch answer. Try again.",
      };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-wrapper">
      {/* Chat Messages */}
      <div className="chat-messages">
        {messages.map((msg, index) => (
          <div
            key={index}
            className={msg.type === "user" ? "query-box" : "answer-box"}
          >
            {msg.text}
          </div>
        ))}
      </div>

      {/* Query Bar */}
      <div className="query-bar">
        <button className="action-btn" onClick={handleResetChat}>
          ⟳
        </button>

        <input
          type="text"
          className="query-input"
          placeholder="In context of your Document, please type your query..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />

        <button
          className="ask-btn"
          onClick={handleAsk}
          disabled={loading}
        >
          {loading ? "?" : "Ask"}
        </button>

        <button className="action-btn" onClick={onNewDocument}>
          +
        </button>
      </div>
    </div>
  );
}
