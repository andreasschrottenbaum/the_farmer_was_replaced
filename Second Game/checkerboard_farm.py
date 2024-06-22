from move import *

def checkerboard_farm(amount):
  while (num_items(Items.Wood) < amount):
    if can_harvest():
      harvest()

    if (get_pos_x() + get_pos_y()) % 2:
      entity = Entities.Tree
    else:
      entity = Entities.Bush

    if (get_entity_type() == None or get_entity_type() != entity):
      plant(entity)
    
    move_to_next()