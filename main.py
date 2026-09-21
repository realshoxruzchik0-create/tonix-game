import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Logging sozlamalari (konsolda xatolar ko'rinishi uchun)
logging.basicConfig(level=logging.INFO)

# Telegram Bot Tokeningiz
BOT_TOKEN = "8648218746:AAGHmVB88Vy-OeP8PJZ7mRMBUPWNwQWhemM"

# GitHub Pages orqali olingan sizning WebApp havolangiz
WEBAPP_URL = "https://realshoxruzchik0-create.github.io/tonix-game/"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    # WebApp tugmasini hosil qilish
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="📈 Exness Forex Terminalni Ochish", 
            web_app=WebAppInfo(url=WEBAPP_URL)
        )]
    ])
    
    await message.answer(
        f"Salom, <b>{message.from_user.first_name}</b>! 👋\n\n"
        "Exness Trading simulatoriga xush kelibsiz.\n"
        "Real vaqtdagi Forex grafiklarini tahlil qilish va savdo qilish uchun quyidagi tugmani bosing:",
        parse_mode="HTML",
        reply_markup=keyboard
    )

async def main():
    print("Bot muvaffaqiyatli ishga tushdi!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
