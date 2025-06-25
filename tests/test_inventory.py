import pytest

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

def mock_playerdata(userid):
    return {"unlocked_mechs": ["loading","st_yietus"], 'ratoon_pulls':2, 'mech_pulls': 5, 'equipment': [1], "scrap": 0}

def mock_onepage_inventory(userid):
    return ["alto:unremarkable_legs", "alto:unremarkable_arms", "alto:unremarkable_body", "bee:artificial_satellite", "st_yietus:weird_lil_guy", "st_yietus:rotborn_stomper", "loading:hook_lash", "loading:gyrobomber"]

def mock_long_inventory(userid):
    return ["alto:unremarkable_legs", "alto:unremarkable_arms", "alto:unremarkable_body", "bee:artificial_satellite", "loading:knuckle_draggers", "st_yietus:weird_lil_guy", "st_yietus:rotborn_stomper", "loading:hook_lash", "loading:gyrobomber", "cheshire:stowaway_cheshire", "loading:elongated_segment_frame", "hillexed:findermech", "hillexed:starfish_mode_legs", "loading:big_jacket", "hillexed:findermech", "hillexed:glolf_patches", "hillexed:teeny_mechanized_legs", "loading:big_jacket", "loading:xr2", "triangle:intrinsic", "moonbug:blankets", "amutecrypt:thunderbirds_are_coming_out", "moonbug:insectoid_arm_array", "metanite64:golden_fiddle", "p_rker:helicoper_blades", "vel:retractible_swords", "moonbug:phase_shifter", "moonbug:insectoid_arm_array", "st_yietus:rotborn_stomper", "loading:lockjaw_needler", "moonbug:antennae", "moonbug:antennae", "loading:xr2", "st_yietus:rotborn_fist", "st_yietus:kitbash_kit_adaptor", "st_yietus:external_utility_pack", "hillexed:crochet_controls", "moonbug:emergency_grippers", "moonbug:legs_design_173", "moonbug:glitch_engine", "oneirocartographer:canopy_viewpoint", "hillexed:parabolic_block", "oneirocartographer:luminescent_core", "moonbug:covert_chassis", "moonbug:legs_design_173", "moonbug:emergency_grippers", "moonbug:antennae", "moonbug:glitch_engine", "moonbug:a.e.i.o.u", "moonbug:covert_chassis", "syl:sticky_fingers", "bytes:harvest_claw", "metanite64:cobras_roar", "renne:caustic_engine", "st_yietus:novelty_mug", "st_yietus:rotborn_stomper", "st_yietus:psychlink_mpi"]


async def test_inventory(monkeypatch):

    import db
    monkeypatch.setattr(db, "get_inventory_data", mock_onepage_inventory)
    monkeypatch.setattr(db, "get_player_data", mock_playerdata)
    
    import inventory
    assert inventory.compute_inventory("testuser") == mock_onepage_inventory("testuser")

    expected_inventory = '''
**Your inventory:**
(Page 1/1)
- Unremarkable Legs ★ - Hydraulic mecha legs, ready for painting, aftermarket tinkering, or full replacement. 
-# **     **`[1]` • LEGS
- Unremarkable Arms ★ - Hydraulic mecha arms, ready for painting, aftermarket tinkering, or full replacement.
-# **     **`[2]` • ARMS • **EQUIPPED**
- Unremarkable Body ★ - Hydraulic mecha body, ready for painting, aftermarket tinkering, or full replacement. 
-# **     **`[3]` • BODY
- Artificial Satellite ★★★ - A small artificial space structure (a satellite, space ship, etc) orbits your mech.
-# **     **`[4]` • COSMETIC
- WEIRD LIL' GUY ★★★ - A bizarre, chimeric creature akin to an illumination has begun following you around. Its presence seems to spur your mech forwards, increasing its speed and giving it a short forward charge. Plus, it's cute.
-# **     **`[5]` • COSMETIC
- ROTBORN STOMPERS ★★ - Sturdy weatherproofed legs. Slow and steady, but surprisingly agile. Capable of performing short leaps and dashes to clear obstacles or close the distance. Slightly reduces the effects of debuffs.
-# **     **`[6]` • LEGS
- Hook Lash ★★ - A whip with a spinning metal weight at the end that applies a random debuff on hit
-# **     **`[7]` • WEAPON
- Gyrobomber ★ - A gyroscopic cockpit with 300 degrees of visibility to allow for the stabilization of the cockpit even as the body contorts.
-# **     **`[8]` • COCKPIT'''.strip()

    assert await inventory.inventory_command(MockMessage("m!inventory"), "", MockClient())  == expected_inventory

