import CONST
from telethon import events
from telethon.sync import TelegramClient

SESSION_NAME = CONST.SESSION_NAME
API_ID = CONST.API_ID
API_HASH = CONST.API_HASH
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

async def main():
    await client.start()
    me = await client.get_me()

    # Get the channel or chat using its username or invite link
    entity = 'https://t.me/m0sHe4kA'  # Replace with the subject's username or invite link
    entity = await client.get_entity(entity)

    # Set up the listener for new messages in the specific chat
    @client.on(events.NewMessage(chats=[entity]))
    async def message_listener(event):
        sender = await event.get_sender()
        print(f"{sender.first_name}: {event.text}")
        await client.send_message('https://t.me/m0sHe4kA', f"{sender.first_name}: {event.text}")

    print(f"Listening for messages in the chat: https://t.me/m0sHe4kA")

    # Keep the script running forever
    await client.run_until_disconnected()

# with client:
#     client.loop.run_until_complete(main())

# async def main():
#     await client.start()
#     me = await client.get_me()
#     entity = 'https://t.me/rueventjob'
#     # Get the channel or chat using its username or invite link
#     # entity = 'https://t.me/m0sHe4kA'  # Replace with the subject's username or invite link
#     entity = await client.get_entity(entity)
#
#     # Retrieve messages from the subject (channel, chat or private conversation)
#     messages = await client.get_messages(entity, limit=10)  # Get the last 100 messages
#
#     for message in messages:
#         print(f'\n {message.sender_id}: {message.text}\n')

with client:
    client.loop.run_until_complete(main())
