"""
This driver does not do any action.
"""

from rose.common import obstacles, actions  # NOQA

driver_name = "MyDriver"

def obstacle_T_F(obs: str) -> bool:
    pass
    

def findPenguin(mapped_world: list[int,int],pos_y: int) -> tuple[int,int]:
    """
    Finds penguins in the world.\n
    Return the position of the penguin if found, otherwise return (-1,-1)
    """

    for x_pos in range(len(mapped_world[0])):
        if mapped_world[pos_y-1][x_pos] == obstacles.PENGUIN:
            return (x_pos, pos_y-1)
    
    for x_pos in range(len(mapped_world[0])):
        if not obstacle_T_F(mapped_world[pos_y-1][[x_pos]]):
            if mapped_world[pos_y][x_pos] == obstacles.PENGUIN:
                return (x_pos, pos_y)
        
    return (-1,-1)

def drive(world):
    return actions.NONE
