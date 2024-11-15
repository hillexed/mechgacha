from gacha_tables import ratoon_pullable_mechs, all_mechs
import random
import db
import inventory
import json

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

def get_playerdata(username):
    playerdata = db.get_player_data(username)

    if playerdata is None:
        inventory.add_new_player(username)
        playerdata = db.get_player_data(username)

    return playerdata
    # sample playerdata = {"unlocked_mechs": ['alto'], 'ratoon_pulls':2, 'mech_pulls': 5}

def get_user_current_mechs(playerdata):
    # sample playerdata = {"unlocked_mechs": ['alto'], 'ratoon_pulls':2, 'mech_pulls': 5}
    return playerdata["unlocked_mechs"]

def get_mech_pulls(playerdata):
    return playerdata["mech_pulls"]

def get_ratoon_pulls(playerdata):
    return playerdata["ratoon_pulls"]

def choose_mech_by_name(all_mechs, requested_mech_name):
    # all_names = [mech.username for mech in all_mechs]

    # todo: replace with fuzzy string matching

    for mech in all_mechs:
        if mech.username.lower() == requested_mech_name.lower():
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

def add_to_inventory(new_item, username):

    inv = db.get_inventory_data(username)
    inv.append(new_item.id)
    print(inv)
    db.set_inventory_data(username, inv)


async def pull_command(message, message_body):

    username = get_username(message)
    playerdata = get_playerdata(username)

    print(playerdata)

    if playerdata is None:
        logging.info(f"Adding {username}")
        inventory.add_new_player(username)

    requested_mech = message_body.strip()

    player_mechs = get_user_current_mechs(playerdata)

    if requested_mech == "":

        if len(player_mechs) == 0:
           # player hasn't pulled from ratoon's gacha yet
           return await message.channel.send(f"\nWelcome! To start getting parts, first use `m!pull ratoon` to get some mechs from Ratoon's gachapon (up to {get_ratoon_pulls(playerdata)} time{'s' if get_ratoon_pulls(playerdata) > 1 else ''}) Then use `m!pull <mech>` to get parts from any mech you have. You have {get_mech_pulls(playerdata)} pulls.")

        else:
            return await message.channel.send(f"\nUse m!pull <mech> to pull from their list! You can pull from: {', '.join(player_mechs)}. You have {get_mech_pulls(playerdata)} pulls.\n You can also use `m!pull ratoon` to get some mechs from Ratoon's gachapon. You have {get_ratoon_pulls(playerdata)} pulls from Ratoon's gachapon.")


    if requested_mech == "ratoon":

        if get_ratoon_pulls(playerdata) >= 1: # can pull
            mechs_user_doesnt_have = [mech.username for mech in ratoon_pullable_mechs if mech.username not in player_mechs]

            if len(mechs_user_doesnt_have) == 0:
                return await message.channel.send("Ya already got all da mechs!")

            new_mech = random.choice(mechs_user_doesnt_have)
            add_new_mech(username, playerdata, new_mech)
            deduct_ratoon_pull(username, playerdata)
            await message.channel.send(f"You got... \n**{new_mech}**!")
            return
        else:
            await message.channel.send("Ya got no pulls from me")
        


    elif can_pull(playerdata):
        # theoretically you can request any mech
        mech_to_pull_from = choose_mech_by_name(all_mechs, requested_mech)

        if mech_to_pull_from is None:
            await message.channel.send(f"I don't know that mech. Maybe ya typoed their name")

        player_mechs = get_user_current_mechs(playerdata)

        if not player_can_pull_from_mech(mech_to_pull_from, playerdata):
            await message.channel.send(f"Ya dont have that mech yet! Ya got these mechs: {','.join(player_mechs)}")
            return

        new_item = pull(mech_to_pull_from,1)[0]

        add_to_inventory(new_item, username)
        deduct_pull(username, playerdata)

        await message.channel.send(f"You got... \n**{new_item.name} {'★' * new_item.stars}**\n{new_item.description}")
    else:
        await message.channel.send(f"You are out of pulls!")
