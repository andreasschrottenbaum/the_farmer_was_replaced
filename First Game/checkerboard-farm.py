from Save0.harvest_functions import hydrate, plant_and_harvest
item = Entities.Grass
altItem = Entities.Grass
clear()

while True:
  for colCount in range(get_world_size()):
    for rowCount in range(get_world_size()):
      if (colCount + rowCount) % 2 == 0:
        plant_and_harvest(item)
      else:
        plant_and_harvest(altItem)

      hydrate()
      move(North)
    move(East)
