def move_next():
    if not num_unlocked(Unlocks.Expand):
        return

    if num_unlocked(Unlocks.Expand) > 1 and get_pos_y() == get_world_size() - 1:
        move(East)

    move(North)


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
