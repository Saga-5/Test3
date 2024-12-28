from aiogram import types
from aiogram.dispatcher import Dispatcher
from database import cursor

async def show_products(message: types.Message):
    products = cursor.execute("SELECT * FROM products").fetchall()
    if not products:
        await message.answer("Список товаров пуст.")
    else:
        for product in products:
            await message.bot.send_photo(
                chat_id=message.chat.id,
                photo=product[5],
                caption=f"Название: {product[0]}\nКатегория: {product[1]}\nРазмеры: {product[2]}\nЦена: {product[3]}\nАртикул: {product[4]}"
            )

def register_products(dp: Dispatcher):
    dp.register_message_handler(show_products, commands=["products"])