from aiogram import Bot,Dispatcher,executor,types
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
import texts

API = '7644570710:AAHlkQaeYgq43y5LR0gAsDeW6kc1C-9OaPk'
bot = Bot(token = API)
dp = Dispatcher(bot,storage=MemoryStorage())


start_bar = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Рассчитать'),
                                          KeyboardButton(text='Информация'),
                                          KeyboardButton(text='Купить')]],resize_keyboard=True)
kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий',callback_data='calories')],
        [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
        ])


product_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Viorgon_1',callback_data="product_buying")],
        [InlineKeyboardButton(text='Viorgon_3',callback_data="product_buying")],
        [InlineKeyboardButton(text='Viorgon_21',callback_data="product_buying")],
        [InlineKeyboardButton(text='Viorgon_28',callback_data="product_buying")],
    ]
)

@dp.message_handler(commands =['start'])
async def main_menu(message):
    await message.answer(f"Привет, {message.from_user.username}! Я бот помогающий твоему здоровью.",reply_markup=start_bar)



@dp.message_handler(text='Купить')
async def get_buying_list(message):
    os.chdir(r'C:\Users\Евгения\PycharmProjects\Module_13_asinc\files')
    file = [f for f in os.listdir() if os.path.isfile(f)]

    for i in range(4):
        with open(file[i], 'rb') as photo:
            await message.answer(f'Название: Product{i+1} | Описание: описание {i+1} | Цена: {(i+1)* 100} ')
            await message.answer_photo(photo)
    await message.answer("Выберите продукт для покупки:",reply_markup=product_kb)
@dp.message_handler(text='Рассчитать')
async def mainmenu(message):
    await message.answer('Выберите опцию',reply_markup=kb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer("Формула расчета для женщин:10 x вес (кг)"
                              " + 6,25 x рост (см) – 5 x возраст (г) – 161")
    await call.answer()

@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.callback_query_handler(text = 'calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст в годах:')
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