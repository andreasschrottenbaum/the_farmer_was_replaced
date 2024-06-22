from harvest_functions import *

farm_size = get_world_size()

while True:
  clear()

  # Pflanzen Sie die Sonnenblumen
  for i in range(farm_size):
      for j in range(farm_size):
          for a in range(i):
              move(East)
          for b in range(j):
              move(South)
          
          make_ground(Grounds.Soil)
          plant(Entities.Sunflower)
          for c in range(j):
              move(North)
          for d in range(i):
              move(West)

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
