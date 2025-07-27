import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000",
});

export const uploadDocument = async (file) => {
  const formData = new FormData();
  formData.append("file", file);
  const res = await API.post("/upload", formData);
  return res.data;
};

export const askQuestion = async (sessionId, question) => {
  const res = await API.post("/ask", { session_id: sessionId, question });
  return res.data.answer;
};