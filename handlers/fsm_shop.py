from aiogram import types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import staff
from db import cursor, db

class FSMAddProduct(StatesGroup):
    name = State()
    category = State()
    size = State()
    price = State()
    article = State()
    photo = State()

async def add_product_cmd(message: types.Message):
    if message.from_user.username in staff:
        await FSMAddProduct.name.set()
        await message.answer("Введите название продукта:")
    else:
        await message.answer("Эта команда доступна только сотрудникам.")

async def add_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await FSMAddProduct.next()
    await message.answer("Введите категорию продукта:")

async def add_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["category"] = message.text
    await FSMAddProduct.next()
    await message.answer("Введите размеры продукта:")

async def add_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["size"] = message.text
    await FSMAddProduct.next()
    await message.answer("Введите цену продукта:")

async def add_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["price"] = message.text
    await FSMAddProduct.next()
    await message.answer("Введите артикул продукта:")

async def add_article(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["article"] = message.text
    await FSMAddProduct.next()
    await message.answer("Отправьте фото продукта:")

async def add_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[-1].file_id
        cursor.execute("INSERT INTO products VALUES (?, ?, ?, ?, ?, ?)",
                       (data["name"], data["category"], data["size"], data["price"], data["article"], data["photo"]))
        db.commit()
    await state.finish()
    await message.answer("Продукт успешно добавлен.")

def register_add_product(dp: Dispatcher):
    dp.register_message_handler(add_product_cmd, commands=["add_product"])
    dp.register_message_handler(add_name, state=FSMAddProduct.name)
    dp.register_message_handler(add_category, state=FSMAddProduct.category)
    dp.register_message_handler(add_size, state=FSMAddProduct.size)
    dp.register_message_handler(add_price, state=FSMAddProduct.price)
    dp.register_message_handler(add_article, state=FSMAddProduct.article)
    dp.register_message_handler(add_photo, content_types=["photo"], state=FSMAddProduct.photo)