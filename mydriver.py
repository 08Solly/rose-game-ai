from rose.common import obstacles, actions  # NOQA

driver_name = "MyDriver"
lane = -1

def map_world(world) -> list[list[str]]:
    car_x: int = world.car.x
    car_y: int = world.car.y

    lanes: tuple[int] = (0, 1, 2)

    # forward offset of the look by car
    forward_look: int = 3

    # get for every lane the obstacle in it for 3x3 car in bottom
    lane_matrix: list[list[str]] = [
        [(world.get((x, y)), y) for x in lanes] for y in range((car_y - forward_look -1), car_y - 1)]

    # testing
    # poses = [([x for x in lanes], y) for y in range((car_y - forward_look -1 ), car_y - 1)]
    # [print(row) for row in poses]
    # [print(row) for row in lane_matrix]
    # print(f"x:{car_x}, y:{car_y}")

    return lane_matrix



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



