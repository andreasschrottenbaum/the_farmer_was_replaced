from movement_functions import *
from harvest_functions import hydrate, plant_and_harvest

clear()


while True:
  plant_and_harvest(Entities.Bush)
  world_size = get_world_size()
  move_to_next()