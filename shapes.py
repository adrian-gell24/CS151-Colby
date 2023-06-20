'''

Adrian Gellert
February 23, 2021
CS151 C
Project 01

This is a python code containing two different codes for different shapes. 
The first code is for a composite function that combines the two functions I created in shapeA.py and shapeB.py. 
Specifically, it is a Python code that uses turtle to draw a filled pentagon that surrounds a star with only its triangular tips filled. 
The second code is a revision to the composite function code above it, and this second code creates an image of three star in pentagon logos side by side.

'''

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


def draw_pentagon(width, fill_color):
    sam.color(fill_color)
    sam.setheading(0)
    
    sam.begin_fill()
    for i in range (0,5):
        sam.forward(width)
        sam.left(72)
    sam.end_fill()

def draw_logo(x_position, y_position):
#draws a logo consisting of a blue tipped star over a red colored pentagon
    sam.up()
    sam.goto(x_position, y_position)
    sam.down()
    
    draw_pentagon(200, "red")
    sam.up()
    sam.goto((-60 + x_position), (190 + y_position))
    sam.down()
    draw_star(320, "blue")

draw_logo(0,0)
sam.hideturtle()
turtle.hideturtle()
turtle.exitonclick()

'''

#The code below is a revision of the above code so that the logos are scalable and moveable on the turtle window without the components of the logo becoming separated.
import turtle

window = turtle.getscreen()
sam = turtle.Turtle()

def draw_star(width, fill_color, scale):
    sam.color(fill_color)
    sam.setheading(72)
    
    sam.begin_fill()
    for i in range (0,5):
        sam.forward(width*scale)
        sam.left(216)
    sam.end_fill()


def draw_pentagon(width, fill_color, scale):
    sam.color(fill_color)
    sam.setheading(0)
    
    sam.begin_fill()
    for i in range (0,5):
        sam.forward(width*scale)
        sam.left(72)
    sam.end_fill()

def draw_logo(x_position, y_position, scale):
    sam.up()
    sam.goto(x_position, y_position)
    sam.down()
    
    draw_pentagon(200, "red", scale)
    draw_star(320, "blue", scale)

draw_logo(0,0,.5)
draw_logo(-200,50,.2)
draw_logo(175,-100,.2)
draw_logo(-200,-100,.33)
#commands in the four lines above draws four logos in random locations with different sizes.
sam.hideturtle()
turtle.hideturtle()
turtle.exitonclick()
