#main.py
"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types

from weather import get_weather

API_TOKEN = '6430088203:AAHtw_E0_G67oJfjeDMUINlA_0V1PNdASr8'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    print('message: ', message)
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler() # London
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    try:
        weather = get_weather(message.text)
        await message.reply(f"Temperature: {weather['main'].get('temp')}\n"
                            f"Wind speed: {weather['wind'].get('speed')}\n"
                            f"Wind direction: {weather['wind'].get('deg')}\n"
                            f"Pressure: {weather['main'].get('pressure')}\n"
                            f"Humidity: {weather['main'].get('humidity')}\n"
                            f"Description: {weather['weather'][0].get('description')}\n"
                            )
    except Exception as e:
        await message.reply(f"Error: {e}")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)