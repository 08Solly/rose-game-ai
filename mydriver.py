from rose.common import obstacles, actions  # NOQA

driver_name = "MyDriver"


def drive(world):
    return escape_obstacles(world)


def escape_obstacles(world):
    x = world.car.x
    y = world.car.y

    if is_obstacle(world.get((x, y - 1))):
        if x == 0 or x == 3:
            return actions.RIGHT
        if x == 2 or x == 5:
            return actions.LEFT
        if not is_obstacle(world.get((x - 1, y - 1))):
            return actions.LEFT
        if not is_obstacle(world.get((x + 1, y - 1))):
            return actions.RIGHT
    else:
        return brake(world.get((x, y - 1)))


# True -> is obstacle
# False -> not obstacle
def is_obstacle(obs):
    if obs in (obstacles.NONE, obstacles.PENGUIN, obstacles.CRACK, obstacles.WATER):
        return False
    return True


def brake(obs):
    if obs == obstacles.WATER:
        return actions.BRAKE
    elif obs == obstacles.CRACK:
        return actions.JUMP
    elif obs == obstacles.PENGUIN:
        return actions.PICKUP
    else:
        return actions.NONE
