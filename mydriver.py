from rose.common import obstacles, actions  # NOQA

driver_name = "MyDriver"


def drive(world):
    x = world.car.x
    y = world.car.y

    try:
        obstacle = world.get((x, y - 1))
    except IndexError:
        return actions.BRAKE

    if obstacle == obstacles.NONE:
        return actions.NONE
    elif obstacle == obstacles.PENGUIN:
        return actions.PICKUP
    elif obstacle == obstacles.WATER:
        return actions.BRAKE
    elif obstacle == obstacles.CRACK:
        return actions.JUMP
    elif obstacle in (obstacles.TRASH, obstacles.BIKE, obstacles.BARRIER):
        right_obstacle = world.get((x + 1, y))
        left_obstacle = world.get((x - 1, y))
        if right_obstacle == obstacles.NONE and x+1 <= 2:
            return actions.RIGHT
        elif left_obstacle == obstacles.NONE:
            return actions.LEFT
        else:
            return actions.NONE

    return actions.BRAKE



