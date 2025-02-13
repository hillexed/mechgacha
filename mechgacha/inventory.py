from collections import Counter
from collections.abc import Sequence
from dataclasses import dataclass
from math import ceil, floor
from typing import Optional
import random
import json
import logging
import asyncio
from fuzzywuzzy import process

import db
from gacha_tables import all_parts_list, starting_inventory
from data_utils import get_playerdata, paginate

def add_new_player(userid):
    inventory = starting_inventory
    db.set_inventory_data(userid, inventory)

    playerdata = {"unlocked_mechs": [], 'ratoon_pulls':2, 'mech_pulls': 5, 'equipment': [], "scrap": 0}
    db.set_player_data(userid, playerdata)

def compute_inventory(userid):
    inventory = db.get_inventory_data(userid)
    if inventory is not None:
        pass
        # inventory = json.loads(inventory)
    else: # not in DB
        add_new_player(userid)
    return inventory



all_item_names = [all_parts_list[itemid].name for itemid in all_parts_list]
name_to_id = {all_parts_list[itemid].name: itemid for itemid in all_parts_list}
def match_item_name_to_id(name):
    chosen_item_name, closeness = process.extractOne(name, choices=all_item_names)

    return name_to_id[chosen_item_name]

def item_already_in_inventory(new_item, inventory):
    return new_item in inventory

def add_id_to_inventory(new_item_id, userid):
    inv = db.get_inventory_data(userid)

    if inv is None:
        inv = starting_inventory

    inv.append(new_item_id)
    db.set_inventory_data(userid, inv)

def add_to_inventory(new_item, userid):
    add_id_to_inventory(new_item.id, userid)

def trade(userid1, item_id_to_trade1, userid2, item_id_to_trade2):
    inventory1 = db.get_inventory_data(userid1)
    inventory2 = db.get_inventory_data(userid2)

    item1 = all_parts_list[item_id_to_trade1]
    item2 = all_parts_list[item_id_to_trade2]

    if item1.id not in inventory1:
        raise ValueError("User #1 doesn't have the item {item1.id}")
    if item2.id not in inventory2:
        raise ValueError("User #2 doesn't have the item {item2.id}")

    remove_from_inventory(item1.id, userid1)
    add_id_to_inventory(item1.id, userid2)
    remove_from_inventory(item2.id, userid2)
    add_id_to_inventory(item2.id, userid1)
        

def remove_from_inventory_by_position(index_to_remove, userid):
    inventory = db.get_inventory_data(userid)
    if inventory is not None:
        pass
        # inventory = json.loads(inventory)
    else: # not in DB
        raise ValueError("Userid not in inventory DB!")

    if index_to_remove < 0 or index_to_remove >= len(inventory):
        raise ValueError("Array index out of bounds!")

    # first deal with equipped items
    # unequip this item if it's equipped
    playerdata = db.get_player_data(userid)

    if index_to_remove in playerdata["equipment"]:
        playerdata["equipment"].remove(index_to_remove)
        
    # if we delete item #3, any "equipped item at index 4" should now read "equipped item at index 3"
    for i in range(len(playerdata["equipment"])):
        item_index = playerdata["equipment"][i]
        if item_index > index_to_remove:
            playerdata["equipment"][i] -= 1 
    db.set_player_data(userid, playerdata)

    # now remove item from inventory
    del inventory[index_to_remove]
    db.set_inventory_data(userid, inventory)
    

def remove_from_inventory(item_id_to_remove, userid):
    inventory = db.get_inventory_data(userid)
    if inventory is not None:
        pass
        # inventory = json.loads(inventory)
    else: # not in DB
        raise ValueError("Userid not in inventory DB!")

    if item_id_to_remove in inventory:
        deleted_item_index = inventory.index(item_id_to_remove)
        remove_from_inventory_by_position(deleted_item_index, userid)
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


page_size = 6 # max 

def represent_inventory_as_string(inventory: Sequence[tuple[int, int]], playerdata, page=1, short=False):
    if inventory is None or len(inventory) == 0:
        return "**You have nothing in your inventory!** \n Use m!pull ratoon to get some mechs from Ratoon's gachapon, then m!pull <mech> to pull from their list!"

    prefix = "**Your inventory:**\n"

    # pagination for when inventory gets big
    page -= 1 #first page should be page 1, not page 0
    items = inventory
    if short:
        items = [(sub[1], sub[0]) for sub in Counter([item[1] for item in inventory]).items()]
    pages = paginate(
                [format_item(
                    item_id, 
                    item_index if not short else -1,
                    item_index in playerdata["equipment"] if not short else False,
                    short, 
                    1 if not short else item_index)
                    for (item_index, item_id) in items],
                1500)


    if page >= len(pages):
        # if requesting page 4 of a 3-page inventory, say
        # just show the last page
        page = len(pages) - 1

    if len(inventory) > page_size:
        prefix += f"(Page {page+1}/{len(pages)})\n"

    if len(inventory) == 0:
        return prefix + "Empty!"
        

    
    return prefix + '\n'.join(pages[page])

