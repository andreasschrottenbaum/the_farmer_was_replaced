world_size = get_world_size()



def move_to_start():
  while get_pos_x() != 0:
    move(West)
  while get_pos_y() != 0:
    move(South)

def move_to_end():
  while get_pos_x() != world_size - 1:
    move(East)
  while get_pos_y() != world_size - 1:
    move(North)

def move_to(x, y):
  while get_pos_x() != x:
    if get_pos_x() < x:
      move(East)
    else:
      move(West)
  while get_pos_y() != y:
    if get_pos_y() < y:
      move(South)
    else:
      move(North)

def move_to_next():
  if get_pos_x() == world_size - 1:
    move(South)
    move_to(0, get_pos_y())
  else:
    move(East)

def move_to_previous():
  if get_pos_x() == 0:
    move(North)
    move_to(world_size - 1, get_pos_y())
  else:
    move(West)

def move_to_highest():
  highest = 0
  highest_pos = 0
  for a in range(world_size):
    for a in range(world_size):
      if measure() > highest:
        highest = measure()
        highest_pos = get_pos_x(), get_pos_y()
      move(East)
    move(South)
    move_to(0, get_pos_y())
  move_to(highest_pos[0], highest_pos[1])

def move_to_lowest():
  lowest = 100
  lowest_pos = 0
  for a in range(world_size):
    for a in range(world_size):
      if measure() < lowest:
        lowest = measure()
        lowest_pos = get_pos_x(), get_pos_y()
      move(East)
    move(South)
    move_to(0, get_pos_y())
  move_to(lowest_pos[0], lowest_pos[1])

def move_to_nearest():
  nearest = 100
  nearest_pos = 0
  for a in range(world_size):
    for a in range(world_size):
      if abs(measure() - 50) < nearest:
        nearest = abs(measure() - 50)
        nearest_pos = get_pos_x(), get_pos_y()
      move(East)
    move(South)
    move_to(0, get_pos_y())
  move_to(nearest_pos[0], nearest_pos[1])

def move_to_farthest():
  farthest = 0
  farthest_pos = 0
  for a in range(world_size):
    for a in range(world_size):
      if abs(measure() - 50) > farthest:
        farthest = abs(measure() - 50)
        farthest_pos = get_pos_x(), get_pos_y()
      move(East)
    move(South)
    move_to(0, get_pos_y())
  move_to(farthest_pos[0], farthest_pos[1])

def move_to_random():
  move_to(random.randint(0, world_size - 1), random.randint(0, world_size - 1))

def move_to_center():
  move_to(world_size // 2, world_size // 2)

def move_to_edge():
  if get_pos_x() < world_size // 2:
    move_to(0, get_pos_y())
  else:
    move_to(world_size - 1, get_pos_y())

def move_to_corner():
  if get_pos_x() < world_size // 2:
    if get_pos_y() < world_size // 2:
      move_to(0, 0)
    else:
      move_to(0, world_size - 1)
  else:
    if get_pos_y() < world_size // 2:
      move_to(world_size - 1, 0)
    else:
      move_to(world_size - 1, world_size - 1)

def move_to_diagonal():
  if get_pos_x() < world_size // 2:
    if get_pos_y() < world_size // 2:
      move_to(0, world_size - 1)
    else:
      move_to(world_size - 1, 0)
  else:
    if get_pos_y() < world_size // 2:
      move_to(world_size - 1, 0)
    else:
      move_to(0, world_size - 1)

def move_to_opposite():
  move_to(world_size - 1 - get_pos_x(), world_size - 1 - get_pos_y())
