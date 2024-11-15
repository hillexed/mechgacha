import db
import time
import threading
import logging
import datetime

max_ratoon_pulls = 4
max_mech_pulls = 10

from gacha_tables import all_parts_list

def get_all_users():
    return db.get_all_users_with_any_inventory()

def transfer_inventory(userid):
    invdata = db.get_inventory_data(userid)

    new_inventory = []

    for old_item in invdata:
        print(f"matching {old_item['name']}")
        item_title = old_item['name']
        found = False
        for itemid in all_parts_list:
            item = all_parts_list[itemid]
            if item.name.lower() == item_title.lower():
                new_inventory.append(itemid)
                found = True
                break
        if not found:
            print("ERROR!")
        
    print(new_inventory)
    db.set_inventory_data(userid, new_inventory)

def transfer_inventories(ratoon_pulls = True, mech_pulls = True):
    users = get_all_users()
    for user in users:
        transfer_inventory(user)

transfer_inventories()
