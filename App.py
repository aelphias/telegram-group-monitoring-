import asyncio
from telethon import TelegramClient, events, sync

# Replace with your own values
api_id = 123456
api_hash = '0123456789abcdef0123456789abcdef'
phone_number = '+1234567890'
username = 'your_username'
group_name = 'group_name'

# Create a client session with your account credentials
client = TelegramClient(username, api_id, api_hash)

# Define an event handler for new members joining the group
@client.on(events.ChatAction())
async def handle_action(event):
    if event.user_added:
        print(f"New member {event.user_added.username} joined the group.")

# Define an async main function to run the script
async def main():
    # Connect to the Telegram servers
    await client.start(phone=phone_number)
    # Join the group by its name
    group = await client.get_entity(group_name)
    await client.join_chat(group)
    # Start the event loop to handle incoming events
    await client.run_until_disconnected()

# Run the async main function
if __name__ == '__main__':
    asyncio.run(main())