async def test_inventory_pagination(monkeypatch):

    import db
    monkeypatch.setattr(db, "get_inventory_data", mock_long_inventory)
    monkeypatch.setattr(db, "get_player_data", mock_playerdata)
    
    import inventory

    message = MockMessage("m!inventory")

    output = await inventory.inventory_command(message, "", MockClient()) 
    assert len(output) < 2000
    assert "(Page 1/9)" in output

    output = await inventory.inventory_command(message, "2", MockClient()) 
    assert len(output) < 2000
    assert "(Page 2/9)" in output

    output = await inventory.inventory_command(message, "9", MockClient()) 
    assert len(output) < 2000
    assert "(Page 9/9)" in output

    # pages beyond current one
    output = await inventory.inventory_command(message, "100000", MockClient()) 
    assert len(output) < 2000
    assert "(Page 9/9)" in output




async def test_inventory_filtering(monkeypatch):

    import db
    monkeypatch.setattr(db, "get_inventory_data", mock_onepage_inventory)
    monkeypatch.setattr(db, "get_player_data", mock_playerdata)

    
    import inventory
    assert inventory.compute_inventory("testuser") == mock_onepage_inventory("testuser")

    message = MockMessage("m!inventory")

    expected_inventory = '''
**Your inventory:**
(Page 1/1)
- Unremarkable Legs ★ - Hydraulic mecha legs, ready for painting, aftermarket tinkering, or full replacement. 
-# **     **`[1]` • LEGS
- Unremarkable Arms ★ - Hydraulic mecha arms, ready for painting, aftermarket tinkering, or full replacement.
-# **     **`[2]` • ARMS • **EQUIPPED**
- Unremarkable Body ★ - Hydraulic mecha body, ready for painting, aftermarket tinkering, or full replacement. 
-# **     **`[3]` • BODY
- Artificial Satellite ★★★ - A small artificial space structure (a satellite, space ship, etc) orbits your mech.
-# **     **`[4]` • COSMETIC
- WEIRD LIL' GUY ★★★ - A bizarre, chimeric creature akin to an illumination has begun following you around. Its presence seems to spur your mech forwards, increasing its speed and giving it a short forward charge. Plus, it's cute.
-# **     **`[5]` • COSMETIC
- ROTBORN STOMPERS ★★ - Sturdy weatherproofed legs. Slow and steady, but surprisingly agile. Capable of performing short leaps and dashes to clear obstacles or close the distance. Slightly reduces the effects of debuffs.
-# **     **`[6]` • LEGS
- Hook Lash ★★ - A whip with a spinning metal weight at the end that applies a random debuff on hit
-# **     **`[7]` • WEAPON
- Gyrobomber ★ - A gyroscopic cockpit with 300 degrees of visibility to allow for the stabilization of the cockpit even as the body contorts.
-# **     **`[8]` • COCKPIT'''.strip()

    assert await inventory.inventory_command(message, "", MockClient()) == expected_inventory
    assert await inventory.inventory_command(message, "5", MockClient()) == expected_inventory # no such page 5

    await inventory.inventory_command(message, "asdhfsadfh", MockClient()) # shouldn't raise any exceptions

    assert await inventory.inventory_command(message, "3 stars", MockClient()) == '''
**Your inventory:**
- Artificial Satellite ★★★ - A small artificial space structure (a satellite, space ship, etc) orbits your mech.
-# **     **`[4]` • COSMETIC
- WEIRD LIL' GUY ★★★ - A bizarre, chimeric creature akin to an illumination has begun following you around. Its presence seems to spur your mech forwards, increasing its speed and giving it a short forward charge. Plus, it's cute.
-# **     **`[5]` • COSMETIC'''.strip()


    assert await inventory.inventory_command(message, "legs", MockClient()) == '''
**Your inventory:**
- Unremarkable Legs ★ - Hydraulic mecha legs, ready for painting, aftermarket tinkering, or full replacement. 
-# **     **`[1]` • LEGS
- ROTBORN STOMPERS ★★ - Sturdy weatherproofed legs. Slow and steady, but surprisingly agile. Capable of performing short leaps and dashes to clear obstacles or close the distance. Slightly reduces the effects of debuffs.
-# **     **`[6]` • LEGS'''.strip()

    assert await inventory.inventory_command(message, "unequipped cosmetic 3 stars", MockClient()) == '''
**Your inventory:**
- Artificial Satellite ★★★ - A small artificial space structure (a satellite, space ship, etc) orbits your mech.
-# **     **`[4]` • COSMETIC
- WEIRD LIL' GUY ★★★ - A bizarre, chimeric creature akin to an illumination has begun following you around. Its presence seems to spur your mech forwards, increasing its speed and giving it a short forward charge. Plus, it's cute.
-# **     **`[5]` • COSMETIC'''.strip()

    assert await inventory.inventory_command(message, "unequipped arms", MockClient()) == '''
**You have nothing in your inventory!** 
 Use m!pull ratoon to get some mechs from Ratoon's gachapon, then m!pull <mech> to pull from their list!'''.strip()
