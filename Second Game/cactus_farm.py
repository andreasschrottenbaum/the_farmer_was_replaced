# Cacti can be grown on soil from cactus seeds.

# They have an odd sense of community.

# When you harvest a cactus all cacti on the field are harvested.
# The number of cactus items dropped per cactus is equal to the world size as returned by get_world_size().

# A cactus only drops cactus items when harvested if it's in sorted order. 
# A cactus is considered to be in sorted order if there is a smaller or equal cactus to the South and to the West and a larger or equal cactus to the North and to the East.
# Essentially the cacti must be sorted in increasing x and y directions for them to drop anything.

# If a cactus is at the edge of the field, only the existing neighboring fields need to be correct for it to be sorted.

# The size of a cactus can be measured with measure(). 
# It is always one of these numbers: 0,1,2,3,4,5,6,7,8,9.

# You can swap a cactus with its neighbor in any direction using the swap() command.
# swap(direction) swaps the object under the drone with the object one tile in the direction of the drone.


from utils import *
from move import *

def bubble_sort(cactus_list):
    n = len(cactus_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if cactus_list[j][0] > cactus_list[j + 1][0]:
                cactus_list[j], cactus_list[j + 1] = cactus_list[j + 1], cactus_list[j]
    return cactus_list

def selection_sort(cactus_list):
    n = len(cactus_list)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if cactus_list[j][0] < cactus_list[min_index][0]:
                min_index = j
        cactus_list[i], cactus_list[min_index] = cactus_list[min_index], cactus_list[i]
    return cactus_list

def cactus_farm(amount):
    original_size = get_world_size()
    set_farm_size(original_size)
    request_items(Items.Cactus_Seed, amount * 2)
    clear()
    set_farm_size(3)    

    while (num_items(Items.Cactus) < amount) or (num_items(Items.Cactus_Seed) == 0):
        if (can_harvest()):
            harvest()
            
        if (get_ground_type() != Grounds.Soil):
            till()
        
        if (get_entity_type() != Entities.Cactus):
            plant(Entities.Cactus)

        move_to_next()
    
    if (num_items(Items.Cactus) == 0):
        quick_print("Ran out of cactus seeds.")
        
    set_farm_size(original_size)
    
        # # Kakteen pflanzen
        # for a in range(world_size):
        #     for b in range(world_size):
        #         if (get_ground_type() != Grounds.Soil):
        #             till()
        #         plant(Entities.Cactus)
        #         if b < world_size - 1:
        #             move(East)
        #     if a < world_size - 1:
        #         move(South)
        #         for c in range(world_size - 1):
        #             move(West)

        # # Kakteen in einer Liste speichern und sortieren
        # cactus_list = []
        # for a in range(world_size):
        #     for b in range(world_size):
        #         move_to(a, b)
        #         size = measure()
        #         cactus_list.append((size, a, b))

        # cactus_list = selection_sort(cactus_list)

        # # Kakteen auf dem Feld sortieren
        # for i in range(len(cactus_list)):
        #     for j in range(len(cactus_list) - i - 1):
        #         # Positionen der zu tauschenden Kakteen abrufen
        #         value1, x1, y1 = cactus_list[j]
        #         value2, x2, y2 = cactus_list[j + 1]

        #         # Zur Position des ersten Kaktus bewegen
        #         move_to(x1, y1)

        #         # Größe des aktuellen Kaktus messen
        #         size_current = measure()

        #         # Richtung zum zweiten Kaktus bestimmen und dorthin bewegen
        #         if x2 > x1:
        #             direction = East
        #         elif x2 < x1:
        #             direction = West
        #         elif y2 > y1:
        #             direction = South
        #         else:
        #             direction = North
        #         move(direction)

        #         # Größe des nächsten Kaktus messen
        #         size_next = measure()

        #         # Wenn der aktuelle Kaktus größer ist als der nächste, tauschen Sie sie
        #         if size_current > size_next:
        #             swap(direction)
        #             # Kakteen in der Liste tauschen
        #             cactus_list[j], cactus_list[j + 1] = cactus_list[j + 1], cactus_list[j]

        # # Kakteen ernten
        # for cactus in cactus_list:
        #     # Zur Position des Kaktus bewegen
        #     move_to(cactus[1], cactus[2])
        #     # Kaktus ernten
        #     harvest()
            