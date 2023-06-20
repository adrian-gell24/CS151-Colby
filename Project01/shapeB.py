'''

Adrian Gellert
February 23, 2021
CS151 C
Project 01

This is a python code that uses turtle to draw a pentagon that is outlined and filled with the colored red.

'''

import turtle
window = turtle.getscreen()
sam = turtle.Turtle()

def draw_pentagon(width, fill_color):
    sam.color(fill_color)
    sam.setheading(0)
    
    sam.begin_fill()
    for i in range (0,5):
        sam.forward(width)
        sam.left(72)
    sam.end_fill()

draw_pentagon(200,"red")
sam.hideturtle()
turtle.hideturtle()
turtle.exitonclick()