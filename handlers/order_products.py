from aiogram import types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import staff

class FSMOrder(StatesGroup):
    product = State()
    quantity = State()
    size = State()
    contact = State()

async def order_cmd(message: types.Message):
    await FSMOrder.product.set()
    await message.answer("Введите название продукта, который хотите купить:")

async def order_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["product"] = message.text
    await FSMOrder.next()
    await message.answer("Введите количество:")

async def order_quantity(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["quantity"] = message.text
    await FSMOrder.next()
    await message.answer("Введите размер продукта:")

async def order_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["size"] = message.text
    await FSMOrder.next()
    await message.answer("Введите ваш номер телефона:")

async def order_contact(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["contact"] = message.text
        for user in staff:
            await message.bot.send_message(
                chat_id=user,
                text=f"Новый заказ:\nПродукт: {data['product']}\nКоличество: {data['quantity']}\nРазмер: {data['size']}\nКонтакт: {data['contact']}"
            )
    await state.finish()
    await message.answer("Ваш заказ отправлен сотрудникам.")

def register_order(dp: Dispatcher):
    dp.register_message_handler(order_cmd, commands=["order"])
    dp.register_message_handler(order_product, state=FSMOrder.product)
    dp.register_message_handler(order_quantity, state=FSMOrder.quantity)
    dp.register_message_handler(order_size, state=FSMOrder.size)
    dp.register_message_handler(order_contact, state=FSMOrder.contact)