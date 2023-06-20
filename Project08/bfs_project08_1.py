
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

    # return the grid
    return grid


def search_from(grid, row, col):
    ''' recursive function to search the grid for the end (E) '''

    global steps
    
    steps += 1
    
    # make sure row and col are valid positions on the grid
    if (row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1):
        return False
    
    # check that the grid cell at row and col is not obstacle (X), tried (T), or deadend (D)
    if (grid[row][col] == 'X' or grid[row][col] == 'T' or grid[row][col] == 'D'):
        # return False if obstacle, tried, or deadend
        return False
        
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
    up = search_from(grid, row-1, col)
    print(up)
    down = search_from(grid, row+1, col)
    print(down)
    left = search_from(grid, row, col-1)
    print(left)
    right = search_from(grid, row, col+1)
    print(right)
            
    # if any of the 4 directions returns True (found), mark the cel at row, col as part of the path and return True
    if up != 'S':
        grid[row][col] = 'T'
        #return True
    elif down != 'S':
        grid[row][col] = 'T'
    elif left != 'S':
        grid[row][col] = 'T'
    elif right != 'S':
        grid[row][col] = 'T'

    # else, if the cell at row, col is not the start cell (S), mark it as a deadend
    elif grid[row][col] != 'S':
        grid[row][col] = 'D'
    

def main():
    ''' reads a maze file and sets the search parameters '''

    # read maze file and create playground grid
    playground = read_grid("maze2.txt")
    print(playground)

    # find start position
    row, col = find_start(playground)
    print(row, col)

    # call the search function, it takes the grid, row, column, and steps
    search_from(playground, row, col)

    # create a list of tuples representing the path
    path = []
    for row in range(len(playground)):
        for col in range(len(playground[0])):
            if playground[row][col] == 'P':
                path.append((row, col))

    # print path length
    print(len(path))

    # draw the final grid
    draw_grid(playground, turt, x_offset, y_offset, tile_size)
    
    # pause the grid drawing for 4 seconds
    time.sleep(4)

    # print the number of steps taken to find the path
    print(steps)
    

if __name__ == "__main__":
    main()