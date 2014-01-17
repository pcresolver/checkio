"""
Takes in a square maze as a list of lists - rows of columns.
From the beginning goes to each available cell until it finds the exit.
It avoids walls and doesn't cover ground it has already covered using recursion.

Start at cell 0,0 .
Mark cells covered with '3' so that we don't go back
"""
grid = [[0, 0, 0, 0, 0, 1],[1, 1, 0, 0, 0, 1],[0, 0, 0, 1, 0, 0],[0, 1, 1, 0, 0, 1], [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 0, 2]]

def search(x, y):
    if grid[x][y] == 55: # we have found the exit
        print("Exit found here: {}{}" .format(x, y))
        return True
    elif grid[x][y] == 1: # can't go to this cell
        print("Can't go to : {}{}" .format(x, y))
        return False
    elif grid[x][y] == 3: # a cell that we have been to has its value changed to '3'
        print("Already been here: {}{}" .format(x, y))
        return False
     
    print('We are here: {}{}' .format(x, y))
 
    # Been here so modify content to avoid re-visits
    grid[x][y] = 3
 
    # Look for the next move. Start looking to the E.
    if ((x < len(grid)-1 and search(x+1, y))
        or (y > 0 and search(x, y-1))
        or (x > 0 and search(x-1, y))
        or (y < len(grid)-1 and search(x, y+1))):
        return True
 
    return False
 
search(0, 0)
