from inventory import compute_inventory, format_item
import db
import inventory
from data_utils import paginate
from pulls import get_playerdata, get_username
from gacha_tables import all_parts_list, all_mechs_by_part
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

def filter_equipment(player_data, inventory, short=False):
    equipment = []
    player_data["equipment"].sort()
    for equipped_index in player_data["equipment"]:
        # print(equipped)
        equipment.append(format_item(inventory[equipped_index], equipped_index, False, short))
    return equipment

def count_equipped_categories(player_data, inventory):

    tagCount = {tag.name: 0 for tag in TagType}
    for equipped_index in player_data["equipment"]:

        equipped_item_index = inventory[equipped_index]

        item = all_parts_list[equipped_item_index]

        for tag in item.tags:
            tagCount[tag] += 1
    return tagCount

    

async def mech_command(message, message_body, client, include_sources = False, short=False):
    return await print_mech_inventory_command(message, message_body, client, include_sources, short)


async def print_mech_inventory_command(message, message_body, client, include_sources = False, short = False):

    userid = message.author.id
    username = message.author.display_name

    playerdata = get_playerdata(userid)

    inventory = compute_inventory(userid)

    if not "equipment" in playerdata:
        playerdata["equipment"] = []
        db.set_player_data(userid, playerdata)

    try:
        page = int(message_body.strip())
    except:
        page = 1 # page 1 is the first page

    if page <= 0:
        return await message.channel.send("There ain't no such page of your inventory")


    newline = "\n"

    if include_sources:
        mechs = {} # dict of mech username: items
        playerdata["equipment"].sort()

        for equipped_index in playerdata["equipment"]:
            item_id = inventory[equipped_index]
            item_data = all_parts_list[item_id]

            mech = all_mechs_by_part[item_id]
            mechs.setdefault(mech, []).append(item_data)

        mechs_string = f"# {username}'s Mech has items from:"
        for (mech, items) in sorted(mechs.items(), key=lambda t: -len(t[1])):
            mechs_string += newline
            items = sorted(items, key=lambda i: -i.stars)
            mech_string_array = []
            for item_data in items:
                star_character = "☆" if "event" in item_data.tags else "★"
                stars_string = star_character * item_data.stars
                mech_string_array.append(f'- {item_data.name} {stars_string}')
            mechs_string += f"## {mech}:{newline}" + newline.join(mech_string_array)

        return await message.channel.send(mechs_string)


    equipment = filter_equipment(playerdata, inventory, short)
    page -= 1
    pages = paginate(equipment, 1500)
    prefix = ""
    if (len(pages) > 1):
        prefix = f"(Page {page+1}/{len(pages)})\n"

    equipped_items_report = f"{newline}".join(pages[page])

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

    mech_string = f'## {username}\'s Mech:{newline}{prefix}{equipped_items_report}{missing_categories_report}{instructions}'

    # Todo: replace this with an item count limit
    if len(mech_string) >= 2000:
        return await message.channel.send("Error: Your mech has too many items equipped! Please unequip some.")

    return await message.channel.send(mech_string)

async def equip_command(message, message_body, client):
    userid = message.author.id

    playerdata = get_playerdata(userid)

    inventory = compute_inventory(userid)

    if len(inventory) == 0:
        return await message.channel.send("Get some items first using m!pull !")


    if not "equipment" in playerdata:
        playerdata["equipment"] = []
        db.set_player_data(userid, playerdata)

    # Items can be equipped either by number (position in inventory) or by title, which will use fuzzy string matching

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
        # no item given
        return await print_mech_inventory_command(message, message_body, client)

    if (item_index < 0 or item_index >= len(inventory)):
        return await message.channel.send("That isn't an existing id!")
    
    if item_index in playerdata["equipment"]:
        return await message.channel.send("That item is already equipped!")

    equip_item(userid, playerdata, item_index)
    
    return await message.channel.send(f"Equipped {all_parts_list[inventory[item_index]].name}!")

def select_item_index_by_name_or_position(requested_item, inventory):
    # requested_item is the name of an item in your inventory, or "2" for the second item in inventory
    # returns the index of an item in your inventory matching that name, or -1 if not found

    item_index = -1
    if requested_item.isnumeric():
        try:
            item_index = int(requested_item) - 1
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

    return item_index


async def unequip_command(message, message_body, client):
    userid = message.author.id

    playerdata = get_playerdata(userid)

    inventory = compute_inventory(userid)

    if not "equipment" in playerdata:
        playerdata["equipment"] = []
        db.set_player_data(userid, playerdata)

    requested_item = message_body.strip()

    item_index = select_item_index_by_name_or_position(requested_item, inventory)
        
    if item_index < 0:
        # no item given
        return await print_mech_inventory_command(message, message_body, client)
    
    if (item_index < 0 or item_index >= len(inventory)):
        return await message.channel.send("That isn't an existing id!")
    
    # print(item_index, playerdata["equipment"])
    if item_index not in playerdata["equipment"]:
        return await message.channel.send(f"Do you mean your {all_parts_list[inventory[item_index]].name}? That item is not equipped!")

    unequip_item(userid, playerdata, item_index)

    return await message.channel.send(f"Unequipped {all_parts_list[inventory[item_index]].name}")
