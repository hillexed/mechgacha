import discord, dotenv
config = dotenv.dotenv_values(".env")

import time
from datetime import datetime
import sys
import logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

import db 

from pulls import pull_command
import inventory
import regeneration
import equip
import tradecommand
import progress
import scrap
import event
import sleepy

debug = False
prefix = 'm!'
version = '2.1'

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
    await sleepy.wakeup_command(client, prefix)

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
        # update last used channel
        db.update_data("last_channel", message.channel.id, "stats")

    elif message.content.startswith(prefix + "shuck"):
        message_body = get_command_body(message, "shuck")
        await pull_command(message, message_body)
        # update last used channel
        db.update_data("last_channel", message.channel.id, "stats")

    elif message.content.startswith(prefix + "inv"):

        message_body = get_command_body(message, "inv")
        if message.content.startswith(prefix + "inventory"):
            message_body = get_command_body(message, "inventory")
        

        #if user_is_admin(message) and len(message_body) > 0 and "regenerate" in message_body:
        #    if "<@" in message_body and ">" in message_body:
        #        atted_userID = message_body.split("<@")[1].split(">")[0]
        #        db.delete_inventory_data(atted_userID)
        #        await message.channel.send("Their inventory is now:"+ inventory.represent_inventory_as_string(atted_userID))
        #        return
        #    return await message.channel.send("on a new line, @ someone.")

            
        if user_is_admin(message) and len(message_body) > 0 and "debug_add" in message_body:
            print(message_body)
            if "<@" in message_body and ">" in message_body:
                atted_userID = message_body.split("<@")[1].split(">")[0]
            else:
                return await message.channel.send("at a user to use this debug command")

            item_name = message_body.replace("debug_add","").replace(f"<@{atted_userID}>","")

            item_id = inventory.match_item_name_to_id(item_name)
            inventory.add_id_to_inventory(item_id, atted_userID)
            return await message.channel.send(f"added {item_id} to em")
            
        if user_is_admin(message) and len(message_body) > 0 and "accept_bribe" in message_body:
            print(message_body)
            if "<@" in message_body and ">" in message_body:
                atted_userID = message_body.split("<@")[1].split(">")[0]
                regeneration.add_pulls(atted_userID, 1, 0.5)
            else:
                regeneration.add_pulls(userID, 1, 0.5)
            return await message.channel.send("thank you very much")

        if user_is_admin(message) and len(message_body) > 0 and "regen_everyone" in message_body:
            regeneration.regenerate_everyones_pulls()
            return await message.channel.send("Everyone's pulls have regenerated!")

        await inventory.inventory_command(message, message_body, client)
   
    elif message.content.startswith(prefix + "mech equip"):
        await equip.equip_command(message, get_command_body(message, "mech equip"), client)

    elif message.content.startswith(prefix + "scrap"):
        await scrap.scrap_command(message, get_command_body(message, "scrap"), client)
    
    elif message.content.startswith(prefix + "recycle"): # alias
        await scrap.scrap_command(message, get_command_body(message, "recycle"), client)
    
    elif message.content.startswith(prefix + "mech unequip"):
        await equip.unequip_command(message, get_command_body(message, "mech unequip"), client)

    elif message.content.startswith(prefix + "mech sources"):
        await equip.mech_command(message, get_command_body(message, "mech sources"), client, include_sources=True)

    # shortcuts for m!mech equip and m!mech unequip
    elif message.content.startswith(prefix + "equip"):
        await equip.equip_command(message, get_command_body(message, "equip"), client)
    
    elif message.content.startswith(prefix + "unequip"):
        await equip.unequip_command(message, get_command_body(message, "unequip"), client)

    elif message.content.startswith(prefix + "mech short"):
        await equip.mech_command(message, get_command_body(message, "mech short"), client, short=True)

    elif message.content.startswith(prefix + "mech"):
        await equip.mech_command(message, get_command_body(message, "mech"), client)

    elif message.content.startswith(prefix + "trade"):
        await tradecommand.trade_command(message, get_command_body(message, "trade"), client)

    elif message.content.startswith(prefix + "progress"):
        await progress.progress_command(message, get_command_body(message, "progress"))

    elif message.content.startswith(prefix + "event claim"):
        await event.event_claim_command(message)

    # elif message.content.startswith(prefix + "event clam"):
    #    await event.clam(message)

    elif message.content.startswith(prefix + "event"):
        message_body = get_command_body(message, "event")
        if user_is_admin(message) and "debug_add" in message_body:
            if "<@" in message_body and ">" in message_body:
                atted_userID = message_body.split("<@")[1].split(">")[0]
                return await event.debug_add_gift(message, atted_userID)
            else:
                return await message.channel.send("@ a user to use!")

        else:
            await event.event_info_command(message)

    elif message.content.startswith(prefix + "wakeup"):
        await message.channel.send("ok ok im up")


    elif message.content.startswith(prefix + "version"):
        await message.channel.send(str(version))

    elif message.content.startswith(prefix + "help"):
        await message.channel.send(
"""Command list:
`m!pull` - Get new items and mechs from the gacha
`m!inventory` - Check the mecha parts you have.
- If there are too many parts to display in one page, use a number to look through pages of your inventory.
- Optional: `m!inventory legs` will only show legs parts.
- Optional: `m!inventory unequipped` will only show items that are not equipped to your mech.
`m!mech` - Equip or unequip items from your inventory to build a mecha!
- `m!mech equip/unequip <part name or slot number>`
- `m!mech sources` - see which mechs your equipped items came from
`m!trade` - Trade parts with other users
`m!progress <mech name>` - See how many parts you have collected from a specific mech
`m!scrap` - Get rid of unwanted items. Scrap is recycled into free pulls.
`m!event` - See info about ongoing events.
- `m!event claim` - Claim any currently active event gifts.
""")
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
        file = discord.File(_get_db_filename(), filename=f"mechgacha_{current_time_string.replace(' ','_')}.sqlite")
        await message.channel.send(f"Here's a copy of the DB at {current_time_string}", file=file)

    elif user_is_admin(message) and message.content.startswith(prefix + "time"):
        logging.info(datetime.fromisoformat(db.get_data("last_time", tablename="stats")))

    # update time from last recorded message
    db.update_data("last_time", datetime.now().isoformat(), "stats")

if __name__ == "__main__":
    token = config["TOKEN"]
    if debug:
        token = config["DEV_TOKEN"]
    regeneration.start_timer()

    try:
        client.run(token, log_level=logging.INFO)
    except Exception as e:
        logging.error("Received exception: ")
        logging.exception(e)
    logging.info("Shutting down")
