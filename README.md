# Discord_things
Stuff for discord, some fun stuff and some plex stuff.\
You will need a discord bot and its token.\
All scripts are writing in python.

### delete_all_messages_in_a_channel.py
This will delete all messages in a channel except pinned.\
Made this to bypass the 14day limit on bots deleting messages.

### Delete_2day_old_messages.py
This will run once a day to delete messages that are older than 2 days except pinned.\
I use this to clear out my plex show request channel.

### MemeBots
Discord meme bot This bot will respond to any message in discord with a meme for the subreddit "memes" top 50 from hot.
membot_list_of_subreddits_hot100.py is newest iteration, it will take a while for first meme to appear but after that its super fast

### Add tags based on codec
This was created to solve and issue of trying to mass encode av1 movies and have a fallback if there was an issue so I could redownload if encoding went wrong.

### add_to_4k_radarr_if_watched.py - tautulli script
Created to add movies that are in 1080p to my 4k radarr.
Add "{title} {library_name}" to arguments in tautulli scripts

