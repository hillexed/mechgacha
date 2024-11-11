import discord, dotenv
config = dotenv.dotenv_values(".env")

import time
import sys
import logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

import db 

from pulls import pull_command
import inventory
import regeneration

debug = False
prefix = 'm!'
version = '1'

if len(sys.argv) > 1:
    if sys.argv[1] == "debug":
        debug=True
        logging.info("Debug mode on!")
        prefix = 'd' + prefix

def user_is_admin(message):
    if "ADMIN_IDS" in config:
        if str(message.author.id) in config["ADMIN_IDS"].strip().split(","):
            return True
    return False




intents = discord.Intents(messages=True, message_content=True, guilds=True)
intents.reactions = True

client = discord.Client(intents=intents)
@client.event
async def on_ready():
    logging.info("The bot is ready!")

def get_command_body(message, command_name_to_remove):
    return message.content.replace(prefix + command_name_to_remove,"")


@client.event
async def on_message(message):
    if message.author == client.user or message.webhook_id is not None:
        return
    try:
        await handle_commands(message)
    except (Exception, KeyboardInterrupt) as e:
            await message.add_reaction('⚠️')
            logging.exception(e)
            raise e

async def handle_commands(message):
    if message.content.startswith(prefix + "pull"):
        message_body = get_command_body(message, "pull")
        await pull_command(message, message_body)

    elif message.content.startswith(prefix + "inventory"):

        message_body = get_command_body(message, "inventory")

        #if user_is_admin(message) and len(message_body) > 0 and "regenerate" in message_body:
        #    if "<@" in message_body and ">" in message_body:
        #        atted_userID = message_body.split("<@")[1].split(">")[0]
        #        db.delete_inventory_data(atted_userID)
        #        await message.channel.send("Their inventory is now:"+ inventory.represent_inventory_as_string(atted_userID))
        #        return
        #    return await message.channel.send("on a new line, @ someone.")
            
        #if user_is_admin(message) and len(message_body) > 0 and "debug_gift" in message_body:
        #    if "<@" in message_body and ">" in message_body:
        #        atted_userID = message_body.split("<@")[1].split(">")[0]
        #        inventory.give_random_gift(atted_userID)
        #        return
        #    else:
        #        inventory.give_random_gift(userID)

        if user_is_admin(message) and len(message_body) > 0 and "regen_everyone" in message_body:
            regeneration.regenerate_everyones_pulls()
            return await message.channel.send("Everyone's pulls have regenerated!")

        await inventory.inventory_command(message, get_command_body(message, "inventory"), client)

    elif message.content.startswith(prefix + "version"):
        await message.channel.send(str(version))

    elif message.content.startswith(prefix + "help"):
        pass
    #     await parse_help_command(message, get_command_body(message, "help"), client)


    elif message.content.startswith(prefix + "discordid"):
        logging.info(message.author.id) # you should only be able to access this if you're an admin

    elif user_is_admin(message) and message.content.startswith(prefix + "countservers"):
        servers = client.guilds
        await message.channel.send(f"{len(servers)}: {[(s.name, s.member_count) for s in servers]}")

    # ultra debug
    elif user_is_admin(message) and message.content.startswith(prefix + "downloadentiredb"):
        # this might hit the discord message filesize limit but it's an admin command so I don't care
        from db import _get_db_filename
        current_time_string = time.asctime(time.localtime()).lower()
        file = discord.File(_get_db_filename(), filename=f"glolf_{current_time_string.replace(' ','_')}.sqlite")
        await message.channel.send(f"Here's a copy of the DB at {current_time_string}", file=file)

# now run the bot
token = config["TOKEN"]
if debug:
    token = config["DEV_TOKEN"]


regeneration.start_timer()
client.run(token)
