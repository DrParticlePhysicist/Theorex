import React, { useState } from "react";
import { uploadDocument } from "../api";

export default function UploadBox({ onUpload }) {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (file) {
      try {
        const response = await uploadDocument(file);
        onUpload(response.session_id);
      } catch (error) {
        console.error("Upload failed:", error);
        alert("Upload failed. Please try again.");
      }
    } else {
      alert("Please select a file first.");
    }
  };

  return (
    <div className="upload-container">
      {/* Custom file upload button */}
      <label htmlFor="file-upload" className="custom-file-upload">
        {file ? file.name : "Choose File"}
      </label>
      <input
        id="file-upload"
        type="file"
        onChange={handleFileChange}
        style={{ display: "none" }}
      />
      
      {/* Upload button */}
      <button onClick={handleUpload} className="upload-btn">
        Upload
      </button>
    </div>
  );
}
