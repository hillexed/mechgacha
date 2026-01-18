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

async def test_shop_works(monkeypatch):

    scrap=2

    import db
    monkeypatch.setattr(db, "get_inventory_data", mock_onepage_inventory)
    monkeypatch.setattr(db, "get_player_data", mock_playerdata(scrap=scrap))

    import shop
    monkeypatch.setattr(shop, "get_shop_items", mock_shop_items)


    
    import inventory
    assert inventory.compute_inventory("testuser") == mock_onepage_inventory("testuser")

    # the message changes with time, so .startswith() ensures the test doesn't fail because of the time of day
    assert (await shop.shop_command(MockMessage("m!shop"), "", MockClient())).startswith(f'''
# **The Repair Shop**
A "freshly renovated" sign beckons you into a wild array of half-disassembled bits and bobs with people at work all around you. Inside, several filing cabinets, car hoists, and horizontal painted doors have been combined to form display stands. Today, these items proudly sit on top of them:
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

    You have {scrap} scrap.'''.strip())

async def test_shop_redeeming_pulls(monkeypatch):

    import db
    monkeypatch.setattr(db, "get_inventory_data", mock_onepage_inventory)
    monkeypatch.setattr(db, "get_player_data", mock_playerdata(scrap=3))

    import shop
    monkeypatch.setattr(shop, "get_shop_items", mock_shop_items)

    # not enough scrap
    assert (await shop.shop_command(MockMessage("m!shop"), "4", MockClient())) == ("You don't have the 5 scrap needed to exchange for this item. You have 3 scrap. Use m!scrap to recycle parts in your inventory into scrap.")

    # yes enough scrap
    prev_scrap = 6
    monkeypatch.setattr(db, "get_player_data", mock_playerdata(scrap=prev_scrap))
    prev_pulls = db.get_player_data("testid")["mech_pulls"]

    def mock_set_playerdata(userid, playerdata):
        assert playerdata["mech_pulls"] == prev_pulls + 1
        assert playerdata["scrap"] == prev_scrap - 5
    monkeypatch.setattr(db, "set_player_data", mock_set_playerdata)

    assert (await shop.shop_command(MockMessage("m!shop"), "4", MockClient())) != ("You don't have the 5 scrap needed to exchange for this item. You have 3 scrap. Use m!scrap to recycle parts in your inventory into scrap.")


async def test_shop_buying(monkeypatch):

    import db
    monkeypatch.setattr(db, "get_inventory_data", mock_onepage_inventory)
    monkeypatch.setattr(db, "get_player_data", mock_playerdata(scrap=3))

    import shop
    monkeypatch.setattr(shop, "get_shop_items", mock_shop_items)

    import inventory

    # test if monkeypatching worked
    assert inventory.compute_inventory("testuser") == mock_onepage_inventory("testuser")

    # test buying a thing with no scrap
    assert (await shop.shop_command(MockMessage("m!shop"), "1", MockClient())) == (f"You don't have the 5 scrap needed to exchange for the {mock_shop_items()[0].name}. You have 3 scrap. Use m!scrap to recycle parts in your inventory into scrap.")

    assert (await shop.shop_command(MockMessage("m!shop"), "2", MockClient())) == (f"You don't have the 5 scrap needed to exchange for the {mock_shop_items()[1].name}. You have 3 scrap. Use m!scrap to recycle parts in your inventory into scrap.")

    assert (await shop.shop_command(MockMessage("m!shop"), "3", MockClient())) == (f"You don't have the 5 scrap needed to exchange for the {mock_shop_items()[2].name}. You have 3 scrap. Use m!scrap to recycle parts in your inventory into scrap.")

    # now, test what happens when you have enough scrap
    original_scrap = 100
    monkeypatch.setattr(db, "get_player_data", mock_playerdata(scrap=original_scrap))

    # prepare to test whether scrap is successfully changed when buying something
    def mock_set_playerdata(userid, returned_playerdata):
        assert returned_playerdata["scrap"] < original_scrap
    monkeypatch.setattr(db, "set_player_data", mock_set_playerdata)

    # prepare to test whether inventory successfully changes when buying something
    def mock_set_inventory(userid, inventory):
        assert len(inventory) == len(mock_onepage_inventory("testuser")) + 1
        assert inventory[-1] == mock_shop_items()[0].id
    monkeypatch.setattr(db, "set_inventory_data", mock_set_inventory)

    # buy item 1, triggering previous monkeypatch tests
    buymessage = await shop.shop_command(MockMessage("m!shop"), "1", MockClient())

    # message split into two chunks like this to avoid the randomization
    assert "You traded in 10 scrap and received a" in buymessage
    assert "**Unremarkable Legs**! You now have 90 scrap." in buymessage
