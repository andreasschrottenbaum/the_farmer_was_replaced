from maze import solve_maze
from sunflowers import sunflower_farm
from pumpkins import pumpkin_farm
from carrots import carrot_farm
from wood import wood_farm
from grass import hay_farm
from dinosaurs import dino_farm
from cactus import cactus_farm


def request_items(item, amount):
    if num_items(item) >= amount:
        return
    if item == Items.Gold:
        solve_maze(amount)
    elif item == Items.Power:
        sunflower_farm(amount)
    elif item == Items.Pumpkin:
        pumpkin_farm(amount)
    elif item == Items.Carrot:
        carrot_farm(amount)
    elif item == Items.Wood:
        wood_farm(amount)
    elif item == Items.Hay:
        hay_farm(amount)
    elif item == Items.Bones:
        dino_farm(amount)
    elif item == Items.Cactus:
        cactus_farm(amount)
    elif item == Items.Carrot_Seed:
        buy(Items.Carrot_Seed, amount)
    elif item == Items.Pumpkin_Seed:
        buy(Items.Pumpkin_Seed, amount)
    elif item == Items.Fertilizer:
        buy(Items.Fertilizer, amount)
    elif item == Items.Empty_Tank:
        buy(Items.Empty_Tank, amount)
    elif item == Items.Sunflower_Seed:
        buy(Items.Sunflower_Seed, amount)
    elif item == Items.Cactus_Seed:
        buy(Items.Cactus_Seed, amount)
    elif item == Items.Egg:
        buy(Items.Egg, amount)


def buy(item, amount, fixed=False):
    if num_items(item) > amount:
        return

    required_amount = amount - num_items(item)

    if fixed:
        required_amount = amount

    item_costs = get_cost(item)
    for required_item in item_costs:
        request_items(required_item, required_amount * item_costs[required_item])
    for required_item in item_costs:
        request_items(required_item, required_amount * item_costs[required_item])

    trade(item, required_amount)


def upgrade(unlock_item):
    quick_print("Upgrading", unlock_item, "to level", num_unlocked(unlock_item) + 1)
    requirements = get_cost(unlock_item)

    for required_item in requirements:
        request_items(required_item, requirements[required_item])
    for required_item in requirements:
        request_items(required_item, requirements[required_item])

    unlock(unlock_item)
