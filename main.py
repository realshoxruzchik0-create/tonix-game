import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

# Siz bergan bot tokeni joylashtirildi
TOKEN = "8807749721:AAF3WaIQspoQI9nf1HJi4uF3Y0IJTzRntaU"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    # Bu yerga HTML faylingizni internetga (Render yoki GitHub Pages) yuklagandan keyingi havolasini qo'yasiz
    web_app_url = "https://sizning-domen.uz/index.html"
    
    # Web App'ni ochuvchi tugma
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🎮 UZUZ.BET ni ochish", 
                    web_app=WebAppInfo(url=web_app_url)
                )
            ]
        ]
    )
    
    await message.answer(
        "👋 Salom! **UZUZ.BET** hazil stavka botiga xush kelibsiz!\n\n"
        "Quyidagi tugmani bosing va o'yinni boshlang:",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )

async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
