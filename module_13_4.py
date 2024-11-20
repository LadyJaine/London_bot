from aiogram import Bot,Dispatcher,executor,types
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

API = '7644570710:AAHlkQaeYgq43y5LR0gAsDeW6kc1C-9OaPk'
bot = Bot(token = API)
dp = Dispatcher(bot,storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text = 'Calories')
async def set_age(message):
    await message.answer('Введите свой возраст в годах:')

    await UserState.age.set()
@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(first=message.text)
    date = await state.get_data()
    await message.answer('Введите свой рост в см:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(second=message.text)
    date = await state.get_data()
    await message.answer('Введите свой вес в кг:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(third=message.text)
    date = await state.get_data()
    result = (int(date["third"]) * 10) + (6.25 * int(date["second"])) - (5 * int(date["first"])) + 5
    await message.answer(f'Ваша норма калорий: {result}')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
