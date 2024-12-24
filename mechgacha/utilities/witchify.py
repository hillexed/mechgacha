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

    for i in range(len(invdata)):
        invdata[i].replace("warlock", "spellweaver")

    print(invdata)
        
    db.set_inventory_data(userid, invdata)

    pdata = db.get_player_data(userid)
    for i, mech in enumerate(pdata["unlocked_mechs"]):
        pdata["unlocked_mechs"][i] = mech.replace("warlock", "spellweaver")

    #print(pdata)
   # db.set_player_data(userid, pdata)

def transfer_inventories(ratoon_pulls = True, mech_pulls = True):
    users = get_all_users()
    for user in users:
        transfer_inventory(user)

transfer_inventories()
