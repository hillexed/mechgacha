import datetime
import random
import math

from gacha_tables import all_parts_list, shop_gacha, shop_pullable_mechs
from inventory import format_item, add_id_to_inventory
import db
import scrap
from fuzzywuzzy import process

import zoneinfo
timezone_for_shopchange = zoneinfo.ZoneInfo('US/Eastern')# At midnight, when the day changes in this timezone, the shop will update

NUM_SCRAP_FOR_ONE_PULL = 5

def get_all_parts_with_tags(itemlist, desired_tags):
    return list(filter(lambda item: any([tag in desired_tags for tag in item.tags]), itemlist))

# collect all possible parts the shop can pull from in one list
shop_pullable_parts = []
for mech in shop_pullable_mechs:
    shop_pullable_parts.extend(mech.loot)
            
def get_todays_shop_pool():
    # this index will update whenever it is midnight in the timezone timezone_for_shopchange
    shop_index, _ = shop_change_time_computations()

    parts_to_choose_from = shop_pullable_parts

    match shop_index:
        case 0:
            shop_selection = get_all_parts_with_tags(parts_to_choose_from, ["body"])
        case 1:
            shop_selection = get_all_parts_with_tags(parts_to_choose_from, ["arms"])
        case 2:
            shop_selection = get_all_parts_with_tags(parts_to_choose_from, ["power"])
        case 3:
            shop_selection = get_all_parts_with_tags(parts_to_choose_from, ["weapon"])
        case 4:
            shop_selection = get_all_parts_with_tags(parts_to_choose_from, ["kit"])
        case 5:
            shop_selection = get_all_parts_with_tags(parts_to_choose_from, ["bodyplan"])
        case 6:
            shop_selection = get_all_parts_with_tags(parts_to_choose_from, ["event"])
        case 7: # Pillar Utilities
            shop_selection = get_all_parts_with_tags(parts_to_choose_from, ["cockpit"])
        case 8: # Back Market
            shop_selection = get_all_parts_with_tags(parts_to_choose_from, ["back"])
        case 9: # Great Furnace
            shop_selection = get_all_parts_with_tags(parts_to_choose_from, ["legs"])
        case 10: # Crossroads
            shop_selection = get_all_parts_with_tags(parts_to_choose_from, ["cosmetic"])

    return shop_selection

def get_shop_items():
    # Seed the RNG using today's date. This means when the day changes, the 3 random items will change too

    seed = "Shop seeded by day:" + str(datetime.datetime.now(timezone_for_shopchange).date())
    shop_rng = random.Random(seed)

    num_shop_items = 3

    shop_pool = get_todays_shop_pool() # changes based on weekday
    return shop_rng.sample(shop_pool, k=num_shop_items)


def format_item_listing(item, item_index):
    item_as_string = format_item(item.id)
    return format_shop_listing(item_as_string, item_index, cost=shop_cost(item))

def format_pull_listing(item_index):
    return format_shop_listing("An extra gacha pull, freshly refurbished!", item_index, cost=NUM_SCRAP_FOR_ONE_PULL)

def format_shop_listing(item_string, item_index, cost):
    return f"""- `[{item_index+1}]` {item_string}
-# **     **Cost: **{cost} scrap**"""



shop_time_interval = datetime.timedelta(days=2)
num_shops = 11
shop_change_reference = datetime.datetime(2026,1,2, tzinfo=timezone_for_shopchange)

def shop_change_time_computations():
    first_time = datetime.datetime.now(timezone_for_shopchange)
    difference = first_time - shop_change_reference

    shop_index = math.floor((difference / shop_time_interval) % num_shops)

    time_since_last_shop_change = difference % shop_time_interval

    time_until_next_shop = shop_time_interval - time_since_last_shop_change

    return shop_index, time_until_next_shop

    

