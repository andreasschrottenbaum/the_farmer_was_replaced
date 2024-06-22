from move import *
from utils import *

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
    original_size = get_world_size()
    request_items(Items.Egg, amount - num_items(Items.Bones) - num_items(Items.Egg))

    # Füllen Sie das gesamte Feld mit Dinosauriern
    for x in range(get_world_size()):
        for y in range(get_world_size()):
            move_to(x, y)
            use_item(Items.Egg)

    while (num_items(Items.Bones) < amount):
        set_farm_size(original_size)
        request_items(Items.Egg, amount - num_items(Items.Bones))
        
        set_farm_size(5)
        clear()
        dinosaurs = find_dinosaurs()
        groups = find_groups(dinosaurs)
        for group in groups:
            if len(group) >= 4:
                harvest_group(group)
        
        use_item(Items.Egg)
        move_to_next()
    
    set_farm_size(original_size)