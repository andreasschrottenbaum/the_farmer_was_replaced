from utilities import *
from trading import *
from movement import *


def sunflower_farm(amount):
    farm_size = get_world_size() * get_world_size()

    while num_items(Items.Power) < amount:
        request_items(Items.Sunflower_Seed, farm_size + 1)
        clear()

        for i in range(farm_size):
            if get_ground_type() != Grounds.Soil:
                till()

            while get_entity_type() != Entities.Sunflower:
                harvest()
                plant(Entities.Sunflower)

            hydrate()
            move_next()

        # Finden Sie alle Sonnenblumen und ihre Blütenblätter
        sunflowers = []
        for i in range(farm_size):
            petals = measure()
            sunflowers.append(((get_pos_x(), get_pos_y()), petals))
            move_next()

        # Sortieren Sie die Sonnenblumen absteigend nach der Anzahl ihrer Blütenblätter
        for i in range(len(sunflowers)):
            for j in range(len(sunflowers) - i - 1):
                if sunflowers[j][1] < sunflowers[j + 1][1]:
                    sunflowers[j], sunflowers[j + 1] = sunflowers[j + 1], sunflowers[j]

        # Ernten Sie alle Sonnenblumen absteigend nach der Anzahl ihrer Blütenblätter
        for sunflower in sunflowers:
            move_to(sunflower[0][0], sunflower[0][1])
            harvest()
