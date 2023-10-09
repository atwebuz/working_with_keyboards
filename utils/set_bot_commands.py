from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("shop", "Dokon"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("internation", "English school"),
            types.BotCommand("remove", "Remove bg of image"),
            
        ]
    )
