import db
import time
import threading
import logging
import datetime

import inventory

max_ratoon_pulls = 4
max_mech_pulls = 10


def get_all_users():
    return db.get_all_users_with_any_inventory()

def add_pulls(userid, mech_pulls = 1, ratoon_pulls = 0):
    playerdata = get_playerdata(userid)
    if playerdata["ratoon_pulls"] < max_ratoon_pulls:
        playerdata["ratoon_pulls"] += ratoon_pulls

    if playerdata["mech_pulls"] < max_mech_pulls:
        playerdata["mech_pulls"] += mech_pulls

    db.set_player_data(userid, playerdata)

def regenerate_everyones_pulls(ratoon_pulls = True, mech_pulls = True):
    users = get_all_users()
    for userid in users:
        ratoon_pulls_per_day = 1/14 + 0.001 # this is a very silly way to make it one full pull every two weeks. the 0.001 ensures we won't get stuck with 0.999999998
        mech_pulls_per_day = 1 
        add_pulls(userid, mech_pulls_per_day, ratoon_pulls_per_day)

def get_playerdata(username):
    playerdata = db.get_player_data(username)

    if playerdata is None:
        inventory.add_new_player(username)
        playerdata = db.get_player_data(username)

    return playerdata

def regen_pulls_thread():

    while True:

        '''
        # on a monday give everyone a regeneration

        # find next monday
        today_weekday = datetime.datetime.now().weekday() # monday = 0, sunday = 6
        days_till_monday = 7 - today_weekday
        next_regen_day = datetime.datetime.now().date() + datetime.timedelta(days=days_till_monday)

        # compute how long until next midnight
        next_monday_midnight  = datetime.datetime.combine(next_regen_day, datetime.datetime.min.time())
        secs_till_next_monday = (next_monday_midnight - datetime.datetime.now()).total_seconds()
        '''
        
        # regen everyone once a day at midnight
        tomorrow_midnight = datetime.datetime.combine(datetime.datetime.today() + datetime.timedelta(days=1), datetime.datetime.min.time())
        secs_till_next_day = (tomorrow_midnight - datetime.datetime.now()).total_seconds()
        
        logging.info(f"Sleeping {secs_till_next_day} seconds until next midnight...")
        time.sleep(secs_till_next_day)
        logging.info("Regenerating pulls!")
        regenerate_everyones_pulls()

def start_timer():
    logging.info("Begin timer")
    timer = threading.Thread(target=regen_pulls_thread, daemon=True)
    timer.start()
    
