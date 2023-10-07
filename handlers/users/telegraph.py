from aiogram import types

from loader import dp
from utils import photo_link
# from utils import remove_background

@dp.message_handler(content_types='photo')
async def photo_handler(msg: types.Message):
    photo = msg.photo[-1]
    link = await photo_link(photo)
    await msg.answer(link)