def format_item(item_id, item_index = -1, equipped = False, short = False, count = 1):

    new_line = "\n"
    sub_array = []
    item_data = all_parts_list[item_id]

    if item_index > -1 and not short:
        sub_array.append(f"`[{item_index + 1}]`") 

    tags_string = f'{", ".join([tag.upper() for tag in item_data.tags])}'
    if len(item_data.tags) > 0:
        sub_array.append(tags_string)

    if equipped and not short:
        sub_array.append("**EQUIPPED**")

    stars_string = "☆☆☆" if stars == 0 else "★" * item_data.stars
    if short:
        count_string = f' (__x{count}__)'
        sub_line = f'{ count_string if count > 1 else ""} | `{" • ".join(sub_array)}`'
        return f'- {item_data.name} {stars_string}{sub_line if len(tags_string) > 0 else ""}'
    else:
        sub_line = f'{new_line}-# **     **{" • ".join(sub_array)}'
        return f'- {item_data.name} {stars_string} - {item_data.description}{sub_line if len(tags_string) > 0 or item_index > -1 else ""}'

async def inventory_command(message, message_body, client):
    userid = message.author.id

    username = message.author.display_name.lower() # I'd love to use global_name but it doesn't work.

    playerdata = get_playerdata(userid)


    if not "equipment" in playerdata:
        playerdata["equipment"] = []
        db.set_player_data(userid, playerdata)

    parsed_message = parse_message(message_body)

    tag = parsed_message.tag
    include_equipped = parsed_message.include_equipped
    number_of_stars = parsed_message.number_of_stars
    page = parsed_message.page
    short = parsed_message.short

    if page <= 0:
        return await message.channel.send("There ain't no such page of your inventory")

    inventory = compute_inventory(userid)

    if inventory is None:
        # player has no inventory!
        add_new_player(userid)
        inventory = compute_inventory(userid)

    inventory_with_index = list(enumerate(inventory))

    if not include_equipped:
        equipment = playerdata["equipment"]
        inventory_with_index = [(item_index, item_id) for (item_index, item_id) in inventory_with_index if item_index not in equipment]

    if tag is not None:
        all_users_tags = set(tag for item_id in inventory for tag in all_parts_list[item_id].tags)
        chosen_tag, closeness = process.extractOne(tag, all_users_tags)
        if closeness < 85:
            return await message.channel.send(f"Couldn't find any {tag} in your inventory. Maybe you typoed? ")
        inventory_with_index = [(item_index, item_id) for (item_index, item_id) in inventory_with_index if chosen_tag in all_parts_list[item_id].tags]

    if number_of_stars is not None:
        inventory_with_index = [(item_index, item_id) for (item_index, item_id) in inventory_with_index if number_of_stars == all_parts_list[item_id].stars]
        if len(inventory_with_index) == 0:
            return await message.channel.send(f"Nothin in your inventory with {number_of_stars} stars and also the other stuff ya mentioned")

    return await message.channel.send(represent_inventory_as_string(inventory_with_index, playerdata, page, short))

@dataclass
class ParsedMessage:
    tag: Optional[str] = None
    include_equipped: bool = True
    number_of_stars: Optional[int] = None
    short: bool = False
    page: int = 1

def parse_message(message_body) -> ParsedMessage:
    # inventory
    # inventory 2
    # inventory legs
    # inventory cockpits 3
    # inventory unequipped
    # inventory unequipped 2
    # inventory unequipped cockpits
    # inventory unequipped cockpits 3
    # inventory 2 stars
    # inventory 2 stars 3
    # inventory legs 2 stars
    # inventory unequipped legs with 2 stars

    result = ParsedMessage()
    message_body_parts = message_body.split()
    page = -1

    while len(message_body_parts) > 0:
        message_part = message_body_parts.pop(0)
        try:
            num = int(message_part)

            if len(message_body_parts) == 0:
                if not page < 0:
                    raise ValueError("page was already set earlier in inventory command, but message ended with a page number as well")
                result.page = num
                break

            message_part = message_body_parts[0]
            if not ("star" == message_part or "stars" == message_part):
                raise ValueError("found strange number in middle of message")

            message_body_parts.pop(0)
            result.number_of_stars = num
        except:
            if "unequipped" in message_part:
                result.include_equipped = False
                continue

            if "with" in message_part:
                continue

            if "short" in message_part:
                result.short = True
                continue

            if ("star" == message_part or "stars" == message_part):
                raise ValueError("found lone `stars` in inventory command; only permitted following a number, which should have already been consumed earlier in the loop")

            if "page" == message_part:
                if len(message_body_parts) == 0:
                    return result
                message_part = message_body_parts.pop(0)
                # allow for this to throw, we should only ever see a number following "page"
                page = int(message_part)
                continue

            if result.tag is not None:
                raise ValueError("multiple tags found, please only provide one")

            result.tag = message_part

    if page > 0:
        result.page = page
    return result

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
