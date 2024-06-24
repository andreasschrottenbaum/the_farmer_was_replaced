from utilities import *
from trading import *
from movement import *


def wood_farm(amount):
    while num_items(Items.Wood) < amount:
        if hydrate(True):
            stay_energized(True)

        if can_harvest():
            harvest()

        if get_entity_type() == None or get_entity_type() == Entities.Grass:
            if (get_pos_x() + get_pos_y()) % 2 or not num_unlocked(Unlocks.Trees):
                plant(Entities.Bush)
            else:
                plant(Entities.Tree)

        move_next()
