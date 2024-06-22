from harvest_functions import *
from movement_functions import *

while True:
    # Weltgröße abrufen
    world_size = get_world_size()
    clear()

    while True:
        trade(Items.Cactus_Seed, 100)

        # Kakteen pflanzen
        for a in range(world_size):
            for b in range(world_size):
                make_ground(Grounds.Soil)
                plant(Entities.Cactus)
                move(East)
            move(South)
            for a in range(world_size):
                move(West)

        # Zurück zum Anfang des Feldes bewegen
        move_to_start()
        
        # Kakteen in einer Liste speichern
        # cactus_list = []
        # for a in range(world_size):
        #     for b in range(world_size):
        #         cactus_list.append((measure(), a, b))
        #         move(East)
        #     move(South)
        #     for a in range(world_size):
        #         move(West)

        # # Zurück zum Anfang des Feldes bewegen
        # for a in range(world_size):
        #     move(North)

        # # Kakteen mit Bubble-Sort sortieren
        # for i in range(len(cactus_list)):
        #     for j in range(len(cactus_list) - i - 1):
        #         if cactus_list[j][0] > cactus_list[j + 1][0]:
        #             cactus_list[j], cactus_list[j + 1] = cactus_list[j + 1], cactus_list[j]
        
        harvest()