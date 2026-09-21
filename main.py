import asyncio
import json
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Bot tokeningizni shu yerga yozasiz
TOKEN = "SIZNING_BOT_TOKENINGIZ"
# Zakazlar kelib tushadigan o'zingizning Telegram ID'ingiz
ADMIN_ID = 123456789 

bot = Bot(token=TOKEN)
dp = Dispatcher()

# /start buyrug'i bosilganda Web App ochiladigan tugmani chiqaramiz
@dp.message(CommandStart())
async def cmd_start(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="💎 Tanga Sotib Olish", 
                    web_app=WebAppInfo(url="SIZNING_WEBSITE_SILKANGIZ_SIRDAS") # Hostingdagi index.html manzili
                )
            ]
        ]
    )
    await message.answer(
        "Salom! Ommabop ovozli chat va efir ilovalari uchun tangalarni avtomatlashtirilgan tarzda xarid qiling 👇",
        reply_markup=keyboard
    )

# Mini App ichidan "Sotib olish" tugmasi bosilganda ma'lumotlar shu yerga keladi
@dp.message(F.web_app_data)
async def web_app_receive(message: Message):
    try:
        # Web App'dan kelgan JSON ma'lumotni o'qiymiz
        data = json.loads(message.web_app_data.data)
        
        platform = data.get("platform")
        userid = data.get("userid")
        package = data.get("package")
        price = data.get("price")
        
        user_name = message.from_user.full_name
        username = f"@{message.from_user.username}" if message.from_user.username "Mavjud emas"
        user_tg_id = message.from_user.id

        # Foydalanuvchiga buyurtma qabul qilingani haqida xabar beramiz
        await message.answer(
            f"✅ **Buyurtmangiz qabul qilindi!**\n\n"
            f"📱 Ilova: {platform}\n"
            f"🆔 User ID: {userid}\n"
            f"📦 Paket: {package}\n"
            f"💵 Narxi: {price}\n\n"
            f"Tez orada administratorlar tangani ID raqamingizga tashlab berishadi!"
        )

        # Administratorga yangi zakaz haqida xabar yuboramiz
        admin_text = (
            f"🚨 **YANGI BUYURTMA!**\n\n"
            f"📱 Ilova: {platform}\n"
            f"🆔 User ID: <code>{userid}</code>\n"
            f"📦 Paket: {package}\n"
            f"💵 Narxi: {price}\n\n"
            f"👤 Xaridor: {user_name} ({username})\n"
            f"🔗 Telegram ID: <code>{user_tg_id}</code>"
        )
        
        await bot.send_message(chat_id=ADMIN_ID, text=admin_text, parse_mode="HTML")

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos qaytadan urinib ko'ring.")
        print(f"Xato: {e}")

async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
