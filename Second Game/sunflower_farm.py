from utils import *
farm_size = get_world_size()


def sunflower_farm(amount):
  while amount < num_items(Items.Power):
    clear()
    request_items(Items.Sunflower_Seed, 100)

    # Pflanzen Sie die Sonnenblumen
    for i in range(farm_size):
      for j in range(farm_size):
        if i != 0 or j != 0:  # Nicht beim ersten Durchlauf bewegen
          if j == 0:  # Am Anfang einer Zeile, bewegen Sie sich eine Zeile nach unten und ganz nach links
            move(South)
            for a in range(farm_size - 1):
              move(West)
          else:  # Ansonsten bewegen Sie sich einfach nach rechts
            move(East)

        if get_ground_type() != Grounds.Soil:
          till()

        plant(Entities.Sunflower)
        use_item(Items.Water_Tank)


    # Finden Sie alle Sonnenblumen und ihre Blütenblätter
    sunflowers = []
    for i in range(farm_size):
        for j in range(farm_size):
            for a in range(i):
                move(East)
            for b in range(j):
                move(South)
            petals = measure()
            sunflowers.append(((i, j), petals))
            for c in range(j):
                move(North)
            for d in range(i):
                move(West)

    # Sortieren Sie die Sonnenblumen absteigend nach der Anzahl ihrer Blütenblätter
    for i in range(len(sunflowers)):
        for j in range(len(sunflowers) - i - 1):
            if sunflowers[j][1] < sunflowers[j + 1][1]:
                sunflowers[j], sunflowers[j + 1] = sunflowers[j + 1], sunflowers[j]

    # Ernten Sie alle Sonnenblumen absteigend nach der Anzahl ihrer Blütenblätter
    for sunflower in sunflowers:
        for a in range(sunflower[0][0]):
            move(East)
        for b in range(sunflower[0][1]):
            move(South)
        harvest()
        for c in range(sunflower[0][1]):
            move(North)
        for d in range(sunflower[0][0]):
            move(West)
