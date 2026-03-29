import pytest

class MockClient:
    pass

last_bot_message = None

class MockChannel:
    id = 1
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

def mock_playerdata(userid, mech_pulls=5, scrap=0):
    return {"unlocked_mechs": ["loading","st_yietus"], 'ratoon_pulls':2, 'mech_pulls': mech_pulls, 'equipment': [1], "scrap": scrap}

def mock_onepage_inventory(userid):
    return ["alto:unremarkable_legs", "alto:unremarkable_arms", "alto:unremarkable_body", "bee:artificial_satellite", "st_yietus:weird_lil_guy", "st_yietus:rotborn_stomper", "loading:hook_lash", "loading:gyrobomber"]

def mock_long_inventory(userid):
    return ["alto:unremarkable_legs", "alto:unremarkable_arms", "alto:unremarkable_body", "bee:artificial_satellite", "loading:knuckle_draggers", "st_yietus:weird_lil_guy", "st_yietus:rotborn_stomper", "loading:hook_lash", "loading:gyrobomber", "cheshire:stowaway_cheshire", "loading:elongated_segment_frame", "hillexed:findermech", "hillexed:starfish_mode_legs", "loading:big_jacket", "hillexed:findermech", "hillexed:glolf_patches", "hillexed:teeny_mechanized_legs", "loading:big_jacket", "loading:xr2", "triangle:intrinsic", "moonbug:blankets", "amutecrypt:thunderbirds_are_coming_out", "moonbug:insectoid_arm_array", "metanite64:golden_fiddle", "p_rker:helicoper_blades", "vel:retractible_swords", "moonbug:phase_shifter", "moonbug:insectoid_arm_array", "st_yietus:rotborn_stomper", "loading:lockjaw_needler", "moonbug:antennae", "moonbug:antennae", "loading:xr2", "st_yietus:rotborn_fist", "st_yietus:kitbash_kit_adaptor", "st_yietus:external_utility_pack", "hillexed:crochet_controls", "moonbug:emergency_grippers", "moonbug:legs_design_173", "moonbug:glitch_engine", "oneirocartographer:canopy_viewpoint", "hillexed:parabolic_block", "oneirocartographer:luminescent_core", "moonbug:covert_chassis", "moonbug:legs_design_173", "moonbug:emergency_grippers", "moonbug:antennae", "moonbug:glitch_engine", "moonbug:a.e.i.o.u", "moonbug:covert_chassis", "syl:sticky_fingers", "bytes:harvest_claw", "metanite64:cobras_roar", "renne:caustic_engine", "st_yietus:novelty_mug", "st_yietus:rotborn_stomper", "st_yietus:psychlink_mpi"]


async def test_inventory_message(monkeypatch):

    import db
    monkeypatch.setattr(db, "get_inventory_data", mock_onepage_inventory)
    monkeypatch.setattr(db, "get_player_data", mock_playerdata)
    monkeypatch.setattr(db, "update_data", lambda db_name,key,value: 5)
    
    import bot
    import inventory
    assert inventory.compute_inventory("testuser") == mock_onepage_inventory("testuser")

    expected_inventory = '''
**Your inventory:**
(Page 1/1)
- Unremarkable Legs ★ - Hydraulic mecha legs, ready for painting, aftermarket tinkering, or full replacement.
-# **     **`[1]` • LEGS, CLASSIC
- Unremarkable Arms ★ - Hydraulic mecha arms, ready for painting, aftermarket tinkering, or full replacement.
-# **     **`[2]` • ARMS, CLASSIC • **EQUIPPED**
- Unremarkable Body ★ - Hydraulic mecha body, ready for painting, aftermarket tinkering, or full replacement.
-# **     **`[3]` • BODY, CLASSIC
- Artificial Satellite ★★★ - A small artificial space structure (a satellite, space ship, etc) orbits your mech.
-# **     **`[4]` • COSMETIC, SPACE
- WEIRD LIL' GUY ★★★ - A bizarre, chimeric creature akin to an illumination has begun following you around. Its presence seems to spur your mech forwards, increasing its speed and giving it a short forward charge. Plus, it's cute.
-# **     **`[5]` • COSMETIC, MYTHICAL, WHIMSY
- ROTBORN STOMPERS ★★ - Sturdy weatherproofed legs. Slow and steady, but surprisingly agile. Capable of performing short leaps and dashes to clear obstacles or close the distance. Slightly reduces the effects of debuffs.
-# **     **`[6]` • LEGS, CLASSIC, MYTHICAL
- Hook Lash ★★ - A whip with a spinning metal weight at the end that applies a random debuff on hit.
-# **     **`[7]` • WEAPON, KINETIC
- Gyrobomber ★ - A gyroscopic cockpit with 300 degrees of visibility, to allow for the stabilization of the cockpit even as the body contorts.
-# **     **`[8]` • COCKPIT'''.strip()


    await bot.handle_commands(MockMessage("m!inventory"))
    assert last_bot_message == expected_inventory


