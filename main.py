
'''

lab2.py
Adrian Gellert
CS151 C with Al Madi
2nd Semester
March 7, 2021

This file...

'''

import turtle
import shapelib as sl 
#turtle.speed(1)
turtle.tracer(False)

def testScene(x, y, scale):

    '''
    draws a triangle stack using function from shapelib.py as test
    '''

    sl.draw_triangleStack(x, y, scale)


def draw_circle(x, y, radius, extent, tilt, outside_color, inside_color):

    '''
    draws a circle using function from shapelib.py
    '''

    sl.draw_circle(x, y, radius, extent, tilt, outside_color, inside_color)


def draw_card(x, y, width, height, scale, outside_color, inside_color):

    '''
    draws playing card using function from shapelib.py
    '''

    sl.draw_playingcard(x, y, width, height, scale, outside_color, inside_color)


def draw_heart(x, y, scale):

    '''
    draws heart using function from shapelib.py
    '''

    sl.draw_heart(x, y, scale)


def draw_diamond(x, y, scale):

    ''' 
    draws diamond using function from shapelib.py
    '''

    sl.draw_diamond(x, y, scale)


def draw_diamond_card(x, y, width, height, outside_color, inside_color, scale, scale1, scale2):

    '''
    draws a six of diamond card using function from shapelib.py
    '''

    sl.draw_diamond_card(x, y, width, height, outside_color, inside_color, scale, scale1, scale2)


def draw_heart_card(x, y, width, height, outside_color, inside_color, scale, scale1, scale2):

    '''
    draws a three of hearts card using function from shapelib.py
    '''

    sl.draw_heart_card(x, y, width, height, outside_color, inside_color, scale, scale1, scale2)


def draw_board(x, y, radius, extent, tilt1, tilt2, width, height, scale, outside_color, inside_color):

    '''
    draws a playing board/table using function from shapelib.py
    '''

    sl.draw_board(x, y, radius, extent, tilt1, tilt2, width, height, scale, outside_color, inside_color)


def gaming1(x, y, radius, extent, tilt, tilt1, width, height, scale, outside_color, inside_color, x1, x2, x3, y1, width1, height1, scale1, outside_color1, inside_color1, x4, inside_color2, scale2, scale3, x5, y2, width2, height2, x6, x7, x8, x9, y3, radius1, extent2, tilt2, inside_color3):

    '''
    function that draws a poker game scenario
    '''

    draw_board(0, 0, 0, 180, 0, 180, 0, 0, 2, "green", "green")

    #draws cards in center of board/table that players use
    #in conjunction with their cards to make a "hand" 
    #made of five cards
    draw_card(-125, 0, 100, 120, .5, "black", "red")
    draw_card(-50, 0, 100, 120, .5, "black", "red")
    draw_card(25, 0, 100, 120, .5, "black", "red")
    draw_diamond_card(200, 0, 100, 120, "black", "white", 1, .1, .5)
    draw_heart_card(350, 0, 100, 120, "black", "white", 1, .1, .5)

    #draws visible card for each player (each player has two cards)
    draw_card(450, -175, 30, 50, 1, "black", "red")
    draw_card(-450, -175, 30, 50, 1, "black", "red")

    #draws poker chips that each player has
    draw_circle(-480, -155, 10, 360, 0, "white", "blue")
    draw_circle(-455, -155, 10, 360, 0, "white", "red")
    draw_circle(-430, -155, 10, 360, 0, "white", "green")
    draw_circle(-405, -155, 10, 360, 0, "white", "black")
    draw_circle(450, -155, 10, 360, 0, "white", "blue")
    draw_circle(425, -155, 10, 360, 0, "white", "red")
    draw_circle(400, -155, 10, 360, 0, "white", "green")
    draw_circle(375, -155, 10, 360, 0, "white", "black")


#main code

#testScene(0, 0, 1)
#turtle.exitonclick()

#simple shapes
#draw_circle(0, 0, 50, 360, 0, "black", "white")
#draw_card(0, 0, 50, 100, 1, "black", "white")

#gaming themed shapes
#draw_diamond_card(0, 0, 100, 120, "black", "white", 1, .1, .5)
#draw_board(0, 0, 0, 180, 0, 180, 0, 0, .5, "green", "green")

gaming1(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

turtle.hideturtle()
turtle.penup()
turtle.exitonclick()

