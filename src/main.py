from telethon import events
from telethon.sync import TelegramClient

import CONST
from internal.copyright_direction import is_copyright_UWORK, is_smm_UWORK, is_design_UWORK

# Replace these with your own API_ID, API_HASH, and SESSION_NAME number.
API_ID = CONST.API_ID
API_HASH = CONST.API_HASH
SESSION_NAME = CONST.SESSION_NAME
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)


async def main():
    await client.start()
    me = await client.get_me()
    entity = await client.get_entity(CONST.UVORK_CHANNEL_ID)

    @client.on(events.NewMessage(chats=[entity]))
    async def message_listener(event):
        navigate_message = ''
        message_text = event.message.message
        message_id = event.message.id
        print(f'UWORK new message; id={message_id}')
        navigate_message += is_copyright_UWORK(message_text)
        navigate_message += is_smm_UWORK(message_text)
        navigate_message += is_design_UWORK(message_text)
        if navigate_message:
            print(f'\n\nNew orders; Navigations={navigate_message}\n\n')
            try:
                await client.send_message(CONST.HOMEWORK_CHANNEL_ID, navigate_message)
                await client.forward_messages(CONST.HOMEWORK_CHANNEL_ID, message_id, CONST.UVORK_CHANNEL_ID)
            except Exception as err:
                print(f"Failed to forward message from UWORK: {err}")

    print(f"Listening for messages in the chat: UWORK")

    # Keep the script running forever
    await client.run_until_disconnected()


if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())
        # await client.disconnect()
