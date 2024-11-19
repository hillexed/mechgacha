from inventory import compute_inventory, format_item
import db
import inventory
from pulls import get_playerdata, get_username
from gacha_tables import all_parts_list


def equip_item(username, playerdata, item_id):
    # sample playerdata = {"unlocked_mechs": ['alto'], 'ratoon_pulls':2, 'mech_pulls': 5}
    if playerdata is None:
        inventory.add_new_player(username)
        playerdata = db.get_player_data(username)

    if item_id not in playerdata["equipment"]:
        playerdata["equipment"].append(item_id)

    db.set_player_data(username, playerdata)

def unequip_item(username, playerdata, item_id):
    # sample playerdata = {"unlocked_mechs": ['alto'], 'ratoon_pulls':2, 'mech_pulls': 5}
    if playerdata is None:
        inventory.add_new_player(username)
        playerdata = db.get_player_data(username)

    if item_id in playerdata["equipment"]:
        playerdata["equipment"].remove(item_id)

    db.set_player_data(username, playerdata)

def filter_equipment(player_data, inventory):
    equipment = []
    player_data["equipment"].sort()
    for equipped in player_data["equipment"]:
        # print(equipped)
        equipment.append(format_item(inventory[equipped], equipped, True))
    return equipment

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

    return await message.channel.send(f'## {username}\'s Mech:{newline}{f"{newline}".join(filter_equipment(playerdata, inventory))}')

async def equip_command(message, message_body, client):
    userid = message.author.id

    playerdata = get_playerdata(userid)

    inventory = compute_inventory(userid)

    if not "equipment" in playerdata:
        playerdata["equipment"] = []
        db.set_player_data(userid, playerdata)

    try:
        item_id = int(message_body.strip()) - 1
    except:
        item_id = -1
        
    newline = "\n"

    if item_id < 0:
        return await message.channel.send(f'Equipped Items:{newline}{f"{newline}".join(filter_equipment(playerdata, inventory))}')
    
    if (item_id < 0 or item_id >= len(inventory)):
        return await message.channel.send("That isn't an existing id!")
    
    if item_id in playerdata["equipment"]:
        return await message.channel.send("That item is already equipped!")

    equip_item(userid, playerdata, item_id)
    
    return await message.channel.send(f"Equipped {all_parts_list[inventory[item_id]].name}")


async def unequip_command(message, message_body, client):
    userid = message.author.id

    playerdata = get_playerdata(userid)

    inventory = compute_inventory(userid)

    if not "equipment" in playerdata:
        playerdata["equipment"] = []
        db.set_player_data(userid, playerdata)

    try:
        item_id = int(message_body.strip()) - 1
    except:
        item_id = -1
        
    newline = "\n"
    if item_id < 0:
        return await message.channel.send(f'Equipped Items:{newline}{f"{newline}".join(filter_equipment(playerdata, inventory))}')
    
    if (item_id < 0 or item_id >= len(inventory)):
        return await message.channel.send("That isn't an existing id!")
    
    # print(item_id, playerdata["equipment"])
    if item_id not in playerdata["equipment"]:
        return await message.channel.send("That item is not equipped!")

    unequip_item(userid, playerdata, item_id)

    return await message.channel.send(f"Unequipped {all_parts_list[inventory[item_id]].name}")
