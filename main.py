import os
import logging
import sys
from aiohttp import web
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Token va Port sozlamalari
TOKEN = os.getenv("BOT_TOKEN", "SIZNING_BOT_TOKENINGIZ")
PORT = int(os.environ.get("PORT", 8080))

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    # Render'ga joylaganingizdan keyin chiqadigan havolangiz (masalan: https://uzwinbetbot.onrender.com)
    # Yoki buni Render'dagi EnvironmentVariables ga WEB_APP_URL qilib kiritishingiz ham mumkin
    web_app_url = os.getenv("WEB_APP_URL", "https://SIZ_PROYEKT_NOMINGIZ.onrender.com")
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🦎 UzWinBetBot-ni Ochish", web_app=WebAppInfo(url=web_app_url))]
    ])
    
    await message.answer(
        f"Salom, {html.bold(message.from_user.full_name)}! 🎲\n\n"
        "<b>UzWinBetBot</b> rasmiy ilovasiga xush kelibsiz. "
        "Kirish uchun pastdagi tugmani bosing:",
        reply_markup=keyboard
    )

# Foydalanuvchi saytga kirganda index.html ni ko'rsatish
async def index_handler(request):
    return web.FileResponse('./index.html')

async def health_check(request):
    return web.Response(text="Bot ishlayapti!")

async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    
    # Aiohttp veb-serverini yaratamiz (Render portni talab qilgani uchun)
    app = web.Application()
    app.router.add_get('/', index_handler)
    app.router.add_get('/health', health_check)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', PORT)
    await site.start()

    logging.info(f"Veb-server {PORT}-portda ishga tushdi va bot polling boshlanmoqda...")
    
    # Botni ishga tushiramiz
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    import asyncio
    asyncio.run(main())
