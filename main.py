from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8821101595:AAFzvcbSWUZpAa7qmzv3rinvVSMCmiE32jA"
bot = Bot(token=TOKEN)
dp = Dispatcher()

# 1. Asosiy menyu (Start bosilganda)
@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛒 Xaridni Boshlash", callback_data="menu")],
        [InlineKeyboardButton(text="📢 Yangiliklar", url="https://t.me/lavpin_donat")]
    ])
    await message.answer_photo(
        photo="AgACAgEAAxkBAAMeaol63izZUgIsNIZCgKVVUpOVbnMAAjgNaxs1vUlEUZgcRYxeP2sBAAMCAAN5AAM9BA",
        caption="Lavpin botga xush kelibsiz! Xaridni boshlash uchun tugmani bosing.",
        reply_markup=kb
    )

# 2. Xarid bo'limi (Tugma bosilganda chiqadigan menyu)
@dp.callback_query(F.data == "menu")
async def show_menu(callback: types.CallbackQuery):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="PUBG Mobile UC 💎", callback_data="pubg")],
        [InlineKeyboardButton(text="Free Fire Donat 🎮", callback_data="ff")]
    ])
    await callback.message.edit_caption(
        caption="Kerakli xizmatni tanlang:",
        reply_markup=kb
    )

async def main():
    await dp.start_polling(bot)

import asyncio
if __name__ == "__main__":
    asyncio.run(main())