post_pull_playerdata = None
last_modified_inventory = None
async def test_pull_message(monkeypatch, starting_pulls=5):
    import db
    monkeypatch.setattr(db, "get_inventory_data", mock_onepage_inventory)
    monkeypatch.setattr(db, "get_player_data", lambda userid: mock_playerdata(userid, mech_pulls=starting_pulls))
    monkeypatch.setattr(db, "update_data", lambda db_name,key,value: 5)
    

    # test pulling
    pre_pull_playerdata = db.get_player_data("testid")
    pre_pull_inventory = db.get_inventory_data("testid")
    num_pulls = pre_pull_playerdata["mech_pulls"]
    def set_player_data(user, data):
        global post_pull_playerdata
        post_pull_playerdata = data

    def set_inventory_data(userid, data):
        global last_modified_inventory
        last_modified_inventory = data

    monkeypatch.setattr(db, "set_player_data", set_player_data)
    monkeypatch.setattr(db, "set_inventory_data", set_inventory_data)


    import bot

    await bot.handle_commands(MockMessage("m!pull"))
    assert last_bot_message == f"""
Use m!pull <mech> to pull from their list! You can pull from: loading, st_yietus. You have {num_pulls} pulls.
 You can also use `m!pull ratoon` to get some mechs from Ratoon's gachapon. You have 2 pulls from Ratoon's gachapon."""

    await bot.handle_commands(MockMessage("m!pull loading"))
    assert "You pulled from loading and got..." in last_bot_message

    assert post_pull_playerdata["mech_pulls"] == num_pulls - 1
    assert len(last_modified_inventory) == len(pre_pull_inventory) + 1
    assert type(last_modified_inventory[-1]) is str

    

async def test_out_of_pulls_message(monkeypatch):
    import db
    monkeypatch.setattr(db, "get_inventory_data", mock_onepage_inventory)
    monkeypatch.setattr(db, "get_player_data", lambda userid: mock_playerdata(userid, mech_pulls=0))
    monkeypatch.setattr(db, "update_data", lambda db_name,key,value: 5)
    
    import bot
    await bot.handle_commands(MockMessage("m!pull"))
    assert last_bot_message == f"""
Use m!pull <mech> to pull from their list! You can pull from: loading, st_yietus. You have 0 pulls.
 You can also use `m!pull ratoon` to get some mechs from Ratoon's gachapon. You have 2 pulls from Ratoon's gachapon."""

    # test pulling with 0 pulls
    await bot.handle_commands(MockMessage("m!pull loading"))
    assert "You are out of pulls!" == last_bot_message

    # test negative pulls, in case they ever come up
    monkeypatch.setattr(db, "get_player_data", lambda userid: mock_playerdata(userid, mech_pulls=-1))
    await bot.handle_commands(MockMessage("m!pull loading"))
    assert "You are out of pulls!" == last_bot_message

async def test_progress_ratoon_message(monkeypatch):
    import db
    monkeypatch.setattr(db, "get_inventory_data", mock_onepage_inventory)
    monkeypatch.setattr(db, "get_player_data", lambda userid: mock_playerdata(userid, mech_pulls=0))
    monkeypatch.setattr(db, "update_data", lambda db_name,key,value: 5)

    import bot
    await bot.handle_commands(MockMessage("m!progress ratoon"))

    from gacha_tables import ratoon_pullable_mechs
    assert last_bot_message == f"\nYou have {len(ratoon_pullable_mechs) - 2} mechs remaining to pull"

