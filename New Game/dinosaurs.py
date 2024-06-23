from utilities import *
from trading import *
from movement import *


def find_dinosaurs():
    dinosaurs = []
    for x in range(get_world_size()):
        for y in range(get_world_size()):
            move_to(x, y)
            dinosaur_type = measure()
            dinosaurs.append((dinosaur_type, x, y))
    return dinosaurs


def find_groups(dinosaurs):
    groups = []
    dinosaur_types = set()
    for dinosaur in dinosaurs:
        dinosaur_types.add(dinosaur[0])
    for dinosaur_type in dinosaur_types:
        group = []
        for dinosaur in dinosaurs:
            if dinosaur[0] == dinosaur_type:
                group.append((dinosaur[1], dinosaur[2]))
        groups.append(group)
    return groups


def harvest_group(group):
    for position in group:
        x = position[0]
        y = position[1]
        move_to(x, y)
        if can_harvest():
            harvest()


def dino_farm(amount):
    farm_size = get_world_size() * get_world_size()

    while num_items(Items.Bones) < amount:
        request_items(Items.Egg, farm_size)

        for i in range(get_world_size() * get_world_size()):
            if get_entity_type() == None or get_entity_type() == Entities.Grass:
                use_item(Items.Egg)
            move_next()

        dinosaurs = find_dinosaurs()
        groups = find_groups(dinosaurs)
        for group in groups:
            if len(group) >= 4:
                harvest_group(group)
