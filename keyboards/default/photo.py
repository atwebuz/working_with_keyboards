from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_photo = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🌉 PHOTO'),
            KeyboardButton(text='📄 DOC'),
        ],
    ],
    resize_keyboard=True,
)

