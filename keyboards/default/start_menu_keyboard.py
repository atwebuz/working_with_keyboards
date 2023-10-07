from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🛍️ Mahsulotlar'),
            KeyboardButton(text='ℹ️Qoʼllanma'),
            KeyboardButton(text='Yopish'),
        ],
    ],
    resize_keyboard=True,
)


menu_register = ReplyKeyboardMarkup(
    keyboard=[
          [
            KeyboardButton(text='Contact', request_contact=True),
            KeyboardButton(text='Location', request_location=True),
        ],
    ],
    resize_keyboard=True,
)
