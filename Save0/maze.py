def get_position():
    return (get_pos_x(), get_pos_y())

def can_move(direction):
    # Speichern Sie Ihre aktuelle Position
    current_position = get_position()

    # Versuchen Sie, in die angegebene Richtung zu gehen
    move(direction)

    # Überprüfen Sie, ob Sie sich bewegt haben
    if get_position() != current_position:
        # Wenn Sie sich bewegt haben, gehen Sie zurück und geben Sie True zurück
        move_back(direction)
        return True
    else:
        # Wenn Sie sich nicht bewegt haben, geben Sie False zurück
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

def dfs():
    current_position = get_position()
    if current_position in visited:
        return False

    visited.add(current_position)

    if (can_harvest() and get_entity_type() == Entities.Treasure):
        harvest()
        return True

    for direction in get_possible_directions():
        move(direction)
        if dfs():
            return True
        move_back(direction)

    return False

while True:
  visited = set()
  clear()
  plant(Entities.Bush)

  if (num_items(Items.Fertilizer) < 200):
    trade(Items.Fertilizer, 1000)

  while True:
    if can_harvest() and get_entity_type() == Entities.Bush:
      use_item(Items.Fertilizer)
    elif can_harvest() and get_entity_type() == Entities.Hedge:
      break
    elif can_harvest() and get_entity_type() == Entities.Treasure:
      harvest()
      break

  dfs()