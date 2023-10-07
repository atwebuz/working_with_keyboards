import logging
from loader import dp, bot
from aiogram.types import ContentType, Message
from pathlib import Path

# download_path = Path().joinpath("downloads", "categories") ## downloads ichidagai categories popka yoli
download_path = Path().joinpath("downloads") ## downloads path
download_path.mkdir(parents=True, exist_ok=True)

@dp.message_handler()
async def text_handler(message: Message):
    await message.reply("siz matn yubordiz")

@dp.message_handler(content_types=ContentType.DOCUMENT)
async def doc_handler(message: Message):
    await message.document.download(destination=download_path)
    doc_id = message.document.file_id
    await message.reply("siz hujjat yubordingiz\n"f"file_id = {doc_id}")

@dp.message_handler(content_types=ContentType.VIDEO)
async def videoc_handler(message: Message):
    await message.video.download(destination=download_path)
    await message.reply("siz video yubordingiz\n"f"vid_id = {message.video.file_id}")


@dp.message_handler(content_types=ContentType.PHOTO)
async def photo_handler(message: Message):
    await message.photo[-1].download(destination=download_path)
    await message.reply("siz rasm yubordingiz\n"f"file_id = {message.photo[-1].file_id}")

# lubboy faylni yuborish
@dp.message_handler(content_types=ContentType.ANY)
async def any_handler(message: Message):
    await message.reply(f"file_id = {message.content_type} qabul qilindi")