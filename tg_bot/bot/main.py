from aiogram import Bot, Dispatcher
import asyncio
from config import TOKEN
from handlers.start import router as start_router
from handlers.review import router as review_router


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(start_router)
    dp.include_router(review_router)
    print("Bot started")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())