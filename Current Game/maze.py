from utilities import *
from trading import *
from movement import *


def start_maze():
    clear()
    hydrate()
    stay_energized()

    plant(Entities.Bush)

    if num_items(Items.Fertilizer) < 200:
        request_items(Items.Fertilizer, 1000)

    while get_entity_type() == Entities.Bush:
        use_item(Items.Fertilizer)


def solve_maze(amount):
    while num_items(Items.Gold) < amount:
        start_maze()

        # Solve the maze by following the left wall
        direction_index = 0
        while can_harvest() and get_entity_type() != Entities.Treasure:
            if get_entity_type() == Entities.Pumpkin:
                start_maze()
            direction_index = try_move_left(direction_index)

        harvest()
