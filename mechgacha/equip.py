from inventory import compute_inventory, format_item
import db
import inventory
from pulls import get_playerdata, get_username
from gacha_tables import all_parts_list
from gacha_mechanics import TagType
from fuzzywuzzy import process


def equip_item(username, playerdata, item_index):
    # sample playerdata = {"unlocked_mechs": ['alto'], 'ratoon_pulls':2, 'mech_pulls': 5}
    if playerdata is None:
        inventory.add_new_player(username)
        playerdata = db.get_player_data(username)

    if item_index not in playerdata["equipment"]:
        playerdata["equipment"].append(item_index)

    db.set_player_data(username, playerdata)

def unequip_item(username, playerdata, item_index):
    # sample playerdata = {"unlocked_mechs": ['alto'], 'ratoon_pulls':2, 'mech_pulls': 5}
    if playerdata is None:
        inventory.add_new_player(username)
        playerdata = db.get_player_data(username)

    if item_index in playerdata["equipment"]:
        playerdata["equipment"].remove(item_index)

    db.set_player_data(username, playerdata)

def get_equipped_items(player_data, inventory):
    return [all_parts_list[inventory[equipped_index]] for item in player_data['equipment']]

def filter_equipment(player_data, inventory):
    equipment = []
    player_data["equipment"].sort()
    for equipped_index in player_data["equipment"]:
        # print(equipped)
        equipment.append(format_item(inventory[equipped_index], equipped_index, True))
    return equipment

def count_equipped_categories(player_data, inventory):

    tagCount = {tag.name: 0 for tag in TagType}
    for equipped_index in player_data["equipment"]:

        equipped_item_index = inventory[equipped_index]

        item = all_parts_list[equipped_item_index]

        for tag in item.tags:
            tagCount[tag] += 1
    return tagCount

async def mech_command(message, message_body, client):

    # Code here to catch mentions or uids and set it to peoples things

    userid = message.author.id
    username = message.author.display_name

    playerdata = get_playerdata(userid)

    inventory = compute_inventory(userid)

    if not "equipment" in playerdata:
        playerdata["equipment"] = []
        db.set_player_data(userid, playerdata)
    
    newline = "\n"

    equipped_items_report = f"{newline}".join(filter_equipment(playerdata, inventory))

    counts_by_category = count_equipped_categories(playerdata, inventory)
    missing_categories_report = ""
    if counts_by_category[TagType.arms.name] == 0:
        missing_categories_report += "\n* **No arms equipped**"
    if counts_by_category[TagType.legs.name] == 0:
        missing_categories_report += "\n* **No legs equipped**"
    if counts_by_category[TagType.body.name] == 0:
        missing_categories_report += "\n* **No body equipped**"
    #if counts_by_category["power"] == 0:
    #    missing_categories_report += "\n* **No power source equipped**" 

    instructions = "\n\n Equip or unequip parts from your inventory using `m!mech equip <item name>` or `m!mech unequip <item name>`!"

    return await message.channel.send(f'## {username}\'s Mech:{newline}{equipped_items_report}{missing_categories_report}{instructions}')

async def equip_command(message, message_body, client):
    userid = message.author.id

    playerdata = get_playerdata(userid)

    inventory = compute_inventory(userid)

    if len(inventory) == 0:
        return await message.channel.send("Get some items first using m!pull !")

    if not "equipment" in playerdata:
        playerdata["equipment"] = []
        db.set_player_data(userid, playerdata)

    requested_item = message_body.strip()
    item_index = -1
    if requested_item.isnumeric():
        try:
            item_index = int(message_body.strip()) - 1
        except:
            item_index = -1
    elif len(requested_item) == 0:
        item_index = -1
    else:
        # item could be a name.
        choices = [all_parts_list[itemid].name for itemid in inventory]
        chosen_item_name, closeness = process.extractOne(requested_item, choices)

        for i in range(len(inventory)):
            if all_parts_list[inventory[i]].name == chosen_item_name:
                item_index = i
        
        
        
    newline = "\n"

    if item_index < 0:
        return await message.channel.send(f'Equipped Items:{newline}{f"{newline}".join(filter_equipment(playerdata, inventory))}')
    
    if (item_index < 0 or item_index >= len(inventory)):
        return await message.channel.send("That isn't an existing id!")
    
    if item_index in playerdata["equipment"]:
        return await message.channel.send("That item is already equipped!")

    equip_item(userid, playerdata, item_index)
    
    return await message.channel.send(f"Equipped {all_parts_list[inventory[item_index]].name}!")


async def unequip_command(message, message_body, client):
    userid = message.author.id

    playerdata = get_playerdata(userid)

    inventory = compute_inventory(userid)

    if not "equipment" in playerdata:
        playerdata["equipment"] = []
        db.set_player_data(userid, playerdata)

    requested_item = message_body.strip()
    item_index = -1
    if requested_item.isnumeric():
        try:
            item_index = int(message_body.strip()) - 1
        except:
            item_index = -1
    elif len(requested_item) == 0:
        item_index = -1
    else:
        # item could be a name.
        choices = [all_parts_list[itemid].name for itemid in inventory]
        chosen_item_name, closeness = process.extractOne(requested_item, choices)

        for i in range(len(inventory)):
            if all_parts_list[inventory[i]].name == chosen_item_name:
                item_index = i
        
    newline = "\n"
    if item_index < 0:
        return await message.channel.send(f'Equipped Items:{newline}{f"{newline}".join(filter_equipment(playerdata, inventory))}')
    
    if (item_index < 0 or item_index >= len(inventory)):
        return await message.channel.send("That isn't an existing id!")
    
    # print(item_index, playerdata["equipment"])
    if item_index not in playerdata["equipment"]:
        return await message.channel.send("That item is not equipped!")

    unequip_item(userid, playerdata, item_index)

    return await message.channel.send(f"Unequipped {all_parts_list[inventory[item_index]].name}")