def get_shop_info():
    shop_index, _ = shop_change_time_computations()
    match shop_index:
        case 0: # body
            today_shop_name = "Haydrian Mass Foundries"
            today_shop_description = "The cycling of the Core has brought the Mech Gacha to a sprawling industrial park, conveniently aligned with Ratoon's home. The facility's open-plan design and endless iron supply makes it ideal for constructing bulkier components of mechs, such as Body parts. An open hangar before the Mech Gacha holds some freshly-forged mech parts for trade:"
        case 1: # arms
            today_shop_name = "The Workhouse"
            today_shop_description = "The cycling of the Core has brought the Mech Gacha to The Workhouse. The sounds of exercise machines and milling machines greet you as you enter the massive gym/workshop complex—this is where denizens of the Core both mechanical and biological go to build their perfect body. Looking up from their work, an unbelievably buff alien and a robot with distressingly many appendages hurry over, excited to show off their latest mech-scale gains:"
        case 2: # power
            today_shop_name = "Generator #56562 Waste Management Outlet"
            today_shop_description = "The cycling of the Core has brought the Mech Gacha to a sprawling power plant. Facilities like this one help keep the entire Core running, with endless engines and management systems working in tandem to send power to wherever it's needed. A stockpile of Power systems no longer fit for use in the power grid, but perfect for retrofitting, lie before you:"
        case 3: # weapons
            today_shop_name = "Screwloose Botlabs"
            today_shop_description = "The cycling of the Core has brought the Mech Gacha to the Combat Roblotics League campus, a compact arena intended for smaller RC robots to test their might. The Screwloose storefront holds a veritable arsenal of mech weaponry, optimized for winning through style, control, damage and aggression. Torus McGhee, eagerly manning the counter, revs with anticipation as you peruse your options:"
        case 4: # kits
            today_shop_name = "C.E.N.T.E.R. Surplus"
            today_shop_description = "The cycling of the Core has brought the Mech Gacha to C.E.N.T.E.R.'s DownTown HQ. The hub is a hive of activity, with recruits busy at work training for their future roles in reconnaissance, and often willing to help out with mech repairs after particularly fierce battles. Most useful, though, is the wide variety of utility Kits available, which have been upcycled for mech use as a part of project work:"
        case 5: # bodyplans
            today_shop_name = "B.A.C.K. Market"
            today_shop_description = "The cycling of the Core has brought the Mech Gacha to the B.A.C.K. Archives. Towering shelves loom overhead, holding endless mech blueprints and component Manuals. A handwritten note, beside a curated set of blueprints on a stand, simply reads: \"You may have a copy of these Body Plans, in exchange for an appropriate donation of scrap. M.B.\""
        case 6: # special
            today_shop_name = "[NULLIFIED]"
            today_shop_description = "The cycling of the Core has brought the Mech Gacha to parts unknown. Suspended over blackest depths of the Pillars, a metal catwalk over the abyss holds an impromptu black market. Ethereal lighting illuminates the wares of the hooded shopkeeps. Trinkets and decals make up the majority of their collection, but a keen eye spots some worthwhile finds:"
        case 7: 
            today_shop_name = "Pillar Utilities Central"
            today_shop_description = "The cycling of the Core has brought the Mech Gacha to Pillar Utilities Central. A sprawling mass of connectors, cables, pipes and tubes form a mesmerizing backdrop. Given the interconnected nature of this place, it has become part hub part fashion runway; a place for trading, reworking, and showing off Cockpit systems, such as:"
        case 8: 
            today_shop_name = "Back Market"
            today_shop_description = "The cycling of the Core has brought the Mech Gacha to the underground metropolis of the FBL Battle City. From the shade of reinforced back alleys, weary mech pilots spectate an ongoing mech brawl across the North Plaza. A few of them have some spare Back parts they're looking to offload:"
        case 9:
            today_shop_name = "The Great Furnace"
            today_shop_description = "The cycling of the Core has brought the Mech Gacha to the depths of the Foundries, the red-hot birthplace of many artificial beings in the Core. Dodging colorful fireproof banners and sticking to the temperature controlled catwalks above the white-hot vats, you visit the furnace of a Kiln Angel and Foundry Demon couple, known for being the best legsmiths in the game, to peruse their wares:"
        case 6: # Sunday, special
            today_shop_name = "The Crossroads"
            today_shop_description = "The cycling of the Core has brought the Mech Gacha to a dense yet cozy transport hub. Hand-built stores fill every nook and cranny of this ersatz mall. Travellers, collectors or even those just passing through swap art supplies, stories, stickers, postcards, and other mementos from their various journeys. Your modest pile of scrap attracts the interest of several Mechs, each with their own collection of Cosmetic curios:"

    return today_shop_name, today_shop_description

def shop_cost(item):

    if "event" in item.tags:
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
    else:
        match item.stars:
            case 1:
                return 10
            case 2:
                return 15
            case 3:
                return 20
            case 4:
                return 25
            case _:
                return 30

def view_shop(user_scrap="a competing standard (not yet accepted) of"):
    shop_choices = get_shop_items()
    shop_name, shop_description = get_shop_info()

    now = datetime.datetime.now(timezone_for_shopchange)
    t = datetime.time(23, 59, 59, tzinfo=timezone_for_shopchange)
    midnight_today = datetime.datetime.combine(now.date(), t)
    time_before_shop_change = midnight_today - now 


    _, time_before_shop_change = shop_change_time_computations()

    secs_in_hour = 60*60
    secs_in_day = secs_in_hour * 24

    if time_before_shop_change.days > 1:
        time_left_string = f"{time_before_shop_change.days} days"
    elif time_before_shop_change.total_seconds() > secs_in_day:
        time_left_string = f"one day and {int(time_before_shop_change.total_seconds() - secs_in_day) // secs_in_hour} hours"
    elif time_before_shop_change.total_seconds() > secs_in_hour:
        time_left_string = f"{time_before_shop_change.seconds // secs_in_hour} hours"
    elif time_before_shop_change.total_seconds() > (60):
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

    You have {user_scrap} scrap. To exchange scrap for an item, use m!shop <listing number>. Nothing catch your eye? The shop will change its selection in {time_left_string}."""

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
        
        add_id_to_inventory(item.id, user_id)
        playerdata["scrap"] -= scrap_cost

        db.set_player_data(user_id, playerdata)
        return await message.channel.send(f"You traded in {scrap_cost} scrap and received a {random.choice(['refurbished','refurbished','refurbished','lightly used','slightly scratched','polished','brand-new','lovingly worn','banged-up','dented','fine-looking','good quality','new','new','new','gift-wrapped','wrapped-up','wrapped-up','boxed','boxed'])} **{item.name}**! You now have {playerdata['scrap']} scrap.")
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

    
