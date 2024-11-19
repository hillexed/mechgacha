from math import ceil, floor
import db
import random
import json
import logging

from gacha_tables import all_parts_list, starting_inventory

import asyncio

from data_utils import get_playerdata


def add_new_player(userid):
    inventory = starting_inventory
    db.set_inventory_data(userid, inventory)

    playerdata = {"unlocked_mechs": [], 'ratoon_pulls':2, 'mech_pulls': 5, 'equipment': []}
    db.set_player_data(userid, playerdata)

def compute_inventory(userid):
    inventory = db.get_inventory_data(userid)
    if inventory is not None:
        pass
        # inventory = json.loads(inventory)
    else: # not in DB
        add_new_player(userid)
    return inventory

def remove_from_inventory(userid, thing_to_remove):
    inventory = db.get_inventory_data(userid)
    if inventory is not None:
        pass
        # inventory = json.loads(inventory)
    else: # not in DB
        raise ValueError("Userid not in inventory DB!")

    if thing_to_remove in inventory:
        inventory.remove(thing_to_remove)
        db.set_inventory_data(userid, json.dumps(inventory))
    else:
        raise ValueError("Thing not in user's inventory in DB!")
        


def give_random_gift(userid):
    inventory = db.get_inventory_data(userid)
    if inventory is not None:
        inventory = json.loads(inventory)
    else: # not in DB
        inventory = []
    inventory.append(generate_random_gift()) # give someone new a welcome gift!
    db.set_inventory_data(userid, json.dumps(inventory))
    logging.info(f"Gave userid {userid} a random gift")


def represent_inventory_as_string(inventory, playerdata, page=1):

    if inventory is None or len(inventory) == 0:
        return "**You have nothing in your inventory!** \n Use m!pull ratoon to get some mechs from Ratoon's gachapon, then m!pull <mech> to pull from their list!"

    prefix = "**Your inventory:**\n"

    # pagination for when inventory gets big
    page_size = 8
    page -= 1 #first page should be page 1, not page 0
    items_to_display = inventory[page * page_size : (page+1) * page_size]

    if len(inventory) > page_size:
        prefix += f"(Page {page+1}/{ceil(len(inventory) / page_size)})\n"

    if len(inventory) == 0:
        return prefix + "Empty!"


    return prefix + '\n'.join([
    format_item(
        item_id, 
        (item_index + (page_size * page)), 
        (item_index + (page_size * page)) in playerdata["equipment"])
    for item_index, item_id in enumerate(items_to_display)])

def format_item(item_id, item_index = -1, equipped = False):

    new_line = "\n"
    sub_array = []
    item_data = all_parts_list[item_id]

    if item_index > -1:
        sub_array.append(f"[{item_index + 1}]") 

    tags_string = f'{", ".join([tag.upper() for tag in item_data.tags])}'
    if len(item_data.tags) > 0:
        sub_array.append(tags_string)
    
    if equipped:
        sub_array.append("**EQUIPPED**")

    sub_line = f'{new_line}-# **     **{" • ".join(sub_array)}'
    return f'- {item_data.name} {"★" * item_data.stars} - {item_data.description}{sub_line if len(tags_string) > 0 or item_index > -1 else ""}'

async def inventory_command(message, message_body, client):
    userid = message.author.id

    username = message.author.display_name.lower() # I'd love to use global_name but it doesn't work.

    playerdata = get_playerdata(userid)


    if not "equipment" in playerdata:
        playerdata["equipment"] = []
        db.set_player_data(userid, playerdata)

    try:
        page = int(message_body.strip())
    except:
        page = 1 # page 1 is the first page

    if page <= 0:
        return await message.channel.send("There ain't no such page of your inventory")

    inventory = compute_inventory(userid)

    if inventory is None:
        # player has no inventory!
        add_new_player(userid)
        inventory = compute_inventory(userid)

    return await message.channel.send(represent_inventory_as_string(inventory, playerdata, page))


def get_first_item_of_type(userid, type):
    inv = compute_inventory(userid)
    for item in inv:
        if item["type"] == type:
            return item
    return None
    
def give_gift_to_empty_inventories():
    # admin command. very laggy because it's done as many individual DB hits instead of one big commit
    users = db.get_users_with_empty_inventory()
    for userid in users:
        give_random_gift(userid)
        
def give_gift_to_everyone():
    # admin command. very laggy because it's done as many individual DB hits instead of one big commit
    users = db.get_all_users_with_any_inventory()
    for userid in users:
        give_random_gift(userid)
