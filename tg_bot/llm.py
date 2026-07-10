from urllib import response
import os 
import requests
from dotenv import load_dotenv


load_dotenv()
OLLAMA_URL = os.getenv("OLLAMA_URL")
MODEL = os.getenv("MODEL")

def review_resume(resume_text: str):
    prompt = f"""
Ты опытный HR и Senior Software Engineer.

Проанализируй это резюме.

Верни ответ в следующем формате:

Оценка: X/10

Сильные стороны:
- ...

Недостатки:
- ...

Что улучшить:
- ...

Резюме:

{resume_text}
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
            },
            timeout=300,
        )

        response.raise_for_status()

        data = response.json()

        return data.get("response", "Модель не вернула ответ.")

    except requests.exceptions.ConnectionError:
        return "Не удалось подключиться к Ollama. Убедись, что она запущена."

    except requests.exceptions.Timeout:
        return "Время ожидания ответа от модели истекло."

    except Exception as e:
        return f"Ошибка: {e}"
