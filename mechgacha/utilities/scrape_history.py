import db
from datetime import datetime
import logging
import random
import re

import discord
import discord, dotenv
config = dotenv.dotenv_values(".env")

import time


intents = discord.Intents(messages=True, message_content=True, guilds=True)
intents.reactions = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    logging.info("T")
    await recover_playerdata()


lines = []

async def recover_playerdata():
    if (channel := client.get_channel(821802942419697736)) is None:
        logging.warning("Failed to fetch channel for funny joke")
        return

    pull_commanded = False
    userid = 0

    last_timestamp = datetime.fromisoformat("2024-11-06T21:13:24.153148")

    i = 0

    while True:

        print(f"Doing 100... {i}, {last_timestamp}")
        i += 1
        time.sleep(0.5)

        saw_messages = False

        async for message in channel.history(after=last_timestamp, oldest_first=True):
            saw_messages = True

            userid = message.author.id
            msg = message.content
            last_timestamp = message.created_at # a datetime object

            lines.append(f"🌒{userid}🌓{message.created_at}🌓{msg}\n")

        if not saw_messages:
            print("End of the line!")
            break

    with open("logs.txt", 'w') as f:
        f.writelines(lines)


# now run the bot
token = config["TOKEN"]
client.run(token)
