import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
APP_URL = "https://gagazechka-github-io.vercel.app/"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    # Создаем кнопку, которая открывает Mini App
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Играть в Кроссворд 🧩", 
                web_app=WebAppInfo(url=APP_URL)
            )
        ]
    ])
    
    await message.answer(
        f"Привет, {message.from_user.full_name}!\n\n"
        "Нажми на кнопку ниже, чтобы запустить кроссворд прямо в Telegram.",
        reply_markup=markup
    )

async def main():
    while True:
        try:
            print("Бот запущен...")
            await dp.start_polling(bot)
        except Exception as e:
            print(f"Произошла ошибка соединения: {e}")
            print("Попытка перезапуска через 5 секунд...")
            await asyncio.sleep(5) # Ждем, чтобы не спамить запросами

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен пользователем")