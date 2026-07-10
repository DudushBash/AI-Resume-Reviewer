from pathlib import Path

DOWNLOAD_DIR = Path("downloads")
DOWNLOAD_DIR.mkdir(exist_ok=True)

async def download_document(bot, document):
    telegram_file = await bot.get_file(document.file_id)
    file_path = DOWNLOAD_DIR / document.file_name
    await bot.download(telegram_file,destination=file_path)
    return file_path