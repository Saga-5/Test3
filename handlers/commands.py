from aiogram import types , Dispatcher
from config import bot

async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Здрасвуйте {message.from_user.first_name}!\n'
                                f'Ваш Telegram ID - {message.from_user.id}')


async def info_cmd(message: types.Message):
    await message.answer("Этот бот создан для управления заказами и товарами.")

def register_command(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(info_cmd, commands=["info"])