import inventory
import equip
from gacha_tables import all_parts_list
import asyncio
import regeneration
import db


SCRAP_TRADEIN_THRESHOLD = 5

def get_scrap(playerdata):
    return playerdata['scrap']

async def scrap_command(message, message_body, client):

    user_id = message.author.id
    offered_item_name = message_body.strip()


    playerdata = db.get_player_data(user_id)

    if offered_item_name == "":
        return await message.channel.send(f"To use this command, use `m!scrap <item name or ID>`. Items you scrap are destroyed and their stars are turned into scrap. Every {SCRAP_TRADEIN_THRESHOLD} stars' worth of scrap gives you extra pulls! \nYou have {playerdata['scrap']} scrap.")
        
    your_inventory = inventory.compute_inventory(user_id)
  
    # compute id of the item whose title the user gave
    offered_item_index = equip.select_item_index_by_name_or_position(offered_item_name, your_inventory)

    if offered_item_index == -1:
        return await message.channel.send("I'm not sure what item that is. To scrap one of your items, use m!scrap <item title or position>")

    if offered_item_index >= len(your_inventory):
        return await message.channel.send("Ya tried to scrap an item in a position that's beyond the number of items in your inventory! Try a smaller number.")
        
    offered_item = all_parts_list[your_inventory[offered_item_index]]
    offered_item_id = offered_item.id

    playerdata = db.get_player_data(user_id)
    currently_equipped = offered_item_index in playerdata["equipment"]

    # check for how many copies of this item you have, and whether it's equipped
    num_copies = 0
    for index, itemid in enumerate(your_inventory):
        if itemid == offered_item_id:
            num_copies += 1
            # People probably don't want to scrap things currently equipped. 
            # If you have multiple copies of an item, and only one is equipped, sneakily choose the non-equipped one
            if currently_equipped and index not in playerdata['equipment']:
                offered_item_index = index
                currently_equipped = False

    offer_msg = f"Is this the item you want to scrap?\n{inventory.format_item(offered_item.id)}\n{'You have ' + str(num_copies) + ' of them.' if num_copies > 1 else ''}{'**You have this item equipped.**' if currently_equipped else ''}\nIf you're sure, react with 👍 to scrap it."
    reactmessage = await message.channel.send(offer_msg)
    await reactmessage.add_reaction('👍')
    await reactmessage.add_reaction('👎')

    try:
        reaction, user = await client.wait_for('reaction_add', timeout=5 * 60.0, check= 
            lambda reaction, user: reaction.message == reactmessage and user.id == user_id and str(reaction.emoji) in ('👍', '👎')
        )
        if str(reaction.emoji) == '👎':
            await message.channel.send(f'Fine. Keep your items away from my delicious scrap pile.')
            return

        #if we get here, we've got a successful approval!
    except asyncio.TimeoutError:
        await message.channel.send('Okay, this item won\'t be scrapped.')
        try:    
            await reactmessage.clear_reactions()
        except discord.errors.Forbidden:
            pass
        return

    stars = offered_item.stars

    existing_scrap = float(playerdata["scrap"])
    added_scrap = stars
    playerdata["scrap"] = existing_scrap + added_scrap

    traded_in = False
    while playerdata["scrap"] >= SCRAP_TRADEIN_THRESHOLD:
        # trade in!
        traded_in = True
        playerdata["scrap"] -= SCRAP_TRADEIN_THRESHOLD

        # free pulls!
        playerdata["ratoon_pulls"] += 1/4
        playerdata["mech_pulls"] += 1

    db.set_player_data(user_id, playerdata)

    inventory.remove_from_inventory_by_position(offered_item_index, user_id)

    if not traded_in:
        await message.channel.send(f"You scrapped your {offered_item.name} {'★' * stars} and got {stars} scrap. You now have {playerdata['scrap']} scrap.")
    else:
        await message.channel.send(f"You scrapped your {offered_item.name} {'★' * stars} and got {stars} scrap - enough to salvage a day's worth of pulls! You now have {playerdata['scrap']} scrap.")
        
