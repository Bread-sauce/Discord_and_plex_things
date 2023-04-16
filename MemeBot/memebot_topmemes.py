import discord
from discord.ext import commands
import asyncpraw
import asyncio
import random

# Create a new Discord client
intents = discord.Intents().all()
intents.members = True
client = discord.Client(intents=intents)

# Store the list of submissions globally
submission_list = []

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # meme me daddy
    if not submission_list:
        reddit = asyncpraw.Reddit(
            client_id="REDDIT ID GOES HERE",
            client_secret="REDDIT SECRET GOES HERE",
            user_agent="Discord_bot",
            aiohttp_kwargs={"timeout": 10},
        )

        subreddit = await reddit.subreddit("memes")
        async for submission in subreddit.top(limit=300):
                submission_list.append(submission)
    await message.channel.send(random.choice(submission_list).url)

# Run the bot
client.run('DISCORD TOKEN GOES HERE')
