from pathlib import Path
import httpx
from config import API_URL

async def send_resume(file_path: str):
    async with httpx.AsyncClient(timeout=300) as client:
        with open(file_path, "rb") as f:
            response = await client.post(
                f"{API_URL}/uploadfile/",
                files={
                    "file": (
                        Path(file_path).name,
                        f,
                        "application/pdf",
                    )
                },
            )

        response.raise_for_status()

        return response.json()