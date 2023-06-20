
'''
race.py
Adrian Gellert
CS151 C with Al Madi
2nd Semester
Date created: March 21, 2021
Date last modified: March 27, 2021

This file has functions to use object_shapelib.py to create turtles and 
have them race on a track while people in the background cheer them on.
'''


import object_shapelib as osl
import turtle
import math
import random


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
    turt.penup()

    return turt


def move_turtle(turt, speed):
    '''Moves the `Turtle` object `turt` `speed` units
    '''

    #get racer position
    x_pos, y_pos = turt.pos()

    #random speed addition
    jitter = random.randint(1, 1000)

    degrees = (360 + jitter) / speed
    radius = math.sqrt(x_pos ** 2 + y_pos **2)

    turt.circle(radius, degrees)
    return degrees


def main():
    '''Makes racing scene with two racing turtles and a scoreboard
    '''

    osl.make_screen(1200, 1000, "Turtle Racing Track for Project 4", "green")
    turtle.hideturtle()

    #create racetrack scene
    turtle.tracer(False)
    osl.draw_race_scene()
    turtle.tracer(True)

    #create and position racer turtles
    turt1 = make_turtle("turtle", "light green")
    osl.goto(turt1, 0, -150)
    turt1.up()
    turt2 = make_turtle("arrow", "deep sky blue")
    osl.goto(turt2, 0, -250)
    turt2.up()

    #set values for initial score
    lap_lane1 = 0
    lap_lane2 = 0

    #naming scorekeepers for each lane and writing initial score

    #for lane 1
    scorekeeper1 = make_turtle("classic", "midnight blue")
    osl.goto(scorekeeper1, -500, 300)
    scorekeeper1.hideturtle()
    scorekeeper1.write("lane 1:" + str(lap_lane1), font=('Arial', 20, 'normal'))

    #for lane two
    scorekeeper2 = make_turtle("classic", "midnight blue")
    osl.goto(scorekeeper2, -500, 200)
    scorekeeper2.hideturtle()
    scorekeeper2.write("lane 2:" + str(lap_lane2), font=('Arial', 20, 'normal'))

    #setting counter for number of degrees each turtle moves to zero
    degreecounter1 = 0
    degreecounter2 = 0

    #loop to move turtles around race track and update score
    for i in range(0, 1000):

        #totalling number of degrees each turtle moves
        degreecounter1 += move_turtle(turt1, 100)
        degreecounter2 += move_turtle(turt2, 100)

        #if statements that reset the degree counter for each lane and
        #adds one to the score of a racer when it has completee one loop 
        if degreecounter1 > 360:
            lap_lane1 += 1
            degreecounter1 = 0
            scorekeeper1.clear()
            scorekeeper1.write("lane 1:" + str(lap_lane1), font=('Arial', 20, 'normal'))

        if degreecounter2 > 360:
            lap_lane2 += 1
            degreecounter2 = 0
            scorekeeper2.clear()
            scorekeeper2.write("lane 1:" + str(lap_lane2), font=('Arial', 20, 'normal'))


if __name__ == '__main__':
    
    main()

    turtle.exitonclick()
