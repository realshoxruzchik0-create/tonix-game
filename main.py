from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import asyncio

TOKEN = "8821101595:AAFzvcbSWUZpAa7qmzv3rinvVSMCmiE32jA"
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🚀 Lavpin Shop Ochish", 
            web_app=WebAppInfo(url="https://realshoxruzchik0-create.github.io/tonix-game/")
        )],
        [InlineKeyboardButton(text="📢 Yangiliklar", url="https://t.me/lavpin_donat")]
    ])
    
    await message.answer_photo(
        photo="AgACAgEAAxkBAAMeaol63izZUgIsNIZCgKVVUpOVbnMAAjgNaxs1vUlEUZgcRYxeP2sBAAMCAAN5AAM9BA",
        caption="Lavpin botga xush kelibsiz! Xaridni boshlash uchun pastdagi tugmani bosing:",
        reply_markup=kb
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
