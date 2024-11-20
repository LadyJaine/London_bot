from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
start_kb = ReplyKeyboardMarkup(
    keyboard=[
    [KeyboardButton(text='Price'),
     KeyboardButton(text='About us')
     ]
],resize_keyboard=True)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Medium game',callback_data='medium')],
        [InlineKeyboardButton(text='Large Game', callback_data='large')],
        [InlineKeyboardButton(text='Huge Game',callback_data='mega')],
        [InlineKeyboardButton(text='Other options', callback_data='other')]
    ]
)

product_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Viorgon_1',callback_data="product_buying")],
        [InlineKeyboardButton(text='Viorgon_3',callback_data="product_buying")],
        [InlineKeyboardButton(text='Viorgon_21',callback_data="product_buying")],
        [InlineKeyboardButton(text='Viorgon_28',callback_data="product_buying")],
    ]
)

buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Buy now!',url='https://zakupki.deti74.ru/')]])