import fitz  # PyMuPDF for PDF
import docx  # python-docx for DOCX
import io

def extract_text(filename: str, content: bytes) -> str:
    if filename.endswith(".pdf"):
        with fitz.open(stream=content, filetype="pdf") as doc:
            text = ""
            for page in doc:
                text += page.get_text()
            return text

    elif filename.endswith(".docx"):
        doc = docx.Document(io.BytesIO(content))
        return "\n".join([para.text for para in doc.paragraphs])

    elif filename.endswith(".txt"):
        return content.decode("utf-8")

    else:
        return ""