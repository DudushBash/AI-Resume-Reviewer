from aiogram import Router, F
from aiogram.types import Message
from services.downloader import download_document
from services.api import send_resume

router = Router()

@router.message(F.document)
async def review(message: Message):
    allowed = {".pdf", ".docx"}
    filename = message.document.file_name.lower()
    if not any(filename.endswith(ext) for ext in allowed):
        await message.answer("❌ Поддерживаются только PDF и DOCX.")
        return
    await message.answer("📄 Получил файл.\nНачинаю анализ...")
    file_path = await download_document(message.bot,message.document)
    result = await send_resume(str(file_path))
    await message.answer(result["review"])