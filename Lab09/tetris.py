
'''
tetriminos.py
Adrian Gellert
CS151 C with Al Madi
2nd Semester 
Date created: April 29, 2021
Date last modified: 19 May, 2021

This file contains an implementation of the game Tetris. 
'''


import turtle
import time
import random


# S-block tetrimino class
class S_tetrimino:

    def __init__(self):
        ''' initializes coordinates of tetrimino '''

        self.blocks = [[0, 2], [0, 1], [1, 1], [1, 0]] # initial coordinates of tetrimino


    def check(self):
        ''' method to check which tetrimino class is being used '''

        return "S"


    def move_right(self):
        ''' move current coordinates of tetrimino right by one unit '''

        # loop through each list in self.blocks grid 
        # increase second value of each list by 1   
        for row in range(len(self.blocks)):
            self.blocks[row][1] += 1
        
        # checking if correct
        # print(self.blocks)


    def move_left(self):
        ''' move current coordinates of tetrimino left by one unit '''

        # loop through each list in self.blocks grid 
        # decrease second value of each list by 1   
        for row in range(len(self.blocks)):
            self.blocks[row][1] -= 1
        
        # checking if correct
        # print(self.blocks)


    def move_down(self):
        ''' move current coordinates of tetrimino down by one unit '''

        # loop through each list in self.blocks grid 
        # increase first value of each list by 1   
        for row in range(len(self.blocks)):
            self.blocks[row][0] += 1

        # checking if correct
        # print(self.blocks)


    def clockwise_rotation(self):
        pass


    def counterclockwise_rotation(self):
        pass


# Z-block tetrimino class
class Z_tetrimino:

    def __init__(self):
        ''' initializes coordinates of tetrimino '''

        self.blocks = [[0, 0], [0, 1], [1, 1], [1, 2]] # initial coordinates of tetrimino


    def check(self):
        ''' initializes coordinates of tetrimino '''

        return "Z"


    def move_right(self):
        ''' move current coordinates of tetrimino right by one unit '''

        # loop through each list in self.blocks grid 
        # increase second value of each list by 1   
        for row in range(len(self.blocks)):
            self.blocks[row][1] += 1


    def move_left(self):
        ''' move current coordinates of tetrimino left by one unit '''

        # loop through each list in self.blocks grid 
        # decrease second value of each list by 1   
        for row in range(len(self.blocks)):
            self.blocks[row][1] -= 1


    def move_down(self):
        ''' move current coordinates of tetrimino down by one unit '''

        # loop through each list in self.blocks grid 
        # increase first value of each list by 1  
        for row in range(len(self.blocks)):
            self.blocks[row][0] += 1


    def clockwise_rotation(self):
        pass


    def counterclockwise_rotation(self):
        pass


# I-block tetrimino class
class I_tetrimino:

    def __init__(self):
        ''' initializes coordinates of tetrimino '''

        self.blocks = [[0, 0], [0, 1], [0, 2], [0, 3]] # initial coordinates of tetrimino


    def check(self):
        ''' initializes coordinates of tetrimino '''

        return "I"


    def move_right(self):
        ''' move current coordinates of tetrimino right by one unit '''

        # loop through each list in self.blocks grid 
        # increase second value of each list by 1   
        for row in range(len(self.blocks)):
            self.blocks[row][1] += 1


    def move_left(self):
        ''' move current coordinates of tetrimino left by one unit '''

        # loop through each list in self.blocks grid 
        # decrease second value of each list by 1   
        for row in range(len(self.blocks)):
            self.blocks[row][1] -= 1


    def move_down(self):
        ''' move current coordinates of tetrimino down by one unit '''

        # loop through each list in self.blocks grid 
        # increase first value of each list by 1  
        for row in range(len(self.blocks)):
            self.blocks[row][0] += 1


    def clockwise_rotation(self):
        pass


    def counterclockwise_rotation(self):
        pass


