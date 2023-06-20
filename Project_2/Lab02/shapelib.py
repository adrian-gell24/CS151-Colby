
'''

lab2.py
Adrian Gellert
CS151 C with Al Madi
2nd Semester
March 7, 2021

This file draws an equilateral triangle starting at its lower-left
corner and first drawing the base of the triangle.

'''

import turtle
window = turtle.getscreen()
tr = turtle.Turtle()

def draw_triangle1(side_length):
    '''
    Draws a triangle with any side length (`side_length`)
    '''
    
    # Loop for drawing triangle using forward and left functions

    for i in range (0,3):
        tr.forward(side_length)
        tr.left(120)


def goto(x, y):
    '''
    Changes the position of tr. 
    '''
    
    # Uses goto and pen up/down functions to move tr

    print('goto(): going to', x, y)
    print('goto(): before move, turtle at', tr.position())
    tr.up()
    tr.goto(x, y)
    tr.down()
    print('goto(): after move, turtle now at', tr.position())


def draw_triangle2(x, y, scale):
    
    '''
    Draws a triangle at any (`x`, `y`) position and scale (`scale`)

    By default, the side lengths are 100 (when `scale` = 1)
    '''

    #calls triangle1 function with default eastward direction
    #calls triangle1 function with default side lengths of 100
    
    goto(x, y)
    draw_triangle1(100*scale)


def draw_triangleStack(x, y, scale):

    '''
    Draws three triangles on top of each other.

    Smaller triangles are placed on top of larger ones
    '''

    # Largest triangle

    draw_triangle2((0 + x)*scale, (0 + y)*scale, 2*scale)

    # Medium triangle in middle

    draw_triangle2((50 + x)*scale, (173.2 + y)*scale, 1*scale)

    # Small triangle on top of stack

    draw_triangle2((75 + x)*scale, (259.81 + y)*scale, 0.5*scale)


def draw_circle(x, y, radius, extent, tilt, outside_color, inside_color):

    '''
    Draws an oval using segments from circles of two different radii.
    '''

    #changes position of ov and direction in which it will draw
    goto(x, y)
    tr.seth(0 + tilt)

    #set color for pen and shape filling
    tr.pencolor(outside_color)
    tr.fillcolor(inside_color)

    #draws oval with given border colors and radii.
    tr.begin_fill()
    tr.circle(radius, extent)
    tr.end_fill()

    tr.hideturtle()


def draw_playingcard(x, y, width, height, scale, outside_color, inside_color):

    '''
    Draws a rectangular playing card
    '''

    #changes position of rt and colors for pen and shape filling 
    #also changes pen size
    goto(x, y)
    tr.pensize(2)
    tr.pencolor(outside_color)
    tr.fillcolor(inside_color)

    tr.setheading(180)

    #draws playing card
    tr.begin_fill()
    for i in range (0,2):
        tr.forward(width*scale)
        tr.left(90)
        tr.forward(height*scale)
        tr.left(90)
    tr.end_fill()

    tr.hideturtle()


def draw_heart(x, y, scale):

    '''
    function to draw a heart
    '''

    #changes position to draw heart 
    goto(x, y)

    #set color for pen and shape filling
    tr.pencolor("red")
    tr.fillcolor("red")

    #draws heart
    tr.begin_fill()
    tr.setheading(0)
    tr.left(140)
    tr.forward(111.65*scale)
    for i in range(200):
        tr.right(1)
        tr.forward(1*scale)
    tr.left(120)
    for i in range(200):
        tr.right(1)
        tr.forward(1*scale)
    tr.forward(111.65*scale)
    tr.end_fill()

    tr.hideturtle()


def draw_diamond(x, y, scale):

    '''
    draws a diamond from two triangles
    '''

    #changes pen color and color to fill shape
    #also sets heading of `tr` back to heading east
    tr.pencolor("red")
    tr.fillcolor("red")
    tr.setheading(0)

    #draws diamond with red as border and fill color
    tr.begin_fill()
    draw_triangle2(x, y, scale)
    tr.right(60)
    draw_triangle2(x, y, scale)
    tr.end_fill()

    tr.hideturtle()

def draw_diamond_card(x, y, width, height, outside_color, inside_color, scale, scale1, scale2):

    '''
    draws a six of diamonds card
    '''

    #draws card with certain border color (`outside_color`)
    #and fill color (`inside_color`)
    draw_playingcard((0+x)*scale2, (0+y)*scale2, width, height, scale*scale2, outside_color, inside_color)

    #draws six diamonds within the border of the card
    draw_diamond((-75+x)*scale2, (-100+y)*scale2, scale1*scale2)
    draw_diamond((-75+x)*scale2, (-60+y)*scale2, scale1*scale2)
    draw_diamond((-75+x)*scale2, (-20+y)*scale2, scale1*scale2)
    draw_diamond((-35+x)*scale2, (-100+y)*scale2, scale1*scale2)
    draw_diamond((-35+x)*scale2, (-60+y)*scale2, scale1*scale2)
    draw_diamond((-35+x)*scale2, (-20+y)*scale2, scale1*scale2)

    tr.hideturtle()


def draw_heart_card(x, y, width, height, outside_color, inside_color, scale, scale1, scale2):

    '''
    draws a three of hearts card
    '''

    #draws card with certain border color (`outside_color`)
    #and certain fill color (inside_color)
    draw_playingcard((0+x)*scale2, (0+y)*scale2, width, height, scale*scale2, outside_color, inside_color)

    #draws three hearts within the border of the card
    draw_heart((-50+x)*scale2, (-110+y)*scale2, scale1*scale2)
    draw_heart((-50+x)*scale2, (-70+y)*scale2, scale1*scale2)
    draw_heart((-50+x)*scale2, (-30+y)*scale2, scale1*scale2)

    tr.hideturtle()


def draw_board(x, y, radius, extent, tilt1, tilt2, width, height, scale, outside_color, inside_color):

    '''
    draws a playing board/table
    '''

    #draws a table from two half circles and a rectangle
    draw_circle((250+x)*scale, (-100+y)*scale, (75+radius)*scale, extent, tilt1, outside_color, inside_color)
    draw_playingcard((250+x)*scale, (50+y)*scale, (500+width), (150+height), scale, outside_color, inside_color)
    draw_circle((-250+x)*scale, (50+y)*scale, (75+radius)*scale, extent, tilt2, outside_color, inside_color)

    tr.hideturtle()
