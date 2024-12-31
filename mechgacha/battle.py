from mechstats import MechaStats, change_stats
class Mecha
    stats: MechaStats
    turn_buffs: MechaStats
    parts = []

    def __init__(self, stats: MechaStats):
        self.stats = stats

        self.turn_buffs = stats # clone?
        self.clear_buffs() 


        self.health = self.stats.heart  # starts off as stats.heart. when it hits 0 you lose
        self.heat = 0 # when this reaches stats.overheatability, reduce health by 1
        self.energy = 0 # increases by stats.power every turn


    def get_stat(self, statName):
        return stats[statName] + turn_buffs[statName]
    def clear_buffs(self):
        # todo
        for buff in self.turn_buffs:
            self.turn_buffs[buff] = 0

    def buff(self, statName, amount):
        self.turn_buffs[statName] += amount

    def take_damage():
        health -= 1


    

def create_mecha_from_inventory(inventory):
    stats = MechaStats()

    for item_id in inventory:
        item = all_items[item_id]

        # todo: see which stats the item changes
        change_stats(item, stats)

    return Mech(stats)

    
class MovementType:
    PunchIt = 0
    HoldSteady = 1
    PullBack = 2
    
class ActionType:
    Attack = 0
    Dodge = 1
    Block = 2
    CoolOff = 3

class Action:
    def __init__(self, type: ActionType, energy_spent: int):
        self.type = type
        self.energy_spent = energy_spent

def describe_range(range):
    if range <= 0:
        return "point-blank"
    elif range < 5:
        return "close"
    elif range < 10:
        return "medium"
    elif range >= 10:
        return "far"


class ConflictGame:
    def __init__(self, mechs):
        self.current_distance = 10
        self.mechs = []
        self.over = False

    def gameturn(self):
        self.start_turn()

        movement1, movement2 = self.choose_movement()
        self.resolve_movement(self.mechs[0], movement1)
        self.resolve_movement(self.mechs[1], movement2)
        
        self.after_movement()

        action1, action2 = self.choose_actions()
        self.resolve_action(self.mechs[0], action1, movement1, self.mechs[1], action2, movement2)
        self.resolve_action(self.mechs[1], action2, movement2, self.mechs[0], action1, movement1)

        self.end_of_turn(self.mechs[0], action1, movement1)
        self.end_of_turn(self.mechs[1], action2, movement2)
        
        

    def choose_movement():
        return (MovementType.PunchIt, MovementType.HoldSteady) # todo: UI

    def resolve_movement(self, mech, move):
        energy_spent = 1
        if move == MovementType.PunchIt:
            self.current_distance -= mech.movement # todo: randomness?
            mech.energy -= energy_spent
            mech.heat += energy_spent

        elif move == MovementType.PullBack:
            self.current_distance += mech.movement
            mech.energy -= energy_spent
            mech.heat += energy_spent
            mech.buff("evasion", 1)

        elif move == MovementType.HoldSteady:
            # no energy needed
            mech.buff("armor", 1)
            # mech.buff("conflict", 1) # Todo: buff ranged weapons
                
    def after_movement(self, mech1, movement1, mech2, movement2):

        if self.current_distance <= 0:
            self.current_distance = 0

            for move, mech in ((movement1, mech1), (movement2, mech2)):
                if move == MovementType.PunchIt: #Punch It boots conflict if you get close to an enemy
                    mech.buff("conflict", 1)


        if move == MovementType.PunchIt:
            self.current_distance -= mech.movement # todo: randomness?
            mech.energy -= energy_spent
            mech.heat += energy_spent


    def choose_action(self):
        return (Action(ActionTypes.Attack, 2), Action(ActionTypes.Block, 1))

    def successful_attack(self, attacking_mech, defending_mech):
        defending_mech.health -= 1

    def resolve_action(self, mech, my_action, your_movement, othermech, their_action, their_movement):
        my_action_type, energycost = my_action
        their_action_type, _ = their_action

        if my_action_type == Actions.Attack:
            if their_action_type == Actions.Attack or their_action_type == Actions.CoolOff:
                # attack automatically succeeds
                self.successful_attack(mech, othermech)
            else:

                your_dice = mech.getStat("conflict")
                their_dice = 0


                if your_movement.type == MovementType.PunchIt and current_distance <= 0:
                    your_dice += 1
                

                if their_action_type == Actions.Block:
                    their_dice = mech.getStat("armor")
                elif their_action_type == Actions.Dodge:
                    their_dice = mech.getStat("evasion")

                your_roll = # roll your_dice dice
                their_roll = # roll their_dice dice

                if your_roll > their_roll:
                    self.successful_attack(mech, othermech)
                else:                
                    # attack fails!
                    if their_action_type == Actions.Block:
                        self.on_successful_block()
                    if their_action_type == Actions.Dodge:
                        self.on_successful_dodge()
            
        if my_action_type == Actions.Block:
            if their_action_type != Actions.Attack:
                pass
                # mech.on_empty_block()

        if my_action_type == Actions.Dodge:
            if their_action_type != Actions.Attack:
                pass
                # mech.on_empty_dodge()

        if my_action_type == Actions.CoolOff:
            mech.heat -= mech.getStat("cooling") + energycost
            if mech.heat < 0:
                mech.heat = 0

        # actions cost heat
        if my_action_type != Actions.CoolOff:
            mech.heat += energycost
    
        mech.energy -= energycost


        
        
    def end_of_turn(self, mech, action, movement):
        # todo: status effects

        mech.clear_buffs()
        if mech.heat >= 10:
            mech.heat = 0
            mech.take_damage()

        if mech.health <= 0:
            # game over!
            self.over = True
        
