#pylint:disable=C0114
import logging
import os
from pyrogram import Client
from pyrogram.errors import RPCError
from pyrogram.errors import BadRequest
# import asyncio
# from pyrogram.errors import FloodWait
# from pyrogram.handlers import MessageHandler
# os.environ['TZ'] = 'Asia/Kolkata'



logging.basicConfig(level=logging.INFO)



bot = Client(
    'bot',
    api_id= 6690144, #get it from https://my.telegram.org/auth
    api_hash="be8e6aed33f43925819ba03044876a17", #get it from https://my.telegram.org/auth
    bot_token="5192319960:AAF_inLs7Jgh3wtjFX0EAzgM6XoHP9uCal0", #get it from @Botfather
    plugins=dict(root="plugins"),
    parse_mode="html")


try:
    bot.run()
except Exception as e:
    print(e)
        
