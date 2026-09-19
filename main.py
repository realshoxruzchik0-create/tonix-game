import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode

# Bot tokeningiz
TOKEN = "8695811464:AAG09aLyLwWdQ4YVLlrkBz-21hk6cRvktrk"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# /start buyrug'i kelganda ishlaydigan bo'lim
@dp.message(CommandStart())
async def start_handler(message: types.Message):
    # Custom emoji ID: 5990173055026990900
    custom_emoji = '<tg-emoji emoji-id="5990173055026990900">✔️</tg-emoji>'
    
    # Yuboriladigan matn
    text = f"Assalomu alaykum dev {custom_emoji}"
    
    # HTML formatida javob qaytarish
    await message.answer(text, parse_mode=ParseMode.HTML)

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Bot muvaffaqiyatli ishga tushdi!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
