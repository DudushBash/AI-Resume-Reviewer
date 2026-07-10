import fitz
from docx import Document
from pathlib import Path

def extract_text(file_path: str) -> str:
    path = Path(file_path)
    if path.suffix.lower() == ".pdf":
        return extract_pdf(path)
    elif path.suffix.lower() == ".docx":
        return extract_docx(path)
    else:
        raise ValueError("Unsupported file format")

def extract_pdf(path: Path):
    text = ""
    doc = fitz.open(path)
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

def extract_docx(path: Path):
    doc = Document(path)
    return "\n".join(paragraph.text for paragraph in doc.paragraphs)