# J-block tetrimino class
class J_tetrimino:

    def __init__(self):
        ''' initializes coordinates of tetrimino '''
        self.blocks = [[0, 0], [1, 0], [1, 1], [1, 2]] # initial coordinates of tetrimino


    def check(self):
        ''' initializes coordinates of tetrimino '''

        return "J"


    def move_right(self):
        ''' move current coordinates of tetrimino right by one unit '''

        # loop through each list in self.blocks grid 
        # increase second value of each list by 1   
        for row in range(len(self.blocks)):
            self.blocks[row][1] += 1


    def move_left(self):
        ''' move current coordinates of tetrimino left by one unit '''

        # loop through each list in self.blocks grid 
        # decrease second value of each list by 1   
        for row in range(len(self.blocks)):
            self.blocks[row][1] -= 1


    def move_down(self):
        ''' move current coordinates of tetrimino down by one unit '''

        # loop through each list in self.blocks grid 
        # increase first value of each list by 1  
        for row in range(len(self.blocks)):
            self.blocks[row][0] += 1


    def clockwise_rotation(self):
        pass


    def counterclockwise_rotation(self):
        pass


# L-block tetrimino class
class L_tetrimino:

    def __init__(self):
        ''' initializes coordinates of tetrimino '''
        self.blocks = [[0, 0], [0, 1], [0, 2], [1, 0]] # initial coordinates of tetrimino


    def check(self):
        ''' initializes coordinates of tetrimino '''

        return "L"


    def move_right(self):
        ''' move current coordinates of tetrimino right by one unit '''

        # loop through each list in self.blocks grid 
        # increase second value of each list by 1   
        for row in range(len(self.blocks)):
            self.blocks[row][1] += 1


    def move_left(self):
        ''' move current coordinates of tetrimino left by one unit '''

        # loop through each list in self.blocks grid 
        # decrease second value of each list by 1   
        for row in range(len(self.blocks)):
            self.blocks[row][1] -= 1


    def move_down(self):
        ''' move current coordinates of tetrimino down by one unit '''

        # loop through each list in self.blocks grid 
        # increase first value of each list by 1  
        for row in range(len(self.blocks)):
            self.blocks[row][0] += 1


    def clockwise_rotation(self):
        pass


    def counterclockwise_rotation(self):
        pass


# O-block tetrimino class
class O_tetrimino:

    def __init__(self):
        ''' initializes coordinates of tetrimino '''
        self.blocks = [[0, 0], [0, 1], [1, 0], [1, 1]] # initial coordinates of tetrimino


    def check(self):
        ''' initializes coordinates of tetrimino '''

        return "O"


    def move_right(self):
        ''' move current coordinates of tetrimino right by one unit '''

        # loop through each list in self.blocks grid 
        # increase second value of each list by 1   
        for row in range(len(self.blocks)):
            self.blocks[row][1] += 1


    def move_left(self):
        ''' move current coordinates of tetrimino left by one unit '''

        # loop through each list in self.blocks grid 
        # decrease second value of each list by 1   
        for row in range(len(self.blocks)):
            self.blocks[row][1] -= 1


    def move_down(self):
        ''' move current coordinates of tetrimino down by one unit '''

        # loop through each list in self.blocks grid 
        # increase first value of each list by 1  
        for row in range(len(self.blocks)):
            self.blocks[row][0] += 1


    def clockwise_rotation(self):
        pass


    def counterclockwise_rotation(self):
        pass


# T-block tetrimino class
class T_tetrimino:

    def __init__(self):
        ''' initializes coordinates of tetrimino '''
        self.blocks = [[0, 0], [0, 1], [0, 2], [1, 1]] # initial coordinates of tetrimino


    def check(self):
        ''' initializes coordinates of tetrimino '''

        return "T"


    def move_right(self):
        ''' move current coordinates of tetrimino right by one unit '''

        # loop through each list in self.blocks grid 
        # increase second value of each list by 1   
        for row in range(len(self.blocks)):
            self.blocks[row][1] += 1
        
        # checking if correct
        # print(self.blocks)


    def move_left(self):
        ''' move current coordinates of tetrimino left by one unit '''

        # loop through each list in self.blocks grid 
        # decrease second value of each list by 1   
        for row in range(len(self.blocks)):
            self.blocks[row][1] -= 1
        
        # checking if correct
        # print(self.blocks)


    def move_down(self):
        ''' move current coordinates of tetrimino down by one unit '''

        # loop through each list in self.blocks grid 
        # increase first value of each list by 1  
        for row in range(len(self.blocks)):
            self.blocks[row][0] += 1

        # checking if correct
        # print(self.blocks)


    def clockwise_rotation(self):
        pass


    def counterclockwise_rotation(self):
        pass


# Tetris board class
class Board:

    def __init__(self):
        ''' initializes grid '''
        
        # turtle for drawing grid attributes
        self.turt = turtle.Turtle()
        self.turt.speed(0) # Speed of animation, 0 is max
        self.turt.color("black")
        self.turt.penup()
        self.turt.hideturtle()

        # turtle for drawing score attributes
        self.turt.score_keeper = turtle.Turtle()
        self.turt.score_keeper.speed(0) # Speed of animation, 0 is max
        self.turt.score_keeper.color("black")
        self.turt.score_keeper.penup()
        self.turt.score_keeper.hideturtle()
        
        # create a grid filled with 0s
        self.grid = []
        for i in range(25):
            self.grid.append([0] * 10)
        # print(len(self.grid[0]))
        
        # choose a random tetrimino to implement on the Tetris board
        self.list_tetriminos = [S_tetrimino, Z_tetrimino, I_tetrimino, J_tetrimino, L_tetrimino, O_tetrimino, T_tetrimino]
        self.tetrimino = random.choice(self.list_tetriminos)() # parentheses afterwards to make choice an instance


    def draw_square(self, tile_size, fillcolor, fill = False):
        ''' function to draw square '''

        self.turt.fillcolor(fillcolor)

        if fill == True:
            self.turt.begin_fill()
        for i in range(4):
            self.turt.forward(tile_size)
            self.turt.left(90)
        self.turt.end_fill()


    def draw_initial_score(self):
        ''' draws player's initial score above the tetris playing board '''

        # set counter for score
        counter = 0
        
        # draw initial score
        self.turt.score_keeper.penup()
        self.turt.score_keeper.goto(-100, (turtle.window_height() / 2) - 100)
        self.turt.score_keeper.pendown()
        self.turt.score_keeper.write("Player Score: " + str(counter), font=("Verdana", 20, "normal"))

        # print(self.grid)


    def move_right(self):
        ''' calls moving right method from tetrimino class '''
        self.tetrimino.move_right()

    
    def move_left(self):
        ''' calls moving left method from tetrimino class '''
        self.tetrimino.move_left()


    def move_down(self):
        ''' calls moving down method from tetrimino class '''
        self.tetrimino.move_down()
        
    
    # clockwise rotation
    def clockwise_rotation(self):
        pass


    def draw_board(self, window, x_offset, y_offset, tile_size):
        ''' draws tetris board with specific tile_size by implementing draw_square function '''

        # making things on screen draw quickly
        window.tracer(False)

        # go over every cell in the grid
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):

                # find x, y for drawing cell
                x_cor = (tile_size * col) + x_offset
                y_cor = -((tile_size * row) - y_offset)

                # move turtle to the position of the cell in the grid
                self.turt.up() 
                self.turt.goto(x_cor, y_cor)
                self.turt.down()

                if self.grid[row][col] == 0:
                    self.draw_square(tile_size, "white", True)
                
                for block in self.tetrimino.blocks:
                    # checking whether indices within blocks are valid positions within self.grid except for the bottom
                    if block[0] < 0:
                        self.move_right()
                    
                    if block[1] < 0:
                        self.move_right()

                    if block[1] > len(self.grid[0]) - 1:
                        self.move_left()
                    
                    # checking whether tetrimino has reached bottom or touched another tetrimino
                    if block[0] > len(self.grid) - 1 or self.grid[block[0]][block[1]] != 0:
                        for block in self.tetrimino.blocks:
                            # change value of grid units where tetrimino reaches bottom
                            if self.tetrimino.check() == "S":
                                # change value of unit on grid
                                self.grid[block[0] - 1][block[1]] = 1
                            elif self.tetrimino.check() == "Z":
                                # change value of unit on grid
                                self.grid[block[0] - 1][block[1]] = 2
                            elif self.tetrimino.check() == "I":
                                # change value of unit on grid
                                self.grid[block[0] - 1][block[1]] = 3
                            elif self.tetrimino.check() == "J":
                                # change value of unit on grid
                                self.grid[block[0] - 1][block[1]] = 4
                            elif self.tetrimino.check() == "L":
                                # change value of unit on grid
                                self.grid[block[0] - 1][block[1]] = 5
                            elif self.tetrimino.check() == "O":
                                # change value of unit on grid
                                self.grid[block[0] - 1][block[1]] = 6
                            elif self.tetrimino.check() == "T":
                                # change value of unit on grid
                                self.grid[block[0] - 1][block[1]] = 7

                        # stopping game if tetriminos reach the top of the board
                        if self.grid[0][col] != 0:
                            turtle.exitonclick()
                        
                        # making old tetrimino stay where they last stopped
                        if self.grid[row][col] == 1:
                            color = "green"
                            self.draw_square(tile_size, color, True)
                        elif self.grid[row][col] == 2:
                            color = "red"
                            self.draw_square(tile_size, color, True)
                        elif self.grid[row][col] == 3:
                            color = "blue"
                            self.draw_square(tile_size, color, True)
                        elif self.grid[row][col] == 4:
                            color = "purple"
                            self.draw_square(tile_size, color, True)
                        elif self.grid[row][col] == 5:
                            color = "orange"
                            self.draw_square(tile_size, color, True)
                        elif self.grid[row][col] == 6:
                            color = "yellow"
                            self.draw_square(tile_size, color, True)
                        elif self.grid[row][col] == 7:
                            color = "pink"
                            self.draw_square(tile_size, color, True)

                        # make new choice of tetrimino
                        self.tetrimino = random.choice(self.list_tetriminos)()
                        break

                    if row == block[0] and col == block[1]:
                        if block == [row, col]:
                            # checking which tetrimino piece is being drawn 
                            # changing color of drawn square to corresponding tetrimino
                            if self.tetrimino.check() == "S": 
                                #print("works")
                                color = "green"
                                self.draw_square(tile_size, color, True)
                            elif self.tetrimino.check() == "Z": 
                                #print("works")
                                color = "red"
                                self.draw_square(tile_size, color, True)
                            elif self.tetrimino.check() == "I": 
                                #print("works")
                                color = "blue"
                                self.draw_square(tile_size, color, True)
                            elif self.tetrimino.check() == "J": 
                                #print("works")
                                color = "purple"
                                self.draw_square(tile_size, color, True)
                            elif self.tetrimino.check() == "L": 
                                #print("works")
                                color = "orange"
                                self.draw_square(tile_size, color, True)
                            elif self.tetrimino.check() == "O": 
                                #print("works")
                                color = "yellow"
                                self.draw_square(tile_size, color, True)
                            elif self.tetrimino.check() == "T": 
                                #print("works")
                                color = "pink"
                                self.draw_square(tile_size, color, True)


    def draw_score(self):
        ''' draws player's score above the tetris playing board ''' 

        counter = 0

        # clearing a full row
        # loop through every row
        #for row in range(len(self.grid)):
        for row in self.grid:
            if not 0 in row: 
                
                # print(self.grid.index(row))

                # clear writing
                self.turt.score_keeper.clear()

                # increase value of counter
                counter += 100
            
                # rewrite score
                self.turt.score_keeper.penup()
                self.turt.score_keeper.goto(-100, (turtle.window_height() / 2) - 100)
                self.turt.score_keeper.pendown()
                self.turt.score_keeper.write("Player Score: " + str(counter), font=("Verdana", 20, "normal"))
                    
                # switching values back to empty
                for col in range(len(self.grid[0])):
                    self.grid[self.grid.index(row)][col] = 0


