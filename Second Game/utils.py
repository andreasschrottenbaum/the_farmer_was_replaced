from wheat_farm import wheat_farm
from tree_farm import tree_farm
from carrot_farm import carrot_farm
from pumpkin_farm import pumpkin_farm
from maze import solve_maze
from cactus_farm import cactus_farm
from dinosaur import dino_farm
from sunflower_farm import sunflower_farm

def request_items(item, amount):
  if amount <= 0:
    return
  
  if (amount - num_items(item) <= 0):
    return True
     
  tradable_items = [Items.Pumpkin_Seed, Items.Carrot_Seed, Items.Cactus_Seed, Items.Sunflower_Seed, Items.Egg, Items.Empty_Tank, Items.Fertilizer]
  farmable_items = [Items.Pumpkin, Items.Carrot, Items.Cactus, Items.Power, Items.Hay, Items.Wood, Items.Bones, Items.Gold]

  if not(item in tradable_items or item in farmable_items):
    print("Invalid item", item)
    return False

  if num_items(item) < amount and item in tradable_items:
    requirements = get_cost(item)
      
    for requirement in requirements:
      request_items(requirement, requirements[requirement] * amount)

    trade(item, amount - num_items(item))
  elif item in farmable_items:
    farm_items(item, amount)
 
  if num_items(item) < amount:
    requirements = get_cost(item)
      
    for requirement in requirements:
      request_items(requirement, requirements[requirement] * amount)

    return
  
def farm_items(item, amount):
  farms = {
    Items.Bones: dino_farm,
    Items.Cactus: cactus_farm,
    Items.Carrot: carrot_farm,
    Items.Hay: wheat_farm,
    Items.Power: sunflower_farm,
    Items.Pumpkin: pumpkin_farm,
    Items.Wood: tree_farm,
    Items.Gold: solve_maze,
  }
  
  farm = farms[item]
  while num_items(item) < amount:
    farm(amount)


def purchase_upgrade(upgrade):
  requirements = get_cost(upgrade)

  quick_print('Purchasing', upgrade, 'level', num_unlocked(upgrade) + 1)

  for requirement in requirements:
    request_items(requirement, requirements[requirement])

  unlock(upgrade)

def keep_energized():
  if (num_unlocked(Unlocks.Sunflowers) < 1):
    return
  
  if (num_items(Items.Power) < 100):
    request_items(Items.Power, 1000)
