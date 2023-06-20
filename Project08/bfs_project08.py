
'''
project7.py
Adrian Gellert
CS151 C with Al Madi
2nd Semester
Date created: April 26, 2021
Date last modified: April 26, 2021

This file uses the breadth first search algorithm to find a path through a maze.
'''



# Global scope variables

# number of nodes in the grid
#n = 

# adjacency list representing unweighted graph
#g =

# s = start node, e = end node, and 0 <= e, s < n
def bfs(s, e):

    # Do a BFS starting at node s
    prev = solve(s)

    # Return reconstructed path from s -> e 
    return reconstructPath(s, e, prev)


def solve(s):
    #q = # queu data structure with enqueue and dequeue
    q.enqueue(s)

    visited = [False, ..., False] # size n, boolean array with all false values
    visted[s] = True # marking the starting node as visited

    prev = [None, ..., None] # size n, array to help reconstruct path from start node to end node
    while q != Empty():
        '''loop while queue is not empty and pull out top node from the queue''' 
        node = q.dequeue # initializing dequeue operation
        neighbours = g.get(node) # get all neighbors of pulled out node

        for next in neighbors:
            if next != visited:
                q.enqueue(next)
                visited[next] = True
                prev[next] = node

        return prev


def reconstructPath(s, e, prev):

    # Reconstruct path going backwards from e
    path = []
    for at in range(prev, e, -1):
        path.add(at)

    path.reverse()

    if path[0] == s:
        return path
    else:
        return []



''' Steps to writing a BFS code '''
# 1) Convert grid to an adjacency numpy array 
# (numpy array filled with 1 where index has a neighbor with anoth index)
    # a) label cells in grid with numbers [0, n], where n = #rows * #cols
    # b) create adjacency, n x n, numpy array filled with 1's and 0's
    # c) run program

# 2) using vectors for directions of movement
    # a) define direction vectors for north, south, east, west
        # i) direction_row = [-1 = -north, +1 = -south, 0 = east, 0 = west]
            #direction_col = [0 = north, 0 = south, +1 = east, -1 = west]
    # b) loop over every direction vector and add to the current position
        # i) for i in range(len(direction_row[0])):
                # new_row = r + i
                # if new_row < 0 or new_row > len(grid) - 1: ## skipping invalid cells
                    # continue
           # for j in range(len(direction_col[0])):
                # new_col = c + j
                # if new_col < 0 or new_row > len(grid[0]) - 1: ## skipping invalid cells
                    # continue
                    
            #if these conditions are passed, we know that (new_row, new_col) is a neighboring cell of (row, col)



'''
project7.py
Adrian Gellert
CS151 C with Al Madi
2nd Semester
Date created: April 21, 2021
Date last modified: April 26, 2021

This file uses recursion to find a path through a maze.
'''


import turtle
import time
import queue 

# create a turtle and a window for drawing
turt = turtle.Turtle()
window = turtle.getscreen()

# set offsets and tile size for drawing the grid
x_offset = -150
y_offset = 200
tile_size = 50

# create an int variable for counting steps
steps = 0

# create variable for vector of possible movements 
direction_row = [-1, +1, 0, 0]
direction_col = [0, 0, +1, -1]

def draw_grid(grid, turt, x_pos, y_pos, tile_size):
    ''' draws a grid at x_pos, y_pos with a specific tile_size '''

    # turn off tracer for fast drawing
    #window.tracer(False)
    
    # move turtle to initial drawing position
    turt.up()
    turt.goto(x_pos, y_pos)
    turt.down()

    # go over every cell in the grid
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            
            # move turtle to the position of the cell in the grid
            turt.up()
            turt.goto(x_pos + col * tile_size, y_pos - row * tile_size)
            turt.down()

            # if the cell is an obstacle (X) draw a black dot
            if grid[row][col] == 'X':
                turt.dot(tile_size - 5, 'Black')
            
            # if the cell is the start drawing position (S) draw a yellow dot
            elif grid[row][col] == 'S':
                turt.dot(tile_size - 5, 'Yellow')
            
            # if the cell is the End position (E) draw a red dot
            elif grid[row][col] == 'E':
                turt.dot(tile_size - 5, 'Red')

            # if the cell is part of a path (P) draw a royalblue dot
            elif grid[row][col] == 'P':
                turt.dot(tile_size - 5, 'RoyalBlue')

            # if the cell has been tried before (T) draw a light blue dot
            elif grid[row][col] == 'T':
                turt.dot(tile_size - 5, 'LightBlue')

            # if the cell is part of a deadend (D) draw a gray dot
            elif grid[row][col] == 'D':
                turt.dot(tile_size - 5, 'Gray')
            
            # else draw a white dot
            else:
                turt.dot(tile_size-5, "white")
    
    #turn tracer back on
    window.update()
    #window.tracer(True)


def find_start(grid):
    ''' finds the start position (S) in the grid
    returns a tuple of start row and col
    '''

    # go over every cell in the grid
    for row in range(len(grid)):
        for col in range(len(grid[row])):

            # cell at row, col is 'S' return row and col as a tuple
            if grid[row][col] == 'S':
                return (row, col)


def read_grid(file_name):
    ''' reads a maze file and initializes a gird with its contents '''

    # create an empty grid (an empty list called grid)
    grid = []

    # open the text file
    file = open(file_name)

    # read a line from the file
    line = file.readline()

    # replace \n with nothing
    line = line.replace('\n', '')

    while line:
        # split the line into tokens
        tokens = line.split(",")

        # add the tokens to the grid as a single row (use append)
        grid.append(tokens)

        # read a new line from the file
        line = file.readline()
        
        # replace \n with nothing in the line
        line = line.replace('\n', '')

    #close file
    file.close()

    array = numpy.array(grid)
    flipped_array = numpy.flipud(array)

    # return the grid
    return flipped_array


