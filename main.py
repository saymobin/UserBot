import logging
logging.basicConfig(format='[%(levelname) %(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

from telethon import TelegramClient, events
import time

api_id = 

api_hash = ''
session = ''

client = TelegramClient(session, api_id, api_hash)

# async def main():
#     await client.send_message("drugger3385", "hola2")
# with client:
#     client.loop.run_until_complete(main())

@client.on(events.NewMessage)
async def handler(event):
    chat = await event.get_chat()
    sender = await event.get_sender()
    chat_id = event.chat_id
    sender_id = event.sender_id
    print(f'{sender_id}')
    # await time.sleep(2)
    await event.reply("سلام")

client.start()
client.run_until_disconnected()
