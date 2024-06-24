from utilities import *
from trading import *
from movement import *


def pumpkin_farm(amount):
    farm_size = get_world_size() * get_world_size()

    while num_items(Items.Pumpkin) < amount:
        request_items(Items.Pumpkin_Seed, farm_size * 2)

        all_coords = get_all_coordinates()

        stay_energized()

        while len(all_coords):
            for coords in all_coords:
                move_to(coords[0], coords[1])

                hydrate()

                if can_harvest() and get_entity_type() != Entities.Pumpkin:
                    harvest()

                if get_ground_type() != Grounds.Soil:
                    till()

                if can_harvest():
                    all_coords.remove(coords)

                if get_entity_type() == None:
                    plant(Entities.Pumpkin)

        harvest()
