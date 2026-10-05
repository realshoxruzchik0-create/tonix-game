import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

TOKEN = "8807749721:AAF3WaIQspoQI9nf1HJi4uF3Y0IJTzRntaU"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    web_app_url = "https://realshoxruzchik0-create.github.io/tonix-game/index.html"
    
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
    
    # Siz xohlagan matn va custom emoji (HTML formatida)
    text = (
        "Salom UZUZ.BET qumor oʻyiniga hush kelibsiz "
        "<tg-emoji id=\"5370941588165893740\">✅</tg-emoji>"
    )
    
    await message.answer(
        text,
        reply_markup=keyboard,
        parse_mode="HTML"
    )

async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
