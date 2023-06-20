
'''

lab3.py
Adrian Gellert
CS151 C with Al Madi
2nd Semester
Date Created: March 3, 2021
Date Modified: March 11, 2021

This file creates a mondrian style painting of rectangles 
(40% of which are filled wiht colors).

'''

import random
import turtle
import sys

window = turtle.getscreen()
john = turtle.Turtle()
turtle.tracer(False)

def goto(x, y):
    '''
    Changes the position of john to draw. 
    '''
    
    # Uses goto and pen up/down functions to move john

    john.up()
    john.goto(x, y)
    john.down()


def draw_rectangle(x, y, width, height, fill = False, edgeColor = "red", fillColor = "blue", penWidth = "1"):

    '''
    Draws a `width` x `height` rectangle.
    The bottom-left corner of it is positioned at (`x`, `y`).
    '''

    john.pensize(penWidth)
    john.pencolor(edgeColor) 
    john.fillcolor(fillColor) 

    #changes position of rt and colors for pen and shape filling
    goto(x, y)

    if fill == True:
        john.begin_fill()
    
    #draws rectangle
    for i in range (0,2):
        john.forward(width)
        john.left(90)
        john.forward(height)
        john.left(90)

    if fill == True:
        john.end_fill()

    john.pensize()


def main():

    num_rectangles = int(sys.argv[1])

    for i in range(num_rectangles):

        john.pensize(10)

        rand_x = random.randint(-200, 200)
        rand_y = random.randint(-200, 200)

        rand_width = random.randint(50, 150)
        rand_height = random.randint(50, 150)
        
        rand_red = random.random()
        rand_blue = random.random()
        rand_green = random.random()

        if random.random() <= 0.4:
            rand_color = (rand_red, rand_green, rand_blue)
            draw_rectangle(rand_x, rand_y, rand_width, rand_height, True, "black", rand_color)
        else:
            draw_rectangle(rand_x, rand_y, rand_width, rand_height, False, "black", "black")


if __name__ == '__main__':
    
    main()
    turtle.exitonclick()
