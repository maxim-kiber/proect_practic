from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
import asyncio
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utils import get_quote

bot = Bot(
    token="7120474955:AAFAb88Vfek-l30zn8-m2xYp4LBDaKMhkWU",
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Получить цитату")]
    ], resize_keyboard=True
)

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "С помощью этого бота вы можете получить рандомную цитату!\nДля получения цитаты нажмите кнопку.",
        reply_markup=keyboard
    )

@dp.message(F.text.lower() == "получить цитату")
async def handle_quote(message: Message):
    data = get_quote()
    quote = data.get("quote")
    author = data.get("author")
    await message.answer(
        f'"{quote}"\n'
        f'(c) {author}',
        reply_markup=keyboard
    )

async def start_bot():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        print("end")