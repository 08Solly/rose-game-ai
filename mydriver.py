from rose.common import obstacles, actions  # NOQA

driver_name = "MyDriver"


def drive(world):
    return escape_obstacles(world)


def escape_obstacles(world):
    x = world.car.x
    y = world.car.y

    found_penguin = findPenguin(world,x,y)

    if found_penguin != actions.NONE:
        return found_penguin

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
    

def findPenguin(world: list[int, int],pos_x,pos_y: int):
    """
    Finds penguins in the world.\n
    Return the position of the penguin if found, otherwise return (-1,-1)
    """

    
    try:
        if world.get((pos_x, pos_y - 1)) == obstacles.PENGUIN:
            return actions.PICKUP
        
        if world.get((pos_x-1, pos_y-2)) == obstacles.PENGUIN:
            if not is_obstacle(world.get((pos_x-1, pos_y-1))):
                return actions.LEFT
        if world.get((pos_x+1, pos_y-2)) == obstacles.PENGUIN:
            if not is_obstacle(world.get((pos_x+1, pos_y-1))):
                return actions.RIGHT
        
        if world.get((pos_x-2, pos_y-3)) == obstacles.PENGUIN:
            if not is_obstacle(world.get((pos_x-2, pos_y-2))):
                    return actions.LEFT
        
        if world.get((pos_x+2, pos_y-3)) == obstacles.PENGUIN:
            if not is_obstacle(world.get((pos_x+2, pos_y-2))):
                    return actions.RIGHT

    except IndexError:    
        return actions.NONE

    return actions.NONE

