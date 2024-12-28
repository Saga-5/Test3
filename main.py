from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from handlers import commands,fsm_shop,order_products,products
from db import db

commands.register_command(db)

fsm_shop.register_add_product(db)

order_products.register_order(db)

products.register_products()

if __name__ == "__main__":
    executor.start_polling(db, skip_updates=True)