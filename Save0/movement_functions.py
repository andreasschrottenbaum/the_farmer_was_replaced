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
  current_x, current_y = get_pos_x(), get_pos_y()

  if current_x < (x / (world_size / 2)):
    while get_pos_x() != x:
      move(East)
  elif current_x > (x / (world_size / 2)):
    while get_pos_x() != x:
      move(West)

  if current_y < (y / (world_size / 2)):
    while get_pos_y() != y:
      move(South)

  elif current_y > (y / (world_size / 2)):
    while get_pos_y() != y:
      move(North)

def move_to_next():
  next_x = (get_pos_x() + 1) % world_size
  next_y = (get_pos_y() + (next_x == 0)) % world_size
  move_to(next_x, next_y)

def move_to_previous():
  if get_pos_x() == 0:
    move(North)
    if get_pos_y() != 0:
      target_y = get_pos_y() - 1
    else:
      target_y = world_size - 1
    move_to(world_size - 1, target_y)
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

def get_position():
    return (get_pos_x(), get_pos_y())

def can_move(direction):
    current_position = get_position()

    move(direction)

    if get_position() != current_position:
        move_back(direction)
        return True

    return False
    
def get_left_direction(current_direction):
    directions = [North, East, South, West]
    return directions[(directions.index(current_direction) - 1) % len(directions)]

def get_right_direction(current_direction):
    directions = [North, East, South, West]
    return directions[(directions.index(current_direction) + 1) % len(directions)]

def get_back_direction(current_direction):
    directions = [North, East, South, West]
    return directions[(directions.index(current_direction) + 2) % len(directions)]

def get_possible_directions():
    directions = [North, East, South, West]
    possible_directions = []
    for direction in directions:
        if can_move(direction):
            possible_directions.append(direction)
    return possible_directions

def move_back(direction):
    opposite_directions = {North: South, East: West, South: North, West: East}
    move(opposite_directions[direction])

def move_forward_left():
    current_direction = North  # annehmen, dass wir zuerst nach Norden gehen
    while True:
        left_direction = get_left_direction(current_direction)
        if can_move(left_direction):
            move(left_direction)
            current_direction = left_direction
        elif can_move(current_direction):
            move(current_direction)
        else:
            # Wenn wir weder links noch geradeaus gehen können, müssen wir rechts abbiegen
            current_direction = get_left_direction(get_left_direction(get_left_direction(current_direction)))
            move(current_direction)

def move_forward_right():
    current_direction = North  # annehmen, dass wir zuerst nach Norden gehen
    while True:
        right_direction = get_right_direction(current_direction)
        if can_move(right_direction):
            move(right_direction)
            current_direction = right_direction
        elif can_move(current_direction):
            move(current_direction)
        else:
            # Wenn wir weder rechts noch geradeaus gehen können, müssen wir links abbiegen
            current_direction = get_right_direction(get_right_direction(get_right_direction(current_direction)))
            move(current_direction)

def move_forward():
    current_direction = North  # annehmen, dass wir zuerst nach Norden gehen
    while True:
        if can_move(current_direction):
            move(current_direction)
        else:
            # Wenn wir nicht geradeaus gehen können, müssen wir rechts abbiegen
            current_direction = get_right_direction(get_right_direction(get_right_direction(current_direction)))
            move(current_direction)