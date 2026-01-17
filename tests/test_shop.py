import pytest

from gacha_tables import all_parts_list

class MockClient:
    pass

last_bot_message = None

class MockChannel:
    @staticmethod
    async def send(msg):
        global last_bot_message
        last_bot_message = msg
        return msg

class MockAuthor:
    id = "testid"
    display_name = "Testname"

class MockMessage:
    channel = MockChannel
    author = MockAuthor
    def __init__(self, message):
        self.content = message

def mock_playerdata(scrap=0):
    def _mock_playerdata(userid):
        return {"unlocked_mechs": ["loading","st_yietus"], 'ratoon_pulls':2, 'mech_pulls': 5, 'equipment': [1], "scrap": scrap}
    return _mock_playerdata

def mock_onepage_inventory(userid):
    return ["alto:unremarkable_legs", "alto:unremarkable_arms", "alto:unremarkable_body", "bee:artificial_satellite", "st_yietus:weird_lil_guy", "st_yietus:rotborn_stomper", "loading:hook_lash", "loading:gyrobomber"]

def mock_shop_items():
    return [all_parts_list["alto:unremarkable_legs"], all_parts_list["alto:unremarkable_arms"],all_parts_list["alto:unremarkable_body"]]

def mock_shop_info():
    return "The Repair Shop","An "under construction" sign bars the way, but if you squint you can see beyond it. Today, these items sit in front of the shop's messy entrance:"

async def test_shop_works(monkeypatch):

    scrap=2

    import db
    monkeypatch.setattr(db, "get_inventory_data", mock_onepage_inventory)
    monkeypatch.setattr(db, "get_player_data", mock_playerdata(scrap=scrap))

    import shop
    monkeypatch.setattr(shop, "get_shop_items", mock_shop_items)
    monkeypatch.setattr(shop, "get_shop_info", mock_shop_info)


    
    import inventory
    assert inventory.compute_inventory("testuser") == mock_onepage_inventory("testuser")

    assert (await shop.shop_command(MockMessage("m!shop"), "", MockClient())) == f'''
# **The Repair Shop**
An "under construction" sign bars the way, but if you squint you can see beyond it. Today, these items sit in front of the shop's messy entrance:
- `[1]` - Unremarkable Legs ★ - Hydraulic mecha legs, ready for painting, aftermarket tinkering, or full replacement. 
-# **     **LEGS
-# **     **Cost: **10 scrap**
- `[2]` - Unremarkable Arms ★ - Hydraulic mecha arms, ready for painting, aftermarket tinkering, or full replacement.
-# **     **ARMS
-# **     **Cost: **10 scrap**
- `[3]` - Unremarkable Body ★ - Hydraulic mecha body, ready for painting, aftermarket tinkering, or full replacement. 
-# **     **BODY
-# **     **Cost: **10 scrap**
- `[4]` An extra gacha pull, freshly refurbished!
-# **     **Cost: **5 scrap**

    You have {scrap} scrap. Nothing catch your eye? The shop will change its selection in 12 hours. To exchange scrap for an item, go bug Ratoon to stop painting his scrap with that sticky stuff and maybe I'll think about letting ya trade. Now scram!
'''.strip()

async def test_shop_redeeming_pulls(monkeypatch):

    import db
    monkeypatch.setattr(db, "get_inventory_data", mock_onepage_inventory)
    monkeypatch.setattr(db, "get_player_data", mock_playerdata(scrap=3))

    import shop
    monkeypatch.setattr(shop, "get_shop_items", mock_shop_items)

    # not enough scrap
    assert (await shop.shop_command(MockMessage("m!shop"), "4", MockClient())) == ("You don't have the 5 scrap needed to exchange for this item. You have 3 scrap. Use m!scrap to recycle parts in your inventory into scrap.")

    # yes enough scrap
    monkeypatch.setattr(db, "get_player_data", mock_playerdata(scrap=6))
    prev_pulls = db.get_player_data("testid")["mech_pulls"]

    assert (await shop.shop_command(MockMessage("m!shop"), "4", MockClient())) != ("You don't have the 5 scrap needed to exchange for this item. You have 3 scrap. Use m!scrap to recycle parts in your inventory into scrap.")

    # todo: check for pulls
    # check for set_player_data being called, then check its ["mech_pulls"]
    assert False


async def test_shop_buying(monkeypatch):

    import db
    monkeypatch.setattr(db, "get_inventory_data", mock_onepage_inventory)
    monkeypatch.setattr(db, "get_player_data", mock_playerdata(scrap=3))

    import shop
    monkeypatch.setattr(shop, "get_shop_items", mock_shop_items)

    import inventory
    assert inventory.compute_inventory("testuser") == mock_onepage_inventory("testuser")

    assert (await shop.shop_command(MockMessage("m!shop"), "1", MockClient())) == (f"You don't have the 5 scrap needed to exchange for the {mock_shop_items()[0].name}. You have 3 scrap. Use m!scrap to recycle parts in your inventory into scrap.")

    assert (await shop.shop_command(MockMessage("m!shop"), "2", MockClient())) == (f"You don't have the 5 scrap needed to exchange for the {mock_shop_items()[1].name}. You have 3 scrap. Use m!scrap to recycle parts in your inventory into scrap.")

    assert (await shop.shop_command(MockMessage("m!shop"), "3", MockClient())) == (f"You don't have the 5 scrap needed to exchange for the {mock_shop_items()[2].name}. You have 3 scrap. Use m!scrap to recycle parts in your inventory into scrap.")

    # now, test what happens when you have enough scrap
    monkeypatch.setattr(db, "get_player_data", mock_playerdata(scrap=100))

    # buy item 1
    assert (await shop.shop_command(MockMessage("m!shop"), "1", MockClient())) != (f"You don't have the 5 scrap needed to exchange for the {mock_shop_items()[0].name}. You have 3 scrap. Use m!scrap to recycle parts in your inventory into scrap.")

    # is item 1 in the user's inventory?
    # check for set_player_data being called, then check its inventory
    assert False

    # check for set_player_data being called, then check the amount of scrap
    assert False


    

