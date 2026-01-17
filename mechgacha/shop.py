import datetime
import random

from gacha_tables import all_parts_list, shop_gacha
from inventory import format_item
import db
import scrap
from fuzzywuzzy import process

import zoneinfo
timezone_for_shopchange = zoneinfo.ZoneInfo('US/Eastern')# At midnight, when the day changes in this timezone, the shop will update

NUM_SCRAP_FOR_ONE_PULL = 5

def get_all_parts_with_tags(itemlist, desired_tags):
    return list(filter(lambda item: any([tag in desired_tags for tag in item.tags]), itemlist))
            
def get_todays_shop_pool():
    # this index will update whenever it is midnight in the timezone timezone_for_shopchange
    weekday_index = datetime.datetime.now(timezone_for_shopchange).weekday()


    parts_to_choose_from = all_parts_list.values()
    # parts_to_choose_from = shop_gacha.loot

    match weekday_index:
        case 0: # Monday
            shop_selection = get_all_parts_with_tags(parts_to_choose_from, ["body","back"])
        case 1: # Tuesday
            shop_selection = get_all_parts_with_tags(parts_to_choose_from, ["arms","legs"])
        case 2: # Wednesday
            shop_selection = get_all_parts_with_tags(parts_to_choose_from, ["cockpit","power"])
        case 3: # Thursday
            shop_selection = get_all_parts_with_tags(parts_to_choose_from, ["weapon"])
        case 4: # Friday
            shop_selection = get_all_parts_with_tags(parts_to_choose_from, ["kit"])
        case 5: # Saturday
            shop_selection = get_all_parts_with_tags(parts_to_choose_from, ["bodyplan"])
        case 6: # Sunday
            shop_selection = get_all_parts_with_tags(parts_to_choose_from, ["cosmetic"])
            # Sunday shop also includes event items
            for mech in event_mechs:
                shop_selection.extend(mech.loot)
            # shop_selection.extend(nullified.loot)

    return shop_selection

def get_shop_items():
    # Seed the RNG using today's date. This means when the day changes, the 3 random items will change too

    seed = "Shop seeded by day:" + str(datetime.datetime.now(timezone_for_shopchange).today().date())
    shop_rng = random.Random(seed)

    num_shop_items = 3

    shop_pool = get_todays_shop_pool() # changes based on weekday
    return shop_rng.choices(shop_pool, k=num_shop_items)


def format_item_listing(item, item_index):
    item_as_string = format_item(item.id)
    return format_shop_listing(item_as_string, item_index, cost=shop_cost(item))

def format_pull_listing(item_index):
    return format_shop_listing("An extra gacha pull, freshly refurbished!", item_index, cost=NUM_SCRAP_FOR_ONE_PULL)

def format_shop_listing(item_string, item_index, cost):
    return f"""- `[{item_index+1}]` {item_string}
-# **     **Cost: **{cost} scrap**"""


def shop_cost(item):

    if "event" in item.tags:
        match item.stars:
            case 1:
                return 20
            case 2:
                return 45
            case 3:
                return 50
            case 4:
                return 75
            case _:
                return 100
    else:
        match item.stars:
            case 1:
                return 10
            case 2:
                return 20
            case 3:
                return 30
            case 4:
                return 40
            case _:
                return 50

def get_shop_info():
    weekday_index = datetime.datetime.now(timezone_for_shopchange).weekday()
    match weekday_index:
        case 0: # Monday, body & back
            today_shop_name = "Haydrian Mass Foundries"
            today_shop_description = "The cycling of the Core has brought the Mech Gacha to a sprawling industrial park, conveniently aligned with Ratoon's home. The facility's open-plan design and endless iron supply makes it ideal for constructing bulkier components of mechs, such as Body and Back parts. An open hangar before the Mech Gacha holds some freshly-forged mech parts for trade:"
        case 1: # Tuesday, arms & legs
            today_shop_name = ""
            today_shop_description = ""
        case 2: # Wednesday, cockpit & power
            today_shop_name = ""
            today_shop_description = ""
        case 3: # Thursday, weapons
            today_shop_name = "Screwloose Botlabs"
            today_shop_description = "The cycling of the Core has brought the Mech Gacha to the Combat Roblotics League campus, a compact arena intended for smaller RC robots to test their might. The Screwloose storefront holds a veritable arsenal of mech weaponry, optimized for winning through style, control, damage and aggression. Torus McGhee, eagerly manning the counter, revs with anticipation as you peruse your options:"
        case 4: # Friday, kits
            today_shop_name = ""
            today_shop_description = ""
        case 5: # Saturday, bodyplans
            today_shop_name = "B.A.C.K. Market"
            today_shop_description = "The cycling of the Core has brought the Mech Gacha to the B.A.C.K. Archives. Towering shelves loom overhead, holding endless mech blueprints and component Manuals. A handwritten note, beside a curated set of blueprints on a stand, simply reads: \"You may have a copy of these Body Plans, in exchange for an appropriate donation of scrap. M.B.\":"
        case 6: # Sunday, special
            today_shop_name = "[NULLIFIED]"
            today_shop_description = "The cycling of the Core has brought the Mech Gacha to parts unknown. Suspended over blackest depths of the Pillars, a metal catwalk over the abyss holds an impromptu black market. Ethereal lighting illuminates the wares of the hooded shopkeeps. Trinkets and decals make up the majority of their collection, but a keen eye spots some worthwhile finds:"

    return today_shop_name, today_shop_description
       

