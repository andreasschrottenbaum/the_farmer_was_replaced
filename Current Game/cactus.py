from utilities import *
from trading import *
from movement import *


def cactus_farm(amount):
    clear()

    farm_size = get_world_size() * get_world_size()

    while num_items(Items.Cactus) < amount:
        stay_energized()
        request_items(Items.Cactus_Seed, farm_size)

        for i in range(farm_size):
            if get_ground_type() != Grounds.Soil:
                till()

            hydrate()

            if get_entity_type() == None:
                plant(Entities.Cactus)

            move_next()

        sort_cacti()
        move_to(get_world_size() - 1, get_world_size() - 1)
        harvest()


def sort_cacti():
    move_to(0, 0)

    swapped = False

    for horizontal in range(get_world_size()):
        for vertical in range(get_world_size()):
            if measure() > measure(East) and get_pos_x() != get_world_size() - 1:
                swap(East)
                swapped = True

            if measure() > measure(North) and get_pos_y() != get_world_size() - 1:
                swap(North)
                swapped = True
            move(North)
        move(East)

    if swapped:
        sort_cacti()
