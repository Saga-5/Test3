from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage


token = config('TOKEN')

staff = ["username1" , "username2"]



storage = MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot , storage=storage)