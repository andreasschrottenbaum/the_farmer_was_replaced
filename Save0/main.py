from reset_position import reset_pos
from harvest_functions import hydrate, plant_and_harvest

reset_pos()

while True:
	for colCount in range(get_world_size()):
		for rowCount in range(get_world_size()):
			item = Entities.Grass

			if rowCount == get_world_size() - 1:
				item = Entities.Sunflower

			plant_and_harvest(item)

			hydrate()

			move(North)
		move(East)
