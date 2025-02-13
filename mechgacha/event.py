from gacha_tables import event_gift_mech
import random
import db
import inventory
from data_utils import get_playerdata

# Remember to change these when adding or expiring event gifts
available_gift_count = 1
expired_gift_count = 0
gift_size = 3

def has_unclaimed_gift(playerdata):
    if "event_gifts_claimed" not in playerdata or playerdata["event_gifts_claimed"] < expired_gift_count:
        playerdata["event_gifts_claimed"] = expired_gift_count
    return playerdata["event_gifts_claimed"] < (expired_gift_count + available_gift_count)

def get_item_id_pool():
    return {item.id for item in event_gift_mech.loot}

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
            pool = set(pool)
        gift = set()
        amount_to_pull = gift_size
        # Reload the pool if there's not enough left
        if len(pool) < gift_size:
            for item_id in pool:
                gift.add(item_id)
            pool = get_item_id_pool()
            amount_to_pull = gift_size - len(gift)
        # Pull!
        for __ in range(amount_to_pull):
            item_id = random.choice(pool)
            gift.add(item_id)
            pool.remove(item_id)
        for item_id in gift:
            inventory.add_id_to_inventory(item_id, user_id)
        # Save what's left for next time
        db.set_game_data(get_game_data_pool_entry_name(), pool)
        # Don't give infinite gifts
        playerdata["event_gifts_claimed"] += 1
        db.set_player_data(user_id, playerdata)
    else:
        return await message.channel.send("There are no gifts for you to claim.")