# function to make a screen where the playing board will be
def make_window(window_title, bgcolor, width, height):

    '''this functions creates a screen object and returns it'''

    #creating a window variable to set up turtle screen
    window = turtle.getscreen()

    #modify window
    window.title(window_title)
    window.bgcolor(bgcolor)
    window.setup(width, height)
    window.tracer(0)
    turtle.hideturtle()

    return window


def main():

    turtle.hideturtle()

    # create window
    window = make_window("Tetris Game", "white", 600, 800) 

    # create playing grid
    tetris_board = Board()

    # binding keys to methods for moving tetrimino piece
    window.listen()
    window.onkeypress(tetris_board.move_right, "Right")
    window.onkeypress(tetris_board.move_left, "Left")
    window.onkeypress(tetris_board.clockwise_rotation, "Down")

    # testing block

    # testing square class
    #test_square = Square("blue")
    #test_square.draw_square(50)

    # testing move functions with S_tetrimino class
    # s = S_tetrimino()
    # s.move_right()
    # s.move_left()
    # s.move_down()

    # testing drawing tetrimino
    # tetris_board.draw_board(window, -100, 250, 20, "black")

    # draw initial score
    tetris_board.draw_initial_score()

    # infinite while loop
    while True:
        
        # time.sleep(0.1)

        # continuously drawing board so that changes are seen
        tetris_board.draw_score()
        tetris_board.draw_board(window, -100, 250, 20)
        tetris_board.move_down()
        window.update()
         
if __name__ == "__main__":
    main()