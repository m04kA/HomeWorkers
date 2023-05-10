from telethon.sync import TelegramClient

import CONST

# Replace these with your own API_ID, API_HASH, and phone number.
api_id = CONST.api_id
api_hash = CONST.api_hash
phone_number = CONST.phone

# Create a regex pattern for URLs.
# url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
#
#
# def show_urls(events):
#     urls = []
#     for event in events:
#         if event.text:
#             urls += url_pattern.findall(event.text)
#     return urls
channel_id = 1218955142 # Юворк | вакансии и удалёнка

async def main():
    me = await client.get_me()
    # async for dialog in client.iter_dialogs():
    try:
        print('------------')
        async for message in client.iter_messages(channel_id, limit=10):  # Increase the limit if needed.
            print(f"{message.sender_id}: {message.text}")
            if message.id == 5285:
                try:
                    await client.forward_messages('https://t.me/m0sHe4kA', 5285, 1218955142)
                    print(f"Forwarded message with ID {message.text}")
                except Exception as e:
                    print(f"Failed to forward message with ID {5285}: {e}")
        # print(f"Checking chat \"{dialog.title}\"")
        # events = client.iter_messages(dialog.id, limit=10)  # You can increase this limit if needed
        # for event in events:
        #     if event.text:
        #         print(event.text + '\n')
        print('------------')
        # urls = await show_urls(events)
        # if urls:
        #     print(f'URLs in chat "{dialog.title}":')
        #     for url in urls:
        #         print(url)
        #     print("\n")
        # else:
        #     print(f"No URLs found in chat \"{dialog.title}\"\n")
    except Exception as exept:
        print("Cannot check the chat due to an error.", exept)


with TelegramClient(phone_number, api_id, api_hash) as client:
    client.loop.run_until_complete(main())