import discord
import asyncio

TOKEN = 'token goes here'
CHANNEL_ID = 'channel id goes here'

intents = discord.Intents().all()
intents.members = True
client = discord.Client(intents=intents)

async def delete_messages():
    channel = client.get_channel(int(CHANNEL_ID))

    async for message in channel.history(limit=None):
        if not message.pinned:
            await message.delete()
            await asyncio.sleep(1)

async def main():
    while True:
        await delete_messages()
        await asyncio.sleep(60) # Wait for 60 seconds before restarting the loop

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

    # Start the loop
    client.loop.create_task(main())


if __name__ == '__main__':
    client.run(TOKEN)