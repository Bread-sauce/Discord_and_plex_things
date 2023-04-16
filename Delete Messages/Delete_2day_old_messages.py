import discord
import asyncio
import datetime
import pytz
import schedule

TOKEN = 'discord token goes here'
CHANNEL_ID = 'channel id goes here'
TIMEZONE = 'timezone goes here'  # example: 'US/Eastern'

intents = discord.Intents().all()
intents.members = True
client = discord.Client(intents=intents)

async def delete_messages():
    channel = client.get_channel(int(CHANNEL_ID))
    now = datetime.datetime.now(pytz.timezone(TIMEZONE))
    two_days_ago = now - datetime.timedelta(days=2)

    async for message in channel.history(limit=None):
        if not message.pinned and message.created_at < two_days_ago:
            await message.delete()
            await asyncio.sleep(1)

def delete_messages_job():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(delete_messages())

def schedule_delete_messages():
    schedule.every().day.at('06:00').do(delete_messages_job)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    schedule_delete_messages()

if __name__ == '__main__':
    schedule_delete_messages()
    client.run(TOKEN)
