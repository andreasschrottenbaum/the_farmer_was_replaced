from move import *
from checkerboard_farm import checkerboard_farm

def tree_farm(amount):
  if (not num_unlocked(Unlocks.Trees)):    
    # simple bush farm
    while num_items(Items.Wood) < amount:
      if can_harvest():
        harvest()
        plant(Entities.Bush)
      
      if (num_unlocked(Unlocks.Expand) >= 2):
        move_to_next()
      else:
        move(North)
  else:
    # checkerboard farm
    checkerboard_farm(amount)