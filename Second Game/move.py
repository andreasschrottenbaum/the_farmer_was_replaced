directions = [North, East, South, West]

def move_to(x, y):
  current_x, current_y = get_pos_x(), get_pos_y()
  world_size = get_world_size()

  dx = (x - current_x) % world_size
  dy = (y - current_y) % world_size

  if dx <= world_size // 2:
    for a in range(dx):
      move(East)
  else:
    for a in range(world_size - dx):
      move(West)

  if dy <= world_size // 2:
    for a in range(dy):
      move(North)
  else:
    for a in range(world_size - dy):
      move(South)

def move_to_next():
  world_size = get_world_size()

  next_x = (get_pos_x() + 1) % world_size
  next_y = (get_pos_y() + (next_x == 0)) % world_size
  move_to(next_x, next_y)
  

def get_position():
    return (get_pos_x(), get_pos_y())


def can_move(direction):
    current_position = get_position()

    move(direction)

    if get_position() != current_position:
        move_back(direction)
        return True

    return False


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
    
def try_move_left(direction_index):
    directions = [North, East, South, West]

    new_index = (direction_index - 1) % 4
    if move(directions[new_index]):
        return new_index
    elif move(directions[direction_index]):
        return direction_index
    elif move(directions[(direction_index + 1) % 4]):
        return (direction_index + 1) % 4
    elif move(directions[(direction_index + 2) % 4]):
        return (direction_index + 2) % 4
    return direction_index

