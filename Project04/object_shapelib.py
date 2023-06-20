
'''
object_shapelib.py
Adrian Gellert
CS151 C with Al Madi
2nd Semester
Date created: March 21, 2021
Date last modified: March 27, 2021

This file has functions to draw a racetrack with a background.
'''

import turtle
import better_shapelib as sl

window = turtle.getscreen()

def make_turtle(shape='turtle', penColor='white'):
    '''Makes a `Turtle` object

    Parameters:
    -----------
    shape: str.
        From the turtle documentation website, possible options are:
        'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
    penColor: str.
        Color string name (e.g. 'black', 'white', etc) that is to be the pen color of this turtle.

    Returns:
    -----------
    The `Turtle` object that you create.
    '''
    turt = turtle.Turtle()
    turt.shape(shape)
    turt.color(penColor)

    return turt


def goto(turt, x, y, heading = 0):

    '''Changes the position of `john` to draw.'''
    
    # Uses goto and pen up/down functions to move john

    turt.up()
    turt.goto(x, y)
    turt.setheading(heading)
    turt.down()


def circle(turt, x, y, radius, penWidth = "3", fill = True, fillColor = "brown", edgeColor = "black"):

    #, extent = 360, edgeColor = "red", tilt = 0
    '''
    Draws a circle at any position with given `edgeColor` and 
    `fillColor`. 
    '''

    #changes position of turtle
    turt.up()
    turt.goto(x, y)
    turt.down()

    #set color for pen and shape filling
    turt.pensize(penWidth)
    turt.pencolor(edgeColor)
    turt.fillcolor(fillColor)

    #draws circle with given border colors and radii. `john` goes counterclockwise
    turt.begin_fill()
    turt.circle(radius)
    turt.end_fill()


def draw_race_scene():

    '''draws racing scene with turtle, fans, and background scene'''
    
    turtle.tracer(False)

    # calls `make_turtle` to make a turtle to draw racetrack scene
    racetrack_drawer = make_turtle()

    # uses created turtle `racetrack_drawer` to create racing lanes
    circle(racetrack_drawer, 0, -300, 300)
    circle(racetrack_drawer, 0, -200, 200)
    circle(racetrack_drawer, 0, -100, 100, "3", True, "saddle brown")

    #numbering each lane with `racetrack_drawer`
    goto(racetrack_drawer, 0, -200)
    racetrack_drawer.write(str(1), font=('Arial', 20, 'normal'))
    goto(racetrack_drawer, 0, -300)
    racetrack_drawer.write(str(2), font=('Arial', 20, 'normal'))

    racetrack_drawer.hideturtle()
    turtle.tracer(True)

    #draw bench
    sl.draw_rectangle(-234, -230, 240, 20, True, "goldenrod", "goldenrod")
    sl.draw_rectangle(-242, -250, 220, 5, True, "goldenrod", "goldenrod")
    sl.draw_rectangle(-260, -230, 20, 100, True, "goldenrod", "goldenrod")
    sl.draw_rectangle(-420, -230, 20, 100, True, "goldenrod", "goldenrod")
    
    #draw fans
    sl.draw_person(-420, 100, .5)
    sl.draw_person(-520, -180, .5)
    sl.draw_person(-320, 20, .5)
    sl.draw_person(450, -100, .5)
    sl.draw_person(480, 0, .5)
    sl.draw_person(400, 150, .5)


def make_screen(width, height, title, color='black'):
    
    '''Makes a `Screen` object: the window in each turtles can draw shapes

    Parameters:
    -----------
    width: int.
        The width of the window/screen in pixels.
    height: int.
        The height of the window/screen in pixels.
    title: str.
        The name that you'd like to call the pop-up window. Appears at the center of top of the window.
    color: str.
        Color string name (e.g. 'black', 'white', etc). This is the background color of the screen.

    Returns:
    -----------
    The `Screen` object that you create.
    '''

    window = turtle.getscreen()
    window.setup(width, height)
    window.title(title)
    window.bgcolor(color)

    return window


if __name__ == '__main__':

    make_screen(1200, 1000, "Turtle Racing Track for Project 4", "green")
    draw_race_scene()
    turtle.exitonclick()
