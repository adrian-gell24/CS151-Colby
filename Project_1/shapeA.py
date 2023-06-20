'''

Adrian Gellert
February 23, 2021
CS151 C
Project 01

This is a python code that uses turtle to draw a star that is outlined with blue and whose triangular tips are filled with the color blue.

'''

import turtle
window = turtle.getscreen()
sam = turtle.Turtle()

def draw_star(width, fill_color):
    sam.color(fill_color)
    sam.setheading(0)
    
    sam.begin_fill()
    for i in range (0,5):
        sam.forward(width)
        sam.left(216)
    sam.end_fill()

draw_star(100, "blue")
sam.hideturtle()
turtle.hideturtle()
turtle.exitonclick()