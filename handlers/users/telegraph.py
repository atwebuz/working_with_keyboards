import logging

from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.photo import menu_photo



from keyboards.default.start_menu_keyboard import menu_start
from utils import photo_link, remove_background

from loader import dp


@dp.message_handler(commands='remove')
async def bot_start(message: types.Message):
    logging.info(message)
    logging.info(f"{message.from_user.id=}")
    logging.info(f"{message.from_user.full_name=}")
    await message.answer(f"Salom, {message.from_user.full_name}!\nRasm yuboring va barxam oling )", reply_markup=ReplyKeyboardRemove())


photo_data = {}

@dp.message_handler(content_types='photo')
async def photo_handler(message: types.Message):
    photo = message.photo[-1]
    link = await photo_link(photo)
    await message.answer(link)
    new_photo = await remove_background(link)
    
    chat_id = message.chat.id
    photo_data[chat_id] = new_photo
    
    await message.answer("tanlang: ", reply_markup=menu_photo)

@dp.message_handler(text_contains='🌉 PHOTO')
async def send_photo_pic(message: types.Message):
    chat_id = message.chat.id
    new_photo = photo_data.get(chat_id)
    
    if new_photo:
        await message.reply_photo(new_photo, caption='🌉 Pic Background remove')
        await message.answer("photo")
    else:
        await message.answer("Rasm topilmadi")

        
@dp.message_handler(text_contains='📄 DOC')
async def send_photo_doc(message: types.Message):
    chat_id = message.chat.id
    
    new_photo = photo_data.get(chat_id)
    
    if new_photo:
        await message.reply_document(new_photo, caption='📄 Doc Background remove')
        await message.answer("document")
    else:
        await message.answer("Doc topilmadi")