async def test_progress_all_message(monkeypatch):
    import db
    monkeypatch.setattr(db, "get_inventory_data", mock_onepage_inventory)
    monkeypatch.setattr(db, "get_player_data", lambda userid: mock_playerdata(userid, mech_pulls=0))
    monkeypatch.setattr(db, "update_data", lambda db_name,key,value: 5)

    import bot
    await bot.handle_commands(MockMessage("m!progress all"))
    assert last_bot_message == """
## testname's global progress on the gacha pool:
**st_yietus**
> `[#-----------]` 2/24
**loading**
> `[##----------]` 2/10""".strip()

async def test_shop_no_crash(monkeypatch):
    import db
    monkeypatch.setattr(db, "get_inventory_data", mock_onepage_inventory)
    monkeypatch.setattr(db, "get_player_data", lambda userid: mock_playerdata(userid, mech_pulls=0, scrap=10))
    monkeypatch.setattr(db, "update_data", lambda db_name,key,value: 5)

    
    # shop description may spill over into two lines. If so, last_bot_message will not contain all of the shop dscription.
    # this captures outputs from both messages
    bot_output = ''
    class MockAppendingChannel:
        id = 1
        @staticmethod
        async def send(msg):
            nonlocal bot_output
            bot_output += msg
            return msg

    message = MockMessage("m!shop")
    message.channel = MockAppendingChannel()

    import bot
    await bot.handle_commands(message)

    assert "You have 10 scrap." in bot_output

    assert "An extra gacha pull, freshly refurbished!" in bot_output
    assert "★" in bot_output or "☆" in bot_output

async def test_shop(monkeypatch):
    import db
    monkeypatch.setattr(db, "get_inventory_data", mock_onepage_inventory)
    monkeypatch.setattr(db, "update_data", lambda db_name,key,value: 5)

    import bot
    import shop


    def set_player_data(user, data):
        global post_pull_playerdata
        post_pull_playerdata = data

    def set_inventory_data(userid, data):
        global last_modified_inventory
        last_modified_inventory = data

    monkeypatch.setattr(db, "set_player_data", set_player_data)
    monkeypatch.setattr(db, "set_inventory_data", set_inventory_data)


    # test exchanging for a refurbished gacha pull with no scrap
    command_to_get_refurbished_pull = f'm!shop {shop.num_shop_items+1}'
    initial_scrap_count = shop.NUM_SCRAP_FOR_ONE_PULL - 1
    monkeypatch.setattr(db, "get_player_data", lambda userid: mock_playerdata(userid, mech_pulls=0, scrap=initial_scrap_count))
    await bot.handle_commands(MockMessage(command_to_get_refurbished_pull))

    assert last_bot_message == f"You don't have the {shop.NUM_SCRAP_FOR_ONE_PULL} scrap needed to exchange for this item. You have {initial_scrap_count} scrap. Use m!scrap to recycle parts in your inventory into scrap."


    # test exchanging for a refurbished gacha pull with scrap
    initial_scrap_count = shop.NUM_SCRAP_FOR_ONE_PULL + 3
    monkeypatch.setattr(db, "get_player_data", lambda userid: mock_playerdata(userid, mech_pulls=0, scrap=initial_scrap_count))
    await bot.handle_commands(MockMessage(command_to_get_refurbished_pull))

    assert last_bot_message == f"You traded in {shop.NUM_SCRAP_FOR_ONE_PULL} scrap - enough to salvage a day's worth of pulls! You now have {initial_scrap_count-shop.NUM_SCRAP_FOR_ONE_PULL} scrap."
    assert post_pull_playerdata["scrap"] == initial_scrap_count-shop.NUM_SCRAP_FOR_ONE_PULL
    assert post_pull_playerdata["mech_pulls"] == 1


    initial_scrap_count = 1000 # hopefully enough to buy any item
    monkeypatch.setattr(db, "get_player_data", lambda userid: mock_playerdata(userid, mech_pulls=0, scrap=initial_scrap_count))

    # test buying an item
    previous_inventory = db.get_inventory_data("testid")
    await bot.handle_commands(MockMessage("m!shop 1"))

    assert "You traded in" in last_bot_message
    assert len(last_modified_inventory) == len(previous_inventory) + 1 # assert one more item has been added to inventory
    assert post_pull_playerdata["scrap"] < initial_scrap_count
