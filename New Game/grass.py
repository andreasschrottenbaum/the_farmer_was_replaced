from utilities import *
from trading import *
from movement import *


def hay_farm(amount):
    while num_items(Items.Hay) < amount:
        hydrate()
        stay_energized(True)

        if get_ground_type() != Grounds.Turf:
            till()

        if can_harvest():
            harvest()

        move_next()
