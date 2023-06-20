
'''
project6.py
Adrian Gellert
CS151 C with Al Madi
2nd Semester
Date created: March 31, 2021
Date last modified: April 11, 2021

This file uses python to create the game tic tac toe. 
'''

import turtle
import numpy

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


def make_turtle(shape, color, stretch_width, stretch_length, x_pos, y_pos):

    ''' creates a turtle and sets initial postion, returns the turtle '''

    #variable to create turtle
    turt = turtle.Turtle()

    #modifying turtle
    turt.shape(shape)
    turt.color(color)
    turt.shapesize(stretch_width, stretch_length)
    turt.up()
    turt.goto(x_pos, y_pos)

    return turt


def make_grid(rows, cols):

    '''make a rows x cols grid with values 0 and returns it'''

    grid = []

    for i in range(rows):
        grid.append([0] * cols)

    return grid


def goto(turt, x_pos, y_pos):

    '''function to move turtle to position without drawing on window'''

    turt.up()
    turt.goto(x_pos, y_pos)
    turt.down()


def square(side):

    '''function to draw a square'''

    global my_turtle
    my_turtle.pensize(2)

    #keep square surrounding center points of grid
    my_turtle.setheading(90)
    my_turtle.up()
    my_turtle.forward(side / 2)

    #half of top side of square
    my_turtle.down()
    my_turtle.right(90)
    my_turtle.forward(side / 2)
    my_turtle.right(90)

    #three sides of square
    for i in range(3):
        my_turtle.forward(side)
        my_turtle.right(90)
    
    #complete square
    my_turtle.forward(side / 2)


#global scope, usable by all functions afterwards
window = make_window("Tic Tac Toe", "light sky blue", 800, 600)
my_turtle = make_turtle("classic", "white", 1, 1, 0, 0)
picasso = make_turtle("classic", "white", 1, 1, 0, 0)
writer = make_turtle("turtle", "black", 1, 1, -25, 200)
my_grid = make_grid(3, 3)
game_grid = numpy.array(my_grid)
reversed_arr = game_grid[::-1]
player1_counter = 0
player2_counter = 0
draw_counter = 0

#print(game_grid)
y_offset = 50
x_offset = -50
tile_size = 50
turn = 1


def draw_grid(grid, turt, x_offset, y_offset, tile_size):
    '''draws a grid at x, y with a specific tile_size'''
    
    turt.hideturtle()
    picasso.hideturtle()
    writer.hideturtle()

    # loop over grid cells
    for row in range (len(grid)):
        for col in range (len(grid[row])):
            
            # find x, y for drawing the cell
            x_cor = (tile_size * col) + x_offset
            y_cor = -((tile_size * row) - y_offset)

            goto(turt, x_cor, y_cor)

            # if cell value is 1 draw "x"
            if grid[row][col] == 1:
                # subtracted values in goto to make turtle write so that
                # x's center is in the center of tile and not the bottom 
                # left of the x
                goto(picasso, x_cor - 8, y_cor - 12) 
                picasso.write("x", font=("Verdana", 30, "normal"))

            # if cell value is 2 draw "o"
            elif grid[row][col] == 2:
                #same as above if statement
                goto(picasso, x_cor - 8, y_cor - 12)
                picasso.write("o", font=("Verdana", 30, "normal"))

            # else draw an empty spot
            else:
                square(tile_size)


def play(x_pos, y_pos):

    ''' This function is called everytime there is a click on the screen

    python passes the position of the click to us through the arguments

    x_pos: click c-position

    y_pos: click y-position

    '''

    global turn
    global player1_counter
    global player2_counter
    global draw_counter

    # changing clicked x and y position to value of row and column in 
    # grid
    row = int(abs((y_pos - y_offset - (tile_size/2)) // (tile_size) + 1))
    col = int(abs((x_pos - x_offset - (tile_size/2)) // (tile_size) + 1))

    # change the clicked cell in the grid to hold the value in turn
    if game_grid[row][col] == 0:
        game_grid[row][col] = turn

        # switch turns
        if turn == 1:
            turn = 2
        else:
            turn = 1

    # draw the grid and update window after each click
    draw_grid(game_grid, my_turtle, x_offset, y_offset, tile_size)

    # write initial score 
    writer.write(str(player1_counter) + ":" + str(draw_counter) +":" + str(player2_counter), font=("Verdana", 30, "normal"))

    # check winner and change written score

    # check grid from left to right
    if check_win(game_grid, 1):
        writer.clear()
        player1_counter += 1
        writer.write(str(player1_counter) + ":" + str(draw_counter) +":" + str(player2_counter), font=("Verdana", 30, "normal"))
        
        if input("clear board? ") == "Yes":
            picasso.clear()
            game_grid[game_grid > 0] = 0
            return player1_counter
        else:
            turtle.exitonclick()
    elif check_win(game_grid, 2):
        writer.clear()
        player2_counter += 1
        writer.write(str(player1_counter) + ":" + str(draw_counter) +":" + str(player2_counter), font=("Verdana", 30, "normal"))
        if input("clear board? ") == "Yes":
            picasso.clear()
            game_grid[game_grid > 0] = 0
            return player1_counter
        else:
            turtle.exitonclick()
    
    #check grid from right to left
    if check_win(reversed_arr, 1):
        writer.clear()
        player1_counter += 1
        writer.write(str(player1_counter) + ":" + str(draw_counter) +":" + str(player2_counter), font=("Verdana", 30, "normal"))
        if input("clear board? ") == "Yes":
            picasso.clear()
            game_grid[game_grid > 0] = 0
            return player2_counter
        else:
            turtle.exitonclick()
    elif check_win(reversed_arr, 2):
        writer.clear()
        player2_counter += 1
        writer.write(str(player1_counter) + ":" + str(draw_counter) +":" + str(player2_counter), font=("Verdana", 30, "normal"))
        if input("clear board? ") == "Yes":
            picasso.clear()
            game_grid[game_grid > 0] = 0
            return player2_counter
        else:
            turtle.exitonclick()

    #checking for a draw
    if input("full board?") == "Yes":
        writer.clear()
        draw_counter += 1
        writer.write(str(player1_counter) + ":" + str(draw_counter) +":" + str(player2_counter), font=("Verdana", 30, "normal"))
        picasso.clear()
        game_grid[game_grid > 0] = 0
        return player2_counter
    else:
        draw_grid(game_grid, my_turtle, x_offset, y_offset, tile_size)


def check_win(grid, player):

    ''' checks the winner in the grid
    returns true if player won
    returns false if player lost

    player is an int the represents turn (1/2)
    '''

    counter = 0

    # check rows
    for row in range(len(grid)):
        counter = 0
        for col in range(len(grid[0])):

            if grid[row][col] == player:
                counter += 1
            else:
                counter = 0
            
            if counter == 3:
                return True 
           
    # check columns
    for col in range(len(grid)):
        counter = 0
        for row in range(len(grid[0])):

            if grid[row][col] == player:
                counter += 1
            else:
                counter = 0
            
            if counter == 3:
                return True
    
    # check diagonal \ and /
    for i in range(len(grid)):
        counter = 0
        for i in range(len(grid[0])):

            if grid[i][i] == player:
                counter += 1
            else:
                counter = 0
            
            if counter == 3:
                return True    


def main():

    draw_grid(game_grid, my_turtle, -50, 50, 50)

    window.listen()
    window.onscreenclick(play)

    while True:

        # keeps the game running
        window.update()


if __name__ == "__main__":
    main()
    ################################worked with Ashley to fix making game board and writing x's and o's