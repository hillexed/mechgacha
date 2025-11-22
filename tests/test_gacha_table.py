import pytest  

#from mechgacha import gacha_mechanics

def test_gacha_tables():

    seen_ids = set()

    import gacha_tables

    assert len(gacha_tables.all_parts_list) > 1

    for mech in gacha_tables.all_mechs:
        assert len(mech.loot) > 1

        for item in mech.loot:
            assert type(item.name) is str
            assert ":" in item.id
            assert item.stars in (1,2,3,4,5)

            assert item.id not in seen_ids # no duplicate IDs
            seen_ids.add(item.id)

            if "bodyplan" in item.tags:
                bodyparts = item.extradata
                assert bodyparts is not None
                assert type(bodyparts) is dict


def test_item_lengths():

    import gacha_tables
    for mech in gacha_tables.all_mechs:
        for item in mech.loot:
            assert len(item.description) <= 300
            assert len(item.name) > 1
            assert len(item.name) <= 62
