from gacha_tables import event_gift_mech
import random
import db
import inventory
from data_utils import get_playerdata

# Remember to change these when adding or expiring event gifts
starting_event_pulls = 0
current_event = "none"
gift_item_count = 3

# playerdata will have: event_pulls undefined
# event_gifts set to 0 means user has already claimed
# expired_event_pulls

async def debug_add_gift(message, user_id):
    playerdata = get_playerdata(user_id)
    setup_playerdata_if_needed(playerdata)

    if playerdata["event_pulls"] == starting_event_pulls:
        return await message.channel.send("That user has the maximum number of event pulls!")

    playerdata["event_pulls"] += 1
    db.set_player_data(user_id, playerdata)
    return await message.channel.send(f'That user has recieved another gift, bringing the total to {playerdata["event_pulls"]}.')

def setup_playerdata_if_needed(playerdata):
    # set up variables in case this is the first time the player has used an event command
    # make sure to save the playerdata afterwards in the DB!
    if "event_pulls" not in playerdata or playerdata["last_event"] != current_event:
        playerdata["event_pulls"] = starting_event_pulls
        playerdata["last_event"] = current_event

def has_unclaimed_gift(playerdata):
    setup_playerdata_if_needed(playerdata)
    return playerdata["event_pulls"] > 0

def get_item_id_pool():
    return [item.id for item in event_gift_mech.loot]

def get_game_data_pool_entry_name():
    return f"{event_gift_mech.username}_pool"

async def event_info_command(message):
    user_id = message.author.id
    playerdata = get_playerdata(user_id)
    #return await message.channel.send(f"The 48th annual Mech Formal is currently ongoing!\n{'Use `m!event claim` for your gift bag!' if has_unclaimed_gift(playerdata) else 'You have received your gift bags!'}")
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

        playerdata["event_pulls"] -= 1
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
    return await message.channel.send("How'd you find out I'm a bivalve?! I was pretending to be Ratoon so well... If you keep quiet, maybe I'll consider giving you something extra in the next event.")
