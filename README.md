# AI Resume Reviewer

AI Resume Reviewer is a Telegram bot and FastAPI backend that analyzes resumes using a local Large Language Model (LLM) running through Ollama.

The project allows users to upload a PDF or DOCX resume, extracts the text, sends it to a local Qwen model, and returns detailed feedback on the resume.

## Features

* Upload PDF and DOCX resumes
* Resume text extraction
* AI-powered resume analysis
* Local LLM inference with Ollama (no external AI APIs required)
* FastAPI REST API
* Telegram Bot built with Aiogram
* Modular project structure

## Tech Stack

* Python
* FastAPI
* Aiogram 3
* Ollama
* Qwen3:8B
* HTTPX
* python-dotenv

## Project Structure

```text
project/
│
├── backend/
│   ├── main.py
│   ├── parser.py
│   ├── llm.py
│   └── uploads/
│
├── bot/
│   ├── handlers/
│   ├── services/
│   ├── config.py
│   ├── main.py
│   └── .env
│
├── requirements.txt
└── README.md
```

## How It Works

```text
Telegram User
      │
      ▼
Telegram Bot (Aiogram)
      │
      ▼
FastAPI Backend
      │
      ▼
Resume Parser
      │
      ▼
Qwen3 (Ollama)
      │
      ▼
Resume Review
      │
      ▼
Telegram User
```

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/ai-resume-reviewer.git
cd ai-resume-reviewer
```

### Create a virtual environment

```bash
python -m venv .venv
```

Activate it.

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Install Ollama

Install Ollama from:

https://ollama.com

Download the model:

```bash
ollama pull qwen3:8b
```

Run the model:

```bash
ollama run qwen3:8b
```

## Environment Variables

Create a `.env` file.

### Backend

```env
OLLAMA_URL=http://localhost:11434/api/generate
MODEL=qwen3:8b
```

### Telegram Bot

```env
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
API_URL=http://127.0.0.1:8000
```

## Running the Backend

```bash
cd backend
python -m uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

## Running the Telegram Bot

```bash
cd bot
python main.py
```

## API Endpoint

### Upload Resume

```
POST /uploadfile/
```

Request:

* multipart/form-data
* file (PDF or DOCX)

Response:

```json
{
  "filename": "resume.pdf",
  "review": "AI-generated review..."
}
```

## Current Capabilities

* Resume upload
* PDF parsing
* DOCX parsing
* Local AI analysis
* Telegram integration

## Planned Improvements

* ATS compatibility analysis
* Resume score in structured JSON
* Resume improvement suggestions
* Resume vs Job Description matching
* Review history
* PostgreSQL integration
* Docker support
* Authentication
* Web interface

## License

This project is intended for educational and portfolio purposes.
