from gacha_tables import all_parts_list, all_mechs
import sys
from random import randrange

def debug_player_all(id):
    mech_str = "["
    for mech in all_mechs:
        mech_str += f'"{mech.username}",'
    mech_str = mech_str[:-1] + "]"
    item_str = "["
    for item in all_parts_list:
        item_str += f'"{item}",'
    item_str = item_str[:-1] + "]"
    random_mech = [randrange(0, len(all_parts_list)-1) for i in range(20)]
    file = open(r"db_data/debug_files/fully_unlocked.sql", "w") 
    file.writelines([f'update playerdata set data=\'{{"unlocked_mechs":{mech_str},"ratoon_pulls": 1000, "mech_pulls":1000, "equipment":{random_mech}}}\' where name=\'178116262390398976\';',
                     f'update inventory set data=\'{item_str}\' where name=\'178116262390398976\';',
                     ])
    

def generate_debug_files():
    id = sys.argv[1]
    debug_player_all(id)

generate_debug_files()