import sqlite3
import json
import os

DB_DIRECTORY = 'db_data'

database_filename = 'mechgacha.sqlite'

def _get_db_filename():
    # only used for admin "download database" command
    return os.path.join(DB_DIRECTORY,database_filename)

def get_db_connection():
    path = os.path.join(DB_DIRECTORY,database_filename)
    try:
        conn = sqlite3.connect(path)
        conn.execute('pragma journal_mode=wal')
        return conn
    except:
        print(f"failed to open database at {path}")
        raise

def create_table_if_not_made(tablename):
    # WARNING: TABLENAME IS SQL INJECTABLE. DON'T ALLOW USER SUBMITTED TABLE NAMES
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {tablename}
               (name text PRIMARY KEY NOT NULL, data text NOT NULL, version real)''')
    conn.commit()
    cursor.close()


def get_data(name, tablename="players"):
    # WARNING: TABLENAME IS SQL INJECTABLE. DON'T ALLOW USER SUBMITTED TABLE NAMES
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {tablename} WHERE name=?",(name, ))
    db_entry= cursor.fetchone()
    cursor.close()

    if db_entry is not None:
        player_name, player_data, version = db_entry
        return json.loads(player_data)

def create_new_entry(name, data, tablename="players"):
    # WARNING: TABLENAME IS SQL INJECTABLE
    version = 1
    data = json.dumps(data)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {tablename} VALUES (?, ?, ?)",(name, data, version))
    conn.commit()
    cursor.close()

def update_data(name, data, tablename="players"):
    # WARNING: TABLENAME IS SQL INJECTABLE
    version = 1
    data = json.dumps(data)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"UPDATE {tablename} SET data=? WHERE name=?",(data, name))
    conn.commit()
    cursor.close()

def delete_data(name, tablename="players"):
    # WARNING: TABLENAME IS SQL INJECTABLE
    version = 1
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {tablename} WHERE name=?",(name, ))
    conn.commit()
    cursor.close()

def create_gamedata_table_if_not_made():
    create_table_if_not_made("gamedata")

def get_game_data(name):
    create_gamedata_table_if_not_made()
    return get_data(name, tablename="gamedata")

def set_game_data(name, data):
    create_gamedata_table_if_not_made()
    if get_data(name, tablename="gamedata") is None:
        create_new_entry(name, data, tablename="gamedata")
    else:
        update_data(name, data, tablename="gamedata")

def delete_game_data(settingname):
    create_gamedata_table_if_not_made()
    return delete_data(settingname, tablename="gamedata")


def create_inventory_table_if_not_made():
    create_table_if_not_made("inventory")

def get_inventory_data(name):
    create_inventory_table_if_not_made()
    return get_data(name, tablename="inventory")

def set_inventory_data(name, data):
    create_inventory_table_if_not_made()
    if get_data(name, tablename="inventory") is None:
        create_new_entry(name, data, tablename="inventory")
    else:
        update_data(name, data, tablename="inventory")

def delete_inventory_data(settingname):
    create_inventory_table_if_not_made()
    return delete_data(settingname, tablename="inventory")

def get_users_with_empty_inventory():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT name,data FROM inventory WHERE data='\"[]\"' Or data=''")
    userdata= cursor.fetchall()
    cursor.close()

    if userdata is not None:
        user_ids = [name for name,data in userdata]
        return user_ids


def get_all_users_with_any_inventory():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT name, data FROM inventory")
    userdata= cursor.fetchall()
    cursor.close()
    if userdata is not None:
        user_ids = [name for name,data in userdata]
        return user_ids




def create_playerdata_table_if_not_made():
    create_table_if_not_made("playerdata")

def get_player_data(name):
    create_playerdata_table_if_not_made()
    return get_data(name, tablename="playerdata")

def set_player_data(name, data):
    create_playerdata_table_if_not_made()
    if get_data(name, tablename="playerdata") is None:
        create_new_entry(name, data, tablename="playerdata")
    else:
        update_data(name, data, tablename="playerdata")

def delete_player_data(settingname):
    create_playerdata_table_if_not_made()
    return delete_data(settingname, tablename="playerdata")
