import logging
from loader import dp, bot
from aiogram.types import ContentType, Message

@dp.message_handler()
async def text_handler(message: Message):
    await message.reply("siz matn yubordiz")

@dp.message_handler(content_types=ContentType.DOCUMENT)
async def doc_handler(message: Message):
    await message.document.download()
    doc_id = message.document.file_id
    await message.reply("siz hujjat yubordingiz\n"f"file_id = {doc_id}")