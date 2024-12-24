import db
from datetime import datetime
import logging
import random
import re


from fuzzywuzzy import process
import time

from gacha_tables import all_parts_list

with open("logs.txt") as f:
    lines = f.readlines()

lines = "\n".join(lines).strip().split("🌒")
print(lines[0])
if lines[0] == "":
    lines = lines[1:]
    
bot_id = "836012465732059146"
last_commander = 0
pull_commanded = False

recovered_data = {}
last_commands = {}


all_item_names = [all_parts_list[itemid].name for itemid in all_parts_list]
name_to_id = {all_parts_list[itemid].name: itemid for itemid in all_parts_list}
def match_item_name_to_id(name):
    chosen_item_name, closeness = process.extractOne(name, choices=all_item_names)

    return name_to_id[chosen_item_name]

for i, line in enumerate(lines):

        userid, timestamp, msg = line.split("🌓")

        #if "scrap" in msg:
        #    print(f"🌒{userid}🌓{timestamp}🌓{msg}")

        if msg.startswith("m!"):
            cmd = msg.split(" ")[0].strip()
            last_commands[cmd] = userid

            if userid not in recovered_data:
                recovered_data[userid] = {"obtained": [], "scrapcount": 0}

        # counting last scrap values
        if m := re.search(r"You now have (.+) scrap", msg):
            scrap = m.group(1)
            scrap_command_user = last_commands['m!scrap']
            # print(f"User {scrap_command_user} has {scrap} scrap")
            recovered_data[scrap_command_user]["scrap"] = scrap
            recovered_data[scrap_command_user]["scrapcount"] += 1


        # getting new mechs
        if m := re.search(r"You got\.\.\. \n\n\*\*(.+)\*\*!", msg):
            # print(msg)
            thing = m.group(1)
            # print(f"User {last_commands['m!pull']} got {thing} mech")
    
            if "mechs" not in recovered_data[last_commands['m!pull']]:
              recovered_data[last_commands['m!pull']]["mechs"] = []
            recovered_data[last_commands['m!pull']]["mechs"].append(thing)

        if pull_commanded:
            if m := re.match(r"Use m!pull <mech> to pull from their list! You can pull from: (.+)\. You have (.+) pulls\.\n You can also use `m!pull ratoon` to get some mechs from Ratoon's gachapon\. You have (.+) pulls", msg):
                mechs = m.group(1)
                pulls = m.group(2)
                ratoon = m.group(3)
                # print((last_commander, mechs, pulls, ratoon))
                
                # playerdata = {"unlocked_mechs": mechs.split(", "), 'ratoon_pulls':float(ratoon), 'mech_pulls': float(pulls), 'equipment': [], "scrap": 0}
                # db.set_player_data(userid, playerdata)
            pull_commanded = False


        if "got..." and "★**" in msg:
            # part obtained
            if m := re.search(r'\*\*(.+) (★+)\*\*', msg):
                title = m.group(1)
                print((msg, title))
                if "pulls" not in recovered_data[last_commands['m!pull']]:
                  recovered_data[last_commands['m!pull']]["pulls"] = []
                recovered_data[last_commands['m!pull']]["pulls"].append(title)
            else:
                print("huh?")
                print(msg)

        # mech command
        if (msg.startswith("##") and '\'s Mech:' in msg):

            items = msg.split("\n- ")

            for item in items:
                if m := re.search(r'(.+) (★+) - (.+)\n\n-# \*\*     \*\*\[([0-9]+)\]', item):
                    title = m.group(1)
                    stars = m.group(2)
                    desc = m.group(3)
                    index = int(m.group(4))
                    # print((title, stars, desc, index))

                    equipped = '**EQUIPPED**' in item

                    # search for item by title

                    if "inventory" not in recovered_data[last_commands['m!mech']]:
                      recovered_data[last_commands['m!mech']]["inventory"] = {}
                      recovered_data[last_commands['m!mech']]["all_items"] = set()
                    recovered_data[last_commands['m!mech']]["inventory"][index] = title
                    recovered_data[last_commands['m!mech']]["all_items"].add(title)
        
        if msg.startswith("**Your inventory:**"):

            items = msg.split("\n- ")

            for item in items:
                if m := re.search(r'(.+) (★+) - (.+)\n\n-# \*\*     \*\*\[([0-9]+)\]', item):
                    title = m.group(1)
                    stars = m.group(2)
                    desc = m.group(3)
                    index = int(m.group(4))
                    # print((title, stars, desc, index))

                    equipped = '**EQUIPPED**' in item

                    # search for item by title

                    if "inventory" not in recovered_data[last_commands['m!inventory']]:
                      recovered_data[last_commands['m!inventory']]["inventory"] = {}
                      recovered_data[last_commands['m!inventory']]["all_items"] = set()
                    recovered_data[last_commands['m!inventory']]["inventory"][index] = title
                    recovered_data[last_commands['m!inventory']]["all_items"].add(title)
    
                    

                    # print(msg)

print("---")

for userid in recovered_data:
    data = recovered_data[userid]

    if "scrap" in data:
        # print((userid, data))
        pass
        # todo: give userid X data["scrap"] scrap
        # todo: give userid X data["mechs"] mechs (being careful not to overwrite duplicates)

    inventory_titles = []
    recovered_full_inventory = True
    if "inventory" in data:

        sorted_indices = [int(k) for k in data["inventory"].keys()]
        max_index = max(sorted_indices)

        max_index -= data["scrapcount"]

        

        # make sure every number in 1 through max_index is seen
        for i in range(1, max_index+1):
            if i not in sorted_indices:
                recovered_full_inventory = False
        #         print(i)

        inventory_titles = [data["inventory"][index] for index in data["inventory"] if index <= max_index]

        if not recovered_full_inventory:
            pass
            print(f"oh no! {userid} was missing some pages!")

    # backstop: ensure everything in pulls was there
    if "pulls" in data:
        for pull in data["pulls"]:
            if pull not in inventory_titles:
                inventory_titles.append(pull)

    if True:
        inv = db.get_inventory_data(userid)

        inventory = [match_item_name_to_id(title) for title in inventory_titles]                

        if userid == "409528027677196299":
          print(data)
          print(inventory)
        if True or len(inv) == 0:
            pass
            db.set_inventory_data(userid, inventory)


    pdata = db.get_inventory_data(userid)
    if type(pdata) == list:

        playerdata = {"unlocked_mechs": data["mechs"], 'ratoon_pulls':2, 'mech_pulls': 5, 'equipment': [], "scrap": 0}
    
        db.set_inventory_data(userid, pdata)
        pdata = playerdata

    print(data["mechs"])
    pdata["unlocked_mechs"] = data["mechs"]
    if "scrap" in data:
        pdata["scrap"] = data["scrap"]
    db.set_player_data(userid, pdata)
