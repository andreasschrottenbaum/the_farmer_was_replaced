from trading import *


def hydrate(optional=False):
    if not num_unlocked(Unlocks.Watering) or not num_unlocked(Unlocks.Plant):
        return False

    bucket_count = get_world_size() * get_world_size() * get_world_size()
    current_items = num_items(Items.Empty_Tank) + num_items(Items.Water_Tank)

    if optional and current_items < bucket_count:
        return False

    if current_items < bucket_count:
        buy(Items.Empty_Tank, bucket_count - current_items, True)

    if get_water() < 0.2 and num_items(Items.Water_Tank):
        use_item(Items.Water_Tank)

    return True


def stay_energized(optional=False):
    if not num_unlocked(Unlocks.Sunflowers):
        return

    world_area = get_world_size() * get_world_size()

    if optional:
        return

    if num_items(Items.Power) < world_area:
        request_items(Items.Power, world_area)


def get_all_coordinates():
    coords = set()

    for x in range(get_world_size()):
        for y in range(get_world_size()):
            coords.add((x, y))

    return coords
