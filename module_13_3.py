from aiogram import Bot,Dispatcher,executor,types
import asyncio

from aiogram.contrib.fsm_storage.memory import MemoryStorage
api = '7644570710:AAHlkQaeYgq43y5LR0gAsDeW6kc1C-9OaPk'
bot = Bot(token = api)
dp = Dispatcher(bot,storage = MemoryStorage())

@dp.message_handler(commands=['start'])
async def all_massages(message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer('You are cute!')
@dp.message_handler()
async def start(message):
    print('Привет! Я бот помогающий твоему English.')
    await message.answer('We are happy to see you in this bot!')


if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)