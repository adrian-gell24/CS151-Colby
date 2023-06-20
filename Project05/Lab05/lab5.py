
'''
lab5.py
Adrian Gellert
CS151 C with Al Madi
2nd Semester
Date created: March 25, 2021
Date last modified: March 25, 2021

This file creates a basic scene of the "Soaring Thunderbird" game. 
The only animated addition to this scene is the movement of the glider 
down towards the left or right.
'''

import turtle

def make_window(window_title, bgcolor, width, height):
    
    '''this function creates a screen object and returns it'''

    window = turtle.getscreen()
    window.setup(width, height)
    window.title(window_title)
    window.bgcolor(bgcolor)
    window.tracer(False)

    return window


def make_turtle(shape, color, stretch_width, stretch_length, x_pos, y_pos):

    ''' creates a turtle and sets initial position '''

    turt = turtle.Turtle()
    turt.shape(shape)
    turt.color(color)
    turt.shapesize(stretch_width, stretch_length)
    turt.up()
    turt.goto(x_pos, y_pos)
    turt.down()

    return turt


def main():

    ''' creates Soaring Thunderbird game '''

    window = make_window("Soaring Thunderbird - A CS151 original!", "light sky blue", 800, 600)

    #sets background to a gif image
    window.bgpic("sky.gif") 

    #adding to allowed images for turtles
    window.addshape("glider_image_left.gif")
    window.addshape("glider_image_right.gif")
    
    # airport
    airport = make_turtle("square", "dark gray", 1, 5, 0, -295)

    # glider
    glider = make_turtle("glider_image_right.gif", "white", 0.51, 0.51, 0,300)

    def go_left():
        glider.shape("glider_image_left.gif")
        glider.setheading(180)
        glider.left(10)


    def go_right():
        glider.shape("glider_image_right.gif")
        glider.setheading(0)
        glider.right(10)

    window.onkeypress(go_left, "Left")
    window.onkeypress(go_right, "Right")

    #Listen for keyboard input
    window.listen()              

    # Main game loop
    while True:
        window.update()
        glider.forward(0.01)
        
        
if __name__ == "__main__":
    main()

    turtle.hideturtle()
    turtle.exitonclick()

