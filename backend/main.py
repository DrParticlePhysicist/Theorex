from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from llm_pipeline import answer_question  # ✅ Directly import function
from file_utilities import extract_text

app = FastAPI()

# Allow frontend CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # ✅ Change this to your frontend domain if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store uploaded document text in-memory
rag_sessions = {}

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    content = await file.read()
    text = extract_text(file.filename, content)

    if not text:
        return {"error": "Unsupported file type or empty document."}

    # ✅ Instead of storing DocumentRAG object, store raw text
    rag_sessions[file.filename] = text
    return {"message": "File processed successfully.", "session_id": file.filename}


class Query(BaseModel):
    session_id: str
    question: str

@app.post("/ask")
async def ask_question(query: Query):
    document_text = rag_sessions.get(query.session_id)

    if not document_text:
        return {"error": "Session not found. Please upload document first."}

    # ✅ Directly call the function with text and query
    response = answer_question(document_text, query.question)
    return {"answer": response}
