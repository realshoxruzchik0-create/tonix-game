import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

# Bot Tokeningni shu yerga yozasan (BotFather'dan olgan token)
TOKEN = "SENING_BOT_TOKENING_BU YERGA_YOZILADI"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    # Web App ochiladigan tugma (sayting tayyor bo'lganda linkini qo'yasan)
    web_app_url = "https://seni-sayting-manzili.com" 
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🚀 O'yinni Boshlash (Tap)", web_app=WebAppInfo(url=web_app_url))]
        ]
    )
    
    welcome_text = (
        "Assalomu alaykum!\n\n"
        "Bot orqali Ton, Tron, Bitcoin, Notcoin va USDT ishlab, "
        "o'z hamyoningizga yechib olishingiz mumkin.\n\n"
        "Pastdagi tugmani bosing va tanga yig'ishni boshlang!"
    )
    
    await message.answer(welcome_text, reply_markup=keyboard)

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
