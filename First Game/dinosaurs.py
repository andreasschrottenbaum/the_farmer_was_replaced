from movement_functions import *
from harvest_functions import *

trade(Items.Egg, 10)

world_size = get_world_size()

while True:
  plant_and_harvest(Entities.Dinosaur)
  move_to_next()