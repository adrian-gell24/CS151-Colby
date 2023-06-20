
'''
lab4.py
Adrian Gellert
CS151 C with Al Madi
2nd Semester
Date created: March 17, 2021
Date last modified: March 26, 2021

This file has functions to draw a matrix like animation using turtles.
'''

import random
import turtle

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


def reset_turtle(turt, screen_width, screen_height):

    '''
    Function that moves turtle to random position at top of turtle 
    window, sets it heading to south and makes it a random color.
    '''

    rand_x = random.randint(-screen_width / 2, screen_width / 2)
    turt.goto(rand_x, screen_height / 2)
    
    turt.setheading(270)

    rand_red = random.random()
    rand_blue = random.random()
    rand_green = random.random()
    rand_color = (rand_red, rand_blue, rand_green)

    turt.color(rand_color)


def move_and_stamp(turt, distance):

    rand_addition = random.randint(0, 10)

    turt.stamp()
    turt.forward(distance + rand_addition)
    turt.stamp()


def writeNumStrides(turt, numStrides):
    
    turt.clear()
    turt.goto(200, 100)
    turt.hideturtle()

    turt.write(numStrides, font = ('Arial', 30, 'normal'))
    


def main():

    '''
    Function that sets values for parameters in functions above and 
    keeps turtle window visible.
    '''

    # calls `make_screen` with set values for parameters
    screen = make_screen(500, 400, "Lab 4: Matrix Scene Using Turtles")

    # calls `make_turtle` three times with set values for parameters  
    # moves three turtles to different positions on screen
    turt1 = make_turtle("circle", "blue")
    turt1.goto(-200, 0)
    turt2 = make_turtle("turtle", "green")
    turt2.goto(-50, -50)
    turt3 = make_turtle("square", "red")
    turt3.goto(100, 100)

    # calls `reset_turtle` for three turtles created previously with set
    # values for parameters
    reset_turtle(turt1, 500, 400)
    reset_turtle(turt2, 500, 400)
    reset_turtle(turt3, 500, 400)

    #making writer to count number of times a turtle reaches the end of
    #the screen
    writer = make_turtle()
    writer.hideturtle()
    writer.color("white")

    turtle_length_count = 0

    # calls 
    for i in range (1000):

        #writeNumStrides(writer, i)
        #writeNumStrides(turt2, numStrides)
        #writeNumStrides(turt3, numStrides)

        move_and_stamp(turt1, 40)
        move_and_stamp(turt2, 30)
        move_and_stamp(turt3, 20)

        if turt1.ycor() < -200:
            #turt1.speed(10)
            turtle_length_count += 1
            writeNumStrides(writer, turtle_length_count)
            reset_turtle(turt1, 500, 400)
            
        
        elif turt2.ycor() < -200:
            #turt2.speed(10)
            turtle_length_count += 1
            writeNumStrides(writer, turtle_length_count)
            reset_turtle(turt2, 500, 400)

        elif turt3.ycor() < -200:
            #turt3.speed(10)
            turtle_length_count += 1
            writeNumStrides(writer, turtle_length_count)
            reset_turtle(turt3, 500, 400)
                


if __name__ == '__main__':

    main()