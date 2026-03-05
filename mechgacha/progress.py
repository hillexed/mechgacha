import db
from inventory import compute_inventory, item_already_in_inventory
from gacha_tables import all_mechs, ratoon_pullable_mechs, event_mechs, shop_gacha
from pulls import choose_mech_by_name, get_user_current_mechs, player_can_pull_from_mech
from data_utils import get_playerdata

PROGRESS_BAR_LENGTH = 12
can_see_progress_without_unlocking = event_mechs # + (shop_gacha,)

async def progress_command(message, message_body):
    userid = message.author.id
    playerdata = get_playerdata(userid)
    username = message.author.display_name.lower()
    
    if playerdata is None:
       return await message.channel.send(f"\nWelcome! To start getting parts, first use `m!pull ratoon` to get some mechs from Ratoon's gachapon (up to {get_ratoon_pulls(playerdata)} time{'s' if get_ratoon_pulls(playerdata) > 1 else ''}) Then use `m!pull <mech>` to get parts from any mech you have. You have {round(get_mech_pulls(playerdata), 2)} pulls.")

    player_mechs = get_user_current_mechs(playerdata)
    
    requested_mech = message_body.strip()

    if requested_mech == "":
        return await message.channel.send(f"\nUse m!progress <mech> to see your progress through their list! You can see progress for: {', '.join(player_mechs)}.")

    if requested_mech.lower() == "ratoon":
        number_of_mechs_user_doesnt_have = sum(1 for mech in ratoon_pullable_mechs if mech.username not in player_mechs)

        if number_of_mechs_user_doesnt_have == 0:
            return await message.channel.send(f"\nYou have all of the mechs!")
        else:
            return await message.channel.send(f"\nYou have {number_of_mechs_user_doesnt_have} mech{'s' if number_of_mechs_user_doesnt_have != 1 else ''} remaining to pull")

    if requested_mech.lower() == "all":
        inventory = compute_inventory(userid)

        sub_array = [f"## {username}'s global progress on the gacha pool:"]
        for mech in ratoon_pullable_mechs:
            if mech.username not in player_mechs:
                continue
            sub_array.append(f"**{mech.username.lower()}**")
            number_of_unique_items_owned = sum(1 for item in mech.loot if item_already_in_inventory(item, inventory))
            number_of_possible_items = len(mech.loot)
            increments = (number_of_unique_items_owned * PROGRESS_BAR_LENGTH) // len(mech.loot)
            # tick the progress bar at least once if the user has at least one item
            if increments == 0 and number_of_unique_items_owned != 0:
                increments = 1

            sub_array.append(f"> `[{increments * '#'}{(PROGRESS_BAR_LENGTH - increments) * '-'}]` {number_of_unique_items_owned}/{len(mech.loot)}")

        return await message.channel.send("\n".join(sub_array))

    mech_to_see_progress_for: 'gacha_mechanics.Mech' = choose_mech_by_name(all_mechs, requested_mech)

    if mech_to_see_progress_for is None:
        return await message.channel.send(f"I don't know that mech. Maybe ya typoed their name")

    if (not player_can_pull_from_mech(mech_to_see_progress_for, playerdata) and not (mech_to_see_progress_for in can_see_progress_without_unlocking)):
        return await message.channel.send(f"Ya dont have that mech yet! Ya got these mechs: {', '.join(player_mechs)}")

    inventory = compute_inventory(userid)

    if inventory is None or len(inventory) == 0:
        return "**You have nothing in your inventory!** \n Use m!pull ratoon to get some mechs from Ratoon's gachapon, then m!pull <mech> to pull from their list!"

    stars = {}
    max_stars = 0
    for item in mech_to_see_progress_for.loot:
        matches = (item, sum(1 for inventory_item_id in inventory if item.id == inventory_item_id))
        stars.setdefault(item.stars, []).append(matches)
        if item.stars > max_stars:
           max_stars = item.stars

    sub_array = [f"## {username}'s progress on {mech_to_see_progress_for.username.lower()}'s gacha:\n"]
    for star_count in range(max_stars+1):
        items_with_stars = stars.get(star_count)
        if items_with_stars is None:
            continue
        star_character = "☆" if "event" in item.tags else "★"
        stars_string = star_character * star_count
        sub_array.append("## " + stars_string)
        for (item, count) in items_with_stars:
            tags_string = f' ({", ".join([tag.lower() for tag in item.tags])})' if len(item.tags) > 0 else ""
            if count == 0:
                # "secret" tag means item doesn't show up in item list until you have it
                if "secret" not in item.tags: 
                    sub_array.append(f"- ???{tags_string}")
            else:
                item_string = f"- {item.name}{tags_string}"
                if count > 1:
                    item_string += f" (you have {count})"
                sub_array.append(item_string)

    return await message.channel.send("\n".join(sub_array))

     
