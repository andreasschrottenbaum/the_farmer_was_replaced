from move import *
from utils import *

def carrot_farm(amount):
  empty_tanks = num_items(Items.Empty_Tank)
  filled_tanks = num_items(Items.Water_Tank)
  
  required_tanks = get_world_size() * get_world_size() - empty_tanks - filled_tanks
  
  # required_amount = (amount - num_items(Items.Carrot)) / num_unlocked(Unlocks.Carrots)
  request_items(Items.Carrot_Seed, amount)
  
  if (num_unlocked(Unlocks.Plant)):
    request_items(Items.Empty_Tank, required_tanks)
    if (get_water() < 0.2 and num_items(Items.Water_Tank) > 0):
      use_item(Items.Water_Tank)
  
  if (get_ground_type() != Grounds.Soil):
    till()

  if can_harvest():
    harvest()

  if (get_entity_type() == None):
    plant(Entities.Carrots)

  move_to_next()