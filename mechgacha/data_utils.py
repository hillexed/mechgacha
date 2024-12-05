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

def paginate(input_array: list[str], char_limit: int) -> list[list[str]]:
    paginated_array = [[]]
    for idx, x in enumerate(input_array):
      if(len(x) > char_limit):
          raise ValueError(f'Index {idx} is longer then a single page')
      if(len(x) + sum([len(x) for x in paginated_array[-1]]) > char_limit):
          paginated_array.append([])
      paginated_array[-1].append(x)
    return paginated_array