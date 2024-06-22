from utils import *
from move import *

def wheat_farm(amount):
  keep_energized()
  # Are water tanks really an improvement?
  
  # empty_tanks = num_items(Items.Empty_Tank)
  # filled_tanks = num_items(Items.Water_Tank)
  
  # required_tanks = get_world_size() * get_world_size() - empty_tanks - filled_tanks
  
  # if (num_unlocked(Unlocks.Plant)):
  #   request_items(Items.Empty_Tank, required_tanks)
    
  while num_items(Items.Hay) < amount:
    if can_harvest():
      harvest()
      if (num_unlocked(Unlocks.Plant) and get_entity_type() != Entities.Grass):
        plant(Entities.Grass)
    
    if (num_unlocked(Unlocks.Expand) >= 2):
      move_to_next()
    elif (num_unlocked(Unlocks.Expand) == 1):
      move(North)
    
    
