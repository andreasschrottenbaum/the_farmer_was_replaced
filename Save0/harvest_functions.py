def hydrate():
	waterLevel = get_water()
	if (waterLevel < 0.2):
		use_item(Items.Water_Tank)
		

def make_ground(type):
	currentGround = get_ground_type()
	if type == currentGround:
		return
	till()

def buy_seeds(item):
	if get_entity_type() != item and num_items(item) == 0:
		trade(item)

def plant_and_harvest(item, shouldHarvest = True):
	quick_print(measure())

	if not can_harvest() and get_entity_type() != None:
		return


	if shouldHarvest:
		harvest()

	if item == Entities.Carrots:
		buy_seeds(Items.Carrot_Seed)
		make_ground(Grounds.Soil)
		plant(Entities.Carrots)
	
	elif item == Entities.Bush:
		make_ground(Grounds.Turf)
		plant(Entities.Bush)
		
	elif item == Entities.Grass:
		make_ground(Grounds.Turf)
		plant(Entities.Grass)

	elif item == Entities.Tree:
		make_ground(Grounds.Turf)
		plant(Entities.Tree)

	elif item == Entities.Pumpkin:
		buy_seeds(Items.Pumpkin_Seed)
		make_ground(Grounds.Soil)
		plant(Entities.Pumpkin)

	elif item == Entities.Sunflower:
		buy_seeds(Items.Sunflower_Seed)
		make_ground(Grounds.Soil)
		plant(Entities.Sunflower)