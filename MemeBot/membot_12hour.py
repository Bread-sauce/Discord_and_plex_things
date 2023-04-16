import discord
from discord.ext import commands
import asyncpraw
import asyncio
import random
import time

# Create a new Discord client
intents = discord.Intents().all()
intents.members = True
client = discord.Client(intents=intents)

# Store the list of submissions globally
submission_list = []
# Timestamp of when the code was last reset
last_reset = time.time()
# List of subreddits to pull memes from
subreddit_list = ["memes","dankmemes","meirl","dndmemes","Animemes","bonehurtingjuice","PrequelMemes"]

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # meme me daddy
    # Check if 12 hours has passed since the last reset
    global last_reset
    global submission_list
    if time.time() - last_reset >= 43200:
        # Reset the list of submissions and the timestamp
        submission_list = []
        last_reset = time.time()
    if not submission_list:
        reddit = asyncpraw.Reddit(
            client_id="REDDIT ID GOES HERE",
            client_secret="REDDIT SECRET GOES HERE",
            user_agent="Discord_bot",
            aiohttp_kwargs={"timeout": 10},
        )
        for sub_reddit in subreddit_list:
            subreddit = await reddit.subreddit(sub_reddit)
            async for submission in subreddit.hot(limit=100):
                if submission.thumbnail:
                    submission_list.append(submission)
    
    #sends url to discord
    await message.channel.send(random.choice(submission_list).url)

# Run the bot
client.run('DISCORD TOKEN GOES HERE')
