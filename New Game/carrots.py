from utilities import *
from trading import *
from movement import *


def carrot_farm(amount):
    farm_size = get_world_size() * get_world_size()

    while num_items(Items.Carrot) < amount:
        request_items(Items.Carrot_Seed, farm_size)
        stay_energized(True)

        for i in range(farm_size):
            hydrate()

            if can_harvest():
                harvest()

            if get_ground_type() != Grounds.Soil:
                till()

            if get_entity_type() == None:
                plant(Entities.Carrots)

            move_next()
