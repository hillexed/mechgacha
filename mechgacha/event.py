from gacha_tables import event_gift_mech
import random
import db
import inventory
from data_utils import get_playerdata

# Remember to change these when adding or expiring event gifts
event_pulls = 2
current_event = "event_formal"
gift_item_count = 3

# playerdata will have: event_pulls undefined
# event_gifts set to 0 means user has already claimed
# expired_event_pulls

def has_unclaimed_gift(playerdata):
    if "event_pulls" not in playerdata or playerdata["last_event"] != current_event:
        playerdata["event_pulls"] = event_pulls
        playerdata["last_event"] = current_event
    return playerdata["event_pulls"] > 0

def get_item_id_pool():
    return [item.id for item in event_gift_mech.loot]

def get_game_data_pool_entry_name():
    return f"{event_gift_mech.username}_pool"

async def event_info_command(message):
    user_id = message.author.id
    playerdata = get_playerdata(user_id)
    return await message.channel.send(f"The 48th annual Mech Formal is currently ongoing!\n{'Use `m!event claim` for your gift bag!' if has_unclaimed_gift(playerdata) else ''}")

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
        playerdata["event_pulls"] -= 1
        db.set_player_data(user_id, playerdata)
        
        item_string = "\n" + '\n'.join([inventory.format_item(x) for x in gift])

        return await message.channel.send(f"You got: {item_string}")
    else:
        return await message.channel.send("There are no gifts for you to claim.")
