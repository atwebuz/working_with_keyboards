import logging
from loader import dp, bot
from aiogram.types import ContentType, Message, InputFile
from pathlib import Path



@dp.message_handler(content_types=ContentType.VIDEO)
async def videoc_handler(message: Message):
    await message.reply("siz video yubordingiz\n"f"vid_id = {message.video.file_id}")


@dp.message_handler(content_types=ContentType.PHOTO)
async def photo_handler(message: Message):
    await message.reply("siz rasm yubordingiz\n"f"file_id = {message.photo[-1].file_id}")

# lubboy faylni yuborish
@dp.message_handler(commands="kitob")
async def any_handler(message: Message):
    photo_id = 'AgACAgIAAxkBAAIBOGUhz_1b3jgHTNaMv1NVHvSjwmJnAAIw0DEbSk4QSfF5z1PlPODRAQADAgADeAADMAQ' ## sending image with unique id qachonki magazom boladgan bosa qule boladi
    photo_url = 'https://telegra.ph//file/b321d373bee43a2c29c0f.jpg' ## sending image with url xotiradan joy omasin dse qule
    photo_device = InputFile(path_or_bytesio='photos/img.jpg') ## sending image from device
    await message.reply_photo(photo_device, caption="reply image caption")
    await message.answer_photo(photo_id, caption="answer image caption")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_url, caption="send bot.id")