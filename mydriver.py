from rose.common import obstacles, actions  # NOQA

driver_name = "MyDriver"


def drive(world):
    map = map_world(world)

    return escape(map,world)


# def findPenguin(mapped_world: list[int, int], pos_y: int) -> tuple[int, int]:
#     """
#     Finds penguins in the world.\n
#     Return the position of the penguin if found, otherwise return (-1,-1)
#     """
#
#     for x_pos in range(len(mapped_world[0])):
#         if mapped_world[pos_y - 1][x_pos] == obstacles.PENGUIN:
#             return (x_pos, pos_y - 1)
#
#     for x_pos in range(len(mapped_world[0])):
#         if not obstacle_T_F(mapped_world[pos_y - 1][[x_pos]]):
#             if mapped_world[pos_y][x_pos] == obstacles.PENGUIN:
#                 return (x_pos, pos_y)
#
#     return (-1, -1)


def map_world(world) -> list[list[str]]:
    car_x: int = world.car.x
    car_y: int = world.car.y

    lanes: tuple[int] = (0, 1, 2)

    # forward offset of the look by car
    forward_look: int = 3

    # get for every lane the obstacle in it for 3x3 car in bottom
    lane_matrix: list[list[str]] = [
        [(world.get((x, y)), y) for x in lanes] for y in range((car_y - forward_look -1), car_y - 1)]

    poses = [([x for x in lanes], y) for y in range((car_y - forward_look -1 ), car_y - 1)]
    [print(row) for row in poses]
    [print(row) for row in lane_matrix]
    print(f"x:{car_x}, y:{car_y}")

    return lane_matrix


def left_lane(world, x, y) -> str:
    if (obstacle_T_F(map[2][x]) and obstacle_T_F(map[2][x + 1])) and not (
            obstacle_T_F(map[1][x]) and not obstacle_T_F(map[1][x + 1])):
        return actions.RIGHT
    elif obstacle_T_F(map[1][x]):
        return actions.RIGHT
    return actions.NONE

def right_lane(world, x, y) -> str:
    if (obstacle_T_F(map[2][x]) and obstacle_T_F(map[2][x - 1])) and not (
            obstacle_T_F(map[1][x]) and not obstacle_T_F(map[1][x - 1])):
        return actions.LEFT
    elif obstacle_T_F(map[1][x]):
        return actions.LEFT
    return actions.NONE

def middle_lane(world, x, y) -> str:
    if (obstacle_T_F(map[2][x]) == True and obstacle_T_F(map[2][x - 1]) == True) and (
            obstacle_T_F(map[1][x]) == False and obstacle_T_F(map[1][x + 1]) == False):
        return actions.RIGHT
    elif (obstacle_T_F(map[2][x]) == True and obstacle_T_F(map[2][x + 1]) == True) and (
            obstacle_T_F(map[1][x]) == False and obstacle_T_F(map[1][x - 1]) == False):
        return actions.LEFT
    elif obstacle_T_F(map[1][x]):
        if obstacle_T_F(map[1][x + 1]):
            return actions.RIGHT
        else:
            return actions.LEFT
    return actions.NONE


def escape(map,world):
    x = world.car.x
    y = world.car.y

    # penguin_pos = findPenguin(map,y)
    # if penguin_pos != (-1,-1):
    #     if penguin_pos[0] > x:
    #         return actions.RIGHT
    #     if penguin_pos[0] < x:
    #         return actions.LEFT
    if x==0:
        return left_lane(world, x, y)


    elif x==2:
        return right_lane(world, x, y)


    elif x==1:
        return middle_lane(world, x, y)



def obstacle_T_F(obs):
    if obs != obstacles.NONE or obs != obstacles.PENGUIN:
        return True

    return False

