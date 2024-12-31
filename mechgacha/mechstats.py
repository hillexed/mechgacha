from gacha_mechanics import TagType, Item
from dataclasses import dataclass

class MechaStat:
    letter = L
    

movement = MechaStat("M")
evasion = MechaStat("E")
conflict = MechaStat("C")
heart = MechaStat("H")
armor = MechaStat("A")

power = MechaStat("P")
overheatability = MechaStat("O")
cooling = MechaStat("C")

@dataclass
class MechaStats:
    movement = 5
    evasion = 5 # affects dodging
    conflict = 5 # affects damage
    heart = 5   # HP
    armor = 5 # affects blocking
    
    power = 1 # energy per turn
    overheatability = 10 # when heat reaches this number, take 1 damage
    cooling = 3 # when you cool off, remove this much heat


simple_stat_tags = {
"limber": "+M-A"
"brutal": "+C-H"
"minimalist": "+E-A"
"delicate": "+E-H"
"hollow": "+A-H"

}
effect_to_simple_tag = {key: tagname for tagname in simple_stat_tags}

def simple_tag(plus: MechaStat, minus: MechaStat):
    tagEffect = f"+{plus}-{minus}"
    if tagEffect in simple_stat_tags:
        return 

    return 

def only_one_tag(stats, tag):
    if tag == "power":
        stats.power += 1
    elif tag == "arms":
        stats.armor += 1
        stats.evasion -= 1
    elif tag == "legs":
        stats.evasion += 1
        stats.armor -= 1
    elif tag == "weapon":
        stats.conflict += 1
        stats.movement -= 1
    elif tag == "body":
        stats.movement += 1
        stats.conflict -= 1
    elif tag == "back":
        stats.movement += 1
        stats.evasion -= 1
    elif tag == "cockpit":
        stats.heart += 1
        stats.armor -= 1
    elif tag == "cosmetic":
        pass
    elif tag == "bodyplan":
        pass


def change_stats(stats:MechaStats, item: Item):
    # called to apply items' stat changes
    for tag in item.tags:
        if tag == "power":
            stats.power += 1
    
    # defaults, if no other tags are applied
    if len(item.tags) == 1:
        only_one_tag(stats, item.tags[0])
        return
