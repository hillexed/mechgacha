import db
import inventory

def get_playerdata(username):
    playerdata = db.get_player_data(username)

    if playerdata is None:
        inventory.add_new_player(username)
        playerdata = db.get_player_data(username)

    # accounting for previous versions
    # if not hasattr(playerdata, "equipment"):
    #     playerdata["equipment"] = []

    return playerdata
    # sample playerdata = {"unlocked_mechs": ['alto'], 'ratoon_pulls':2, 'mech_pulls': 5}