def view_shop(user_scrap="a competing standard (not yet accepted) of"):
    shop_choices = get_shop_items()
    shop_name, shop_description = get_shop_info()

    now = datetime.datetime.now(timezone_for_shopchange)
    t = datetime.time(23, 59, 59, tzinfo=timezone_for_shopchange)
    midnight_today = datetime.datetime.combine(now.date(), t)
    time_before_shop_change = midnight_today - now 

    secs_in_hour = 60*60
    if time_before_shop_change.seconds > secs_in_hour:
        time_left_string = f"{time_before_shop_change.seconds // secs_in_hour} hours"
    elif time_before_shop_change.seconds > (60):
        time_left_string = f"{time_before_shop_change.seconds // 60} minutes"
    else:
        time_left_string = f"{time_before_shop_change.seconds} seconds"

    newline = '\n'

    return f"""# **{shop_name}**
{shop_description}
{newline.join([
    format_item_listing(item, i) 
    for i, item in enumerate(shop_choices)])}
{format_pull_listing(len(shop_choices))}

    You have {user_scrap} scrap. Nothing catch your eye? The shop will change its selection in {time_left_string}. To exchange scrap for an item, go bug Ratoon to stop painting his scrap with that sticky stuff and maybe I'll think about letting ya trade. Now scram!"""


#     "You have {user_scrap} scrap. To exchange scrap for an item, use m!shop <listing number>. Nothing catch your eye? The shop will change its selection in {time_left_string}."""

async def exchange_scrap_for_pull(message, user_id, playerdata):
    playerdata = db.get_player_data(user_id)

    traded_in = False
    if playerdata["scrap"] >= NUM_SCRAP_FOR_ONE_PULL:
        # trade in!
        playerdata["scrap"] -= NUM_SCRAP_FOR_ONE_PULL

        # free pulls!
        playerdata["ratoon_pulls"] += 1/4
        playerdata["mech_pulls"] += 1

        db.set_player_data(user_id, playerdata)
        return await message.channel.send(f"You traded in {NUM_SCRAP_FOR_ONE_PULL} scrap - enough to salvage a day's worth of pulls! You now have {playerdata['scrap']} scrap.")
    else:
        return await message.channel.send(f"You don't have the {NUM_SCRAP_FOR_ONE_PULL} scrap needed to exchange for this item. You have {playerdata['scrap']} scrap. Use m!scrap to recycle parts in your inventory into scrap.")
    

async def exchange_scrap_for_item(message, user_id, playerdata, item):
    playerdata = db.get_player_data(user_id)
    scrap_cost = shop_cost(item)

    if playerdata["scrap"] >= scrap_cost:
        # trade in!
        
        inventory.add_id_to_inventory(item.id, user_id)
        playerdata["scrap"] -= scrap_cost

        db.set_player_data(user_id, playerdata)
        return await message.channel.send(f"You traded in {NUM_SCRAP_FOR_ONE_PULL} scrap and received a f{random.choice(['refurbished','refurbished','refurbished','lightly used','slightly scratched','polished','brand-new','lovingly worn','banged-up','dented','fine-looking','good quality','new','new','new','gift-wrapped','wrapped-up','wrapped-up','boxed','boxed'])} **{item.name}**! You now have {playerdata['scrap']} scrap.")
    else:
        return await message.channel.send(f"You don't have the {NUM_SCRAP_FOR_ONE_PULL} scrap needed to exchange for the {item.name}. You have {playerdata['scrap']} scrap. Use m!scrap to recycle parts in your inventory into scrap.")

async def shop_command(message, message_body, client):
    # m!shop shows the shop listings.
    # m!shop 1 tries to buy an item.
    # m!shop <item name> tries to search for it.
    # m!shop (last number) or m!shop pull exchanges 5 scrap for a new pull.

    user_id = message.author.id
    selected_item = message_body.strip()

    playerdata = db.get_player_data(user_id)

    scrap_amount = scrap.get_scrap(playerdata)

    current_shop_items = get_shop_items()

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
        choices = [item.name for item in current_shop_items] + ['pull']
        chosen_item_name, closeness = process.extractOne(requested_item, choices)

        for i in range(len(current_shop_items)):
            if current_shop_items[i].name == chosen_item_name:
                item_index = i
        
    if item_index != -1:
        # user requested to exchange for something
        if item_index == len(current_shop_items):
            # last item in the index, which is always 'pull'.
            # exchange 5 scrap for one pull
            # return await message.channel.send("Ya want a pull, eh? They're giving em away for free, you know. Don't even polish em. I'd love to give those pulls a bit of refurbishing first...")
            return await exchange_scrap_for_pull(message, user_id, playerdata)

        elif item_index < 0 or item_index > len(current_shop_items):
            return await message.channel.send("That listing doesn't make any sense!")
        else:
            selected_item = current_shop_items[item_index]
            return await exchange_scrap_for_item(message, user_id, playerdata, selected_item)
            # return await message.channel.send(f"Ya want the {selected_item.name}? I told ya, I have a hard time with touching that rat's scrap. Maybe I'll think about buying some gloves once shop construction is done. For now, scram!")
    else:
        return await message.channel.send(view_shop(scrap_amount))

    