def search_from(grid, row, col):
    ''' recursive function to search the grid for the end (E) '''

    global steps
    movement = queue.Queue()
    movement.put("")
    
    left = 
    
    steps += 1
    
    # looping over direction vector for row and adding values to 
    # current row 
    for i in range(4):
        new_row = row + direction_row[i]
        new_col = col + direction_col[i]
        print(new_row, new_col)
        # skipping over values that will result in "mouse" going to 
        # invalid cell
        if new_row > len(grid) - 1 or new_row < 0: 
            continue
        elif new_col > len(grid[0]) - 1 or new_col < 0: 
            continue
        # skipping over grid cell at row and col that are obstacle (X),
        # tried (T), deadend (D), or start (S)
        elif (grid[new_row][new_col] == 'X' or 
              grid[new_row][new_col] == 'T' or 
              grid[new_row][new_col] == 'D' or
              grid[new_row][new_col] == 'S'):
              continue  
        else:
            grid[new_row, new_col] = 'T'

        # If end is found at row, col return True
        if grid[new_row][new_col] == 'E':
            return True

    # draw the grid
    draw_grid(grid, turt, x_offset, y_offset, tile_size)

    # pause the program for a short duration, try 0.5 and 0.01 seconds
    time.sleep(0.01)

    # recursively search differnt directions adjacent to current row, col (up, down, left, right)
    found = (search_from(grid, row-1, col)
            or search_from(grid, row+1, col)
            or search_from(grid, row, col-1)
            or search_from(grid, row, col+1)
            )

    # if any of the 4 directions returns True (found), mark the cel at row, col as part of the path and return True
    if found:
        grid[row][col] = 'P'
        return True

    # else, if the cell at row, col is not the start cell (S), mark it as a deadend
    elif grid[row][col] != 'S':
        grid[row][col] = 'D'
    
def main():
    ''' reads a maze file and sets the search parameters '''

    # read maze file and create playground grid
    playground = read_grid("maze2.txt")
    #print(playground)

    # find start position
    row, col = find_start(playground)
    #print(row, col)

    # call the search function, it takes the grid, row, column, and steps
    search_from(playground, row, col)

    # create a list of tuples representing the path
    path = []
    for row in range(len(playground)):
        for col in range(len(playground[0])):
            if playground[row][col] == 'P':
                path.append((row, col))

    # print path length
    #print(len(path))

    # draw the final grid
    draw_grid(playground, turt, x_offset, y_offset, tile_size)
    
    # pause the grid drawing for 4 seconds
    time.sleep(4)

    # print the number of steps taken to find the path
    #print(steps)
    


if __name__ == "__main__":
    main()






def search_from(grid, row, col):
    ''' recursive function to search the grid for the end (E) '''

    global steps
    
    steps += 1
    
    '''
    # make sure row and col are valid positions on the grid
    if (row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1):
        return False
    '''

    right = col + 1
    left = col - 1
    up = row + 1
    down = row - 1


    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if ((row - 1) < 0 and (row - 1) > len(grid) - 1 and col < 0 and col > len(grid[0]) - 1) and grid[row - 1][col] == 'S' and grid[row][col] == 'X' or grid[row][col] == 'T' or grid[row][col] == 'D':
                continue
            else:
                grid[row - 1][col] = 'T'
            if ((row + 1) < 0 and (row + 1) > len(grid) - 1 and col < 0 and col > len(grid[0]) - 1) and grid[row + 1][col] == 'S' and grid[row][col] == 'X' or grid[row][col] == 'T' or grid[row][col] == 'D':
                continue
            else:


    if (row > 0 and row < len(grid) - 1 and (col - 1) > 0 and (col - 1) < len(grid[0]) - 1) and grid[row][col - 1] != 'S':
        grid[row][col - 1] = 'T'
    
    if (row > 0 and row < len(grid) - 1 and (col + 1) > 0 and (col + 1) < len(grid[0]) - 1) and grid[row][col + 1] != 'S':
        grid[row][col + 1] = 'T'
    
    '''
    # check that the grid cell at row and col is not obstacle (X), tried (T), or deadend (D)
    if (grid[row][col] == 'X' or grid[row][col] == 'T' or grid[row][col] == 'D'):
        # return False if obstacle, tried, or deadend
        return False
    '''
        
    # If end is found at row, col return True
    if grid[row][col] == 'E':
        return True
    
    '''
    # If the cell at row, col is not the start cell, mark the cell as tried (T)
    if grid[row][col] != 'S':
        grid[row][col] = 'T'
    '''

    # draw the grid
    draw_grid(grid, turt, x_offset, y_offset, tile_size)

    # pause the program for a short duration, try 0.5 and 0.01 seconds
    time.sleep(0.01)

    # recursively search differnt directions adjacent to current row, col (up, down, left, right)
    found = (search_from(grid, row-1, col)
            or search_from(grid, row+1, col)
            or search_from(grid, row, col-1)
            or search_from(grid, row, col+1)
            )

    # if any of the 4 directions returns True (found), mark the cel at row, col as part of the path and return True
    if found:
        grid[row][col] = 'P'
        return True

    # else, if the cell at row, col is not the start cell (S), mark it as a deadend
    elif grid[row][col] != 'S':
        grid[row][col] = 'D'
