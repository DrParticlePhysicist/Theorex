# Theorex

Theorex is an advanced AI-powered document analysis and context aware question-answering system facilitaing you to get specific and efficient answer for your questions/queries relevant to the context and not the global Knowledge base. It empowers users to upload documents and interact with them conversationally using natural language queries.

---

## Project Structure

```
Theorex/
├── backend/            # FastAPI backend serving the API and RAG pipeline
│   ├── main.py           # FastAPI application entry point
│   ├── api.py            # API routes (upload, ask, reset)
│   ├── rag_pipeline.py      # Core Retrieval-Augmented Generation (RAG) logic
│   ├── CRLLM.py      # a custom made runnable which behaves as an text generation LLM required by project Logic
│   ├── file_utilitiess.py          # Utility functions (embedding, text parsing)
│   ├── requirements.txt       # Python dependencies
│
├── frontend/             # React frontend providing the user interface
│   ├── src/
│   │   │── assets/       # Images (e.g., Theorex logo, background)
│   │   ├── components/
│   │   │   ├── UploadBox.jsx         # File upload component
│   │   │   ├── ChatBox.jsx         # Chat UI component
│   │   ├── App.jsx          # Main React component
│   │   ├── App.css          # Styling (with animations)
├   ├── api.js          # API routes (upload, ask, reset)
│   ├── package.json            # Frontend dependencies
│
└── README.md              # Project documentation
```

---

## Features

- Upload PDF documents for analysis
- Chat-based query system powered by LLMs
- Retrieval-Augmented Generation (RAG) pipeline for contextual answers
- Responsive UI with smooth transitions
- Separate Reset and New Document workflows

---

## Tech Stack

### Frontend

- **React** (UI Framework)
- **CSS Animations** (Logo transitions, background zoom effects)
- Axios (API calls)

### Backend

- **FastAPI** (REST API framework)
- **LangChain** (RAG implementation)
- **OpenAI API** (LLM for answering queries)
- **FAISS** (for semantic search and embeddings)

---

## Architecture Overview

### Retrieval-Augmented Generation (RAG)

1. **Document Upload**

   - User uploads a PDF document.
   - Backend parses and splits the text into chunks.

2. **Vectorization**

   - Each chunk is embedded using OpenAI embeddings.
   - Stored in a FAISS vector database for similarity search.

3. **Query Handling**

   - User enters a natural language query.
   - Backend retrieves relevant document chunks using similarity search.

4. **LLM Response**

   - Retrieved chunks are sent to HUGGINGFACE HuggingFaceH4/zephyr-7b-beta model with the user query.
   - LLM generates a contextualized answer.

5. **Chat UI**

   - Frontend displays user query and AI response.

```
User Query --> RAG Pipeline --> LLM --> Response
```

### Data Flow

```
Frontend (React)
   ↓
Backend API (FastAPI)
   ↓
RAG Engine (LangChain + FAISS)
   ↓
HUGGINGFACE LLM (HuggingFaceH4/zephyr-7b-beta)
   ↓
Frontend Response
```

---

## Installation & Running

### Backend (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend (React)

```bash
cd frontend
npm install
npm start
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

---

## 📄 API Endpoints

| Method | Endpoint  | Description            |
| ------ | --------- | ---------------------- |
| POST   | `/upload` | Uploads a PDF document |
| POST   | `/ask`    | Sends a user query     |
| POST   | `/reset`  | Clears session memory  |

---

## 📝 Environment Variables

Backend requires the following environment variables:

```env
HUGGINGFACEHUB_API_TOKEN=your_openai_api_key
```

---

## 👨‍💻 Developers Note

- LLM integration via HUGGINGFACE API.
- FAISS is used for in-memory vector storage.
- Designed for modularity: swap Zephyr Mistral 7b with another LLM if needed.
- Implented leveraging Langchains for swift integration and empoweing project with the chain pipelining
---

## 📌 Future Improvements

- Multi-document support
- Auth and user sessions

---

## 🏷️ License

This project is licensed under the MIT License.

