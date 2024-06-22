from utils import *
from move import *


def get_all_positions():
  pumpkin_positions = []
  
  old_world_size = get_world_size()
  for x in range(old_world_size + 1):
    for y in range(old_world_size + 1):
      pumpkin_positions.append((x, y))
  
  return pumpkin_positions

def pumpkin_farm(amount):
  pumpkin_positions = get_all_positions()

  while (num_items(Items.Pumpkin) < amount):
    keep_energized()
    
    for position in pumpkin_positions:
      move_to(position[0], position[1])

      if (num_items(Items.Pumpkin_Seed) < 100):
        request_items(Items.Pumpkin_Seed, 100)

      if (can_harvest() and get_entity_type() != Entities.Pumpkin):
        harvest()

      if (can_harvest() and get_entity_type() == Entities.Pumpkin):
        pumpkin_positions.remove(position)

      if (can_harvest() and (len(pumpkin_positions) == 0)):
        harvest()
        pumpkin_positions = get_all_positions()
        return
      
      if (get_ground_type() != Grounds.Soil):
        till()
      
      if (get_entity_type() == None):
        plant(Entities.Pumpkin)
        
        if (get_water() < 0.2 and num_items(Items.Water_Tank) > 0):
          use_item(Items.Water_Tank)
  
  clear()
