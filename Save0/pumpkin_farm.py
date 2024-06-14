from reset_position import *
from harvest_functions import *

reset_pos()

while True:
	for colCount in range(get_world_size()):
		for rowCount in range(get_world_size()):
			item = Entities.Pumpkin

			if rowCount == get_world_size() - 1 and colCount == get_world_size() - 1:
				plant_and_harvest(item)
			else:
				plant_and_harvest(item, False)

			hydrate()

			move(North)
		move(East)
