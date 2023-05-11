from telethon import TelegramClient

# Use your own values from my.telegram.org
API_ID = 12345
API_HASH = '0123456789abcdef0123456789abcdef'

# The first parameter is the .session file name (absolute paths allowed)
with TelegramClient('anon', API_ID, API_HASH) as client:
    client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))