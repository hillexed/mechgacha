from gacha_tables import ratoon_pullable_mechs, all_mechs, starting_inventory, merge_gatcha_tables
import random
import db
import inventory
import json
from data_utils import get_playerdata

from fuzzywuzzy import process

item_weights_by_stars = { 
1: 10,
2: 7,
3: 5,
4: 3,
5: 1 # 1/10 chance of getting a 5-star as a 1-star
}

def pull(mech, num_pulls=1):
    loot_options = mech.loot

    weights = [item_weights_by_stars[item.stars] for item in loot_options]

    return random.choices(loot_options, weights=weights, k=num_pulls)
    

if __name__ == "__main__":
    print(pull(ratoon_pullable_mechs[0]))


def can_pull(playerdata):
    return get_mech_pulls(playerdata) > 0

def deduct_pull(username, playerdata):
    playerdata["mech_pulls"] -= 1
    db.set_player_data(username, playerdata)

def deduct_ratoon_pull(username, playerdata):
    playerdata["ratoon_pulls"] -= 1
    db.set_player_data(username, playerdata)

def get_username(message):
    return message.author.id

def get_user_current_mechs(playerdata):
    # sample playerdata = {"unlocked_mechs": ['alto'], 'ratoon_pulls':2, 'mech_pulls': 5}
    return playerdata["unlocked_mechs"]

def get_mech_pulls(playerdata):
    return playerdata["mech_pulls"]

def get_ratoon_pulls(playerdata):
    return playerdata["ratoon_pulls"]

def choose_mech_by_name(all_mechs, requested_mech_name) -> 'gacha_mechanics.Mech':
    # fuzzy string matching!
    mech_names = [mech.username.lower() for mech in all_mechs]
    chosen_mech_name, closeness = process.extractOne(requested_mech_name, mech_names)

    if closeness < 85:
        return None

    for mech in all_mechs:
        if mech.username.lower() == chosen_mech_name.lower():
            return mech
    return None


def player_can_pull_from_mech(mech_to_pull_from, playerdata):

    if mech_to_pull_from.username in ("alto",):
        return True

    return mech_to_pull_from.username in playerdata["unlocked_mechs"] #add .lower()?


def add_new_mech(username, playerdata, new_mech):
    # sample playerdata = {"unlocked_mechs": ['alto'], 'ratoon_pulls':2, 'mech_pulls': 5}
    if playerdata is None:
        inventory.add_new_player(username)
        playerdata = db.get_player_data(username)

    if new_mech not in playerdata["unlocked_mechs"]:
        playerdata["unlocked_mechs"].append(new_mech)

    db.set_player_data(username, playerdata)


async def pull_command(message, message_body):

    username = get_username(message)
    playerdata = get_playerdata(username)

    # print(playerdata)

    if playerdata is None:
        logging.info(f"Adding {username}")
        inventory.add_new_player(username)

    requested_mech = message_body.strip()

    player_mechs = get_user_current_mechs(playerdata)

    if requested_mech == "":

        if len(player_mechs) == 0:
           # player hasn't pulled from ratoon's gacha yet
           return await message.channel.send(f"\nWelcome! To start getting parts, first use `m!pull ratoon` to get some mechs from Ratoon's gachapon (up to {get_ratoon_pulls(playerdata)} time{'s' if get_ratoon_pulls(playerdata) > 1 else ''}) Then use `m!pull <mech>` to get parts from any mech you have. You have {round(get_mech_pulls(playerdata), 2)} pulls, and you get more every day.")

        else:
            return await message.channel.send(f"\nUse m!pull <mech> to pull from their list! You can pull from: {', '.join(player_mechs)}. You have {round(get_mech_pulls(playerdata), 2)} pulls.\n You can also use `m!pull ratoon` to get some mechs from Ratoon's gachapon. You have {round(get_ratoon_pulls(playerdata),2)} pulls from Ratoon's gachapon.")


    if requested_mech.lower() == "ratoon":

        if get_ratoon_pulls(playerdata) >= 1: # can pull
            mechs_user_doesnt_have = [mech.username for mech in ratoon_pullable_mechs if mech.username not in player_mechs]

            if len(mechs_user_doesnt_have) == 0:
                return await message.channel.send("Ya already got all da mechs!")

            new_mech = random.choice(mechs_user_doesnt_have)
            add_new_mech(username, playerdata, new_mech)
            deduct_ratoon_pull(username, playerdata)
            await message.channel.send(f"You got... \n**{new_mech}**!\nNow you can use `m!pull {new_mech}` to get their parts!")
            return
        else:
            await message.channel.send("Ya got no pulls from me")

 
    elif can_pull(playerdata):
        # theoretically you can request any mech
        if requested_mech.lower() == "random":
            mech_to_pull_from = merge_gatcha_tables(player_mechs)
        else:
            mech_to_pull_from = choose_mech_by_name(all_mechs, requested_mech)

        if mech_to_pull_from is None:
            return await message.channel.send(f"I don't know that mech. Maybe ya typoed their name")

        player_mechs = get_user_current_mechs(playerdata)

        if not player_can_pull_from_mech(mech_to_pull_from, playerdata) and requested_mech != "random":
            return await message.channel.send(f"Ya dont have that mech yet! Ya got these mechs: {', '.join(player_mechs)}")
            

        tries_to_get_new_item = 3
        new_item = None

        # try repeatedly to get a new item you don't already have. 
        # If you get unlucky and get all duplicates in a row, then you deserve a duplicate
        user_inv = inventory.compute_inventory(username)
        for i in range(tries_to_get_new_item):
            # pull!
            new_item = pull(mech_to_pull_from,1)[0]
            # if the item isn't a duplicate, we're done!
            if not inventory.item_already_in_inventory(new_item, user_inv):
                break

        inventory.add_to_inventory(new_item, username)
        deduct_pull(username, playerdata)

        if requested_mech.lower() == "random":
            await message.channel.send(f"You pulled from all of your unlocked item pools and got... \n**{new_item.name} {'★' * new_item.stars}**\n{new_item.description}\n-# from {new_item.id.split(':')[0]}")
        else:
            await message.channel.send(f"You pulled from {mech_to_pull_from.username.lower()} and got... \n**{new_item.name} {'★' * new_item.stars}**\n{new_item.description}")
    else:
        await message.channel.send(f"You are out of pulls!")
