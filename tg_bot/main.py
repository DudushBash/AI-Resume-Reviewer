from pathlib import Path
from fastapi import FastAPI, UploadFile, File
from parser import extract_text
from llm import review_resume

app = FastAPI()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.get("/")
async def root():
    return {"message": "AI Resume Reviewer API"}
@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    filename = Path(file.filename).name
    file_path = UPLOAD_DIR / filename
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    resume_text = extract_text(file_path)
    review = review_resume(resume_text)
    return {"filename": filename,"review": review}