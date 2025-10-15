from gacha_tables import event_gift_mech
import random
import db
import inventory
from data_utils import get_playerdata

event_active = True
event_name = "Discovery Day"
event_submission_active = False
event_submission_link = "https://forms.gle/SpKogNFCy5TyTxno9"

# Remember to change these when adding or expiring event gifts
starting_event_pulls = 0 # This counts up to max_event_pulls (I think)
max_event_pulls = 1
current_event = "discovery"
gift_item_count = 3

async def debug_add_gift(message, user_id):
    playerdata = get_playerdata(user_id)
    setup_playerdata_if_needed(playerdata)

    if playerdata["event_pulls"] == starting_event_pulls:
        return await message.channel.send("That user has all their gifts available to claim!")

    playerdata["event_pulls"] -= 1
    db.set_player_data(user_id, playerdata)
    return await message.channel.send(f'That user has recieved a free gift. Now they have claimed {playerdata["event_pulls"]}.')

def setup_playerdata_if_needed(playerdata):
    # set up variables in case this is the first time the player has used an event command
    # make sure to save the playerdata afterwards in the DB!
    if "event_pulls" not in playerdata or playerdata["last_event"] != current_event:
        playerdata["event_pulls"] = starting_event_pulls
        playerdata["last_event"] = current_event

def has_unclaimed_gift(playerdata):
    setup_playerdata_if_needed(playerdata)
    return playerdata["event_pulls"] < max_event_pulls

def get_gift_count(playerdata):
    setup_playerdata_if_needed(playerdata)
    return max_event_pulls - playerdata["event_pulls"]

def get_item_id_pool():
    return [item.id for item in event_gift_mech.loot]

def get_game_data_pool_entry_name():
    return f"{event_gift_mech.username}_pool"

async def event_info_command(message):
    user_id = message.author.id
    playerdata = get_playerdata(user_id)
    if event_active:
        gift_count = get_gift_count(playerdata)
        gift_text = f"You can open {gift_count} more gift bag{'s' if gift_count > 1 else ''}. Use `m!event claim` to open one!" if has_unclaimed_gift(playerdata) else "You have no gift bags available to claim!"
        return await message.channel.send(f"{event_name} is currently ongoing!\n{gift_text}")
    elif event_submission_active:
        return await message.channel.send(f"{event_name} is currently being developed! Participate here: {event_submission_link}")
    else:
        return await message.channel.send("No events are currently ongoing.")

async def event_claim_command(message):
    user_id = message.author.id
    playerdata = get_playerdata(user_id)
    if has_unclaimed_gift(playerdata):
        # Storing the pool ensures an even distribution of the items
        pool = db.get_game_data(get_game_data_pool_entry_name())
        # Initialize
        if pool is None:
            pool = get_item_id_pool()
        else:
            pool = list(pool)
        gift = list()
        amount_to_pull = gift_item_count

        # Reload the pool if there's not enough left
        if len(pool) < amount_to_pull:
            gift = pool[:] # you get the leftovers
            amount_to_pull -= len(gift)
            pool = get_item_id_pool() # refill pool

        pullable_items = [x for x in pool if x not in gift] # ensure you don't get a duplicate if you were at the end of the pool pre-refill
        # Pull!
        for __ in range(amount_to_pull):
            item_id = random.choice(pullable_items)
            gift.append(item_id)
            pool.remove(item_id)
            pullable_items.remove(item_id)
        for item_id in gift:
            inventory.add_id_to_inventory(item_id, user_id)
        # Save what's left for next time
        db.set_game_data(get_game_data_pool_entry_name(), pool)
        # Don't give infinite gifts

        if "event_pulls" not in playerdata:
            playerdata["event_pulls"] = starting_event_pulls

        playerdata["event_pulls"] += 1
        db.set_player_data(user_id, playerdata)
        
        item_string = "\n" + '\n'.join([inventory.format_item(x) for x in gift])

        return await message.channel.send(f"You got: {item_string}")
    else:
        return await message.channel.send("There are no gifts for you to claim.")

async def clam(message):
    user_id = message.author.id
    playerdata = get_playerdata(user_id)
    playerdata["clammed"] = 1
    db.set_player_data(user_id, playerdata)
    return await message.channel.send("*clamps you... with synergy!*")
