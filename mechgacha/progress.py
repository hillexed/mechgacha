import db
from inventory import compute_inventory
from gacha_tables import all_mechs
from pulls import choose_mech_by_name, get_username, get_user_current_mechs, player_can_pull_from_mech
from data_utils import get_playerdata

async def progress_command(message, message_body):
    userid = message.author.id
    username = get_username(message)
    playerdata = get_playerdata(username)
    
    if playerdata is None:
       return await message.channel.send(f"\nWelcome! To start getting parts, first use `m!pull ratoon` to get some mechs from Ratoon's gachapon (up to {get_ratoon_pulls(playerdata)} time{'s' if get_ratoon_pulls(playerdata) > 1 else ''}) Then use `m!pull <mech>` to get parts from any mech you have. You have {round(get_mech_pulls(playerdata), 2)} pulls.")

    player_mechs = get_user_current_mechs(playerdata)
    
    requested_mech = message_body.strip()

    if requested_mech == "":
        return await message.channel.send(f"\nUse m!progress <mech> to see your progress through their list! You can see progress for: {', '.join(player_mechs)}.")

    mech_to_see_progress_for: 'gacha_mechanics.Mech' = choose_mech_by_name(all_mechs, requested_mech)

    if mech_to_see_progress_for is None:
        return await message.channel.send(f"I don't know that mech. Maybe ya typoed their name")

    if not player_can_pull_from_mech(mech_to_see_progress_for, playerdata):
        return await message.channel.send(f"Ya dont have that mech yet! Ya got these mechs: {','.join(player_mechs)}")

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

    sub_array = [f"## {mech_to_see_progress_for.username.lower()}'s gacha\n"]
    for star_count in range(max_stars):
        items_with_stars = stars.get(star_count)
        if items_with_stars is None:
            continue
        sub_array.append("## " + "★" * star_count)
        for (item, count) in items_with_stars:
            tags_string = f' ({", ".join([tag.lower() for tag in item.tags])})' if len(item.tags) > 0 else ""
            if count == 0:
                sub_array.append(f"- ???{tags_string}")
            else:
                item_string = f"- {item.name}{tags_string}"
                if count > 1:
                    item_string += f" (you have {count})"
                sub_array.append(item_string)

    return await message.channel.send("\n".join(sub_array))

     
