import React, { useState } from "react";
import UploadBox from "./components/UploadBox";
import ChatBox from "./components/ChatBox";
import "./App.css";
import logo from "./assets/logo.png";

function App() {
  const [sessionId, setSessionId] = useState(null);
  const [messages, setMessages] = useState([]); // Store chat history

  const handleUpload = (id) => {
    setSessionId(id);
    setMessages([]); // Clear previous chats
  };

  const handleResetChat = () => setMessages([]);
  const handleNewDocument = () => {
    setSessionId(null);
    setMessages([]);
  };

  return (
    <div className="app-container">
      <img
        src={logo}
        alt="Theorex Logo"
        className={` ${sessionId ? "logo-top" : "logo"}`} // Shrinks when chat screen
      />

      {!sessionId ? (
        <UploadBox onUpload={handleUpload} />
      ) : (
        <div className="chat-wrapper">
          <ChatBox
            sessionId={sessionId}
            messages={messages}
            setMessages={setMessages}
            onResetChat={handleResetChat}
            onNewDocument={handleNewDocument}
          />
        </div>
      )}
    </div>
  );
}

export default App;
