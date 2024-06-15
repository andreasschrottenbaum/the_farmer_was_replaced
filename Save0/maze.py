from movement_functions import *

world_size = get_world_size()

def dfs():
    current_position = get_position()
    if current_position in visited:
        return False

    visited.add(current_position)

    if (can_harvest() and get_entity_type() == Entities.Treasure):
        harvest()
        return True

    for direction in get_possible_directions():
        move(direction)
        if dfs():
            return True
        move_back(direction)

    return False


while True:
  visited = set()
  clear()
  plant(Entities.Bush)
  use_item(Items.Fertilizer)
  use_item(Items.Water_Tank)

  if (num_items(Items.Fertilizer) < 200):
    trade(Items.Fertilizer, 1000)

  while True:
    if can_harvest() and get_entity_type() == Entities.Bush:
      use_item(Items.Fertilizer)
    elif can_harvest() and (get_entity_type() == Entities.Hedge or get_entity_type() == Entities.Treasure):
      break

  dfs()