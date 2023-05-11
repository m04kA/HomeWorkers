from telethon.sync import TelegramClient

import CONST

# Replace these with your own API_ID, API_HASH, and SESSION_NAME number.
API_ID = CONST.API_ID
API_HASH = CONST.API_HASH
SESSION_NAME = CONST.SESSION_NAME
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)


async def main():
    me = await client.get_me()
    try:
        async for dialog in client.iter_dialogs():
            if dialog.name:
                print(f'{dialog.name}')
            else:
                print('No dialog title')
            if dialog.entity:
                print(f'Channel_id = {dialog.entity.id}')
            print('------------')
        await client.disconnect()

    except Exception as exept:
        print("Cannot check the chat due to an error.", exept)


if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())