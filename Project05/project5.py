
'''
lab5.py
Adrian Gellert
CS151 C with Al Madi
2nd Semester
Date created: March 29, 2021
Date last modified: March 29, 2021

This file creates the fully remade "Soaring Thunderbird" game 
(with some additions)
'''

import turtle
import random

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

    window_width = 800
    window_height = 600

    # window
    window = make_window("Soaring Thunderbird - A CS151 original!", "light sky blue", window_width, window_height)

    # sets background to a gif image
    window.bgpic("sky.gif") 

    # adding to allowed images for turtles
    window.addshape("glider_image_left.gif")
    window.addshape("glider_image_right.gif")
    
    # airport
    airport_ypos = -295
    airport = make_turtle("square", "dark gray", 1, 5, 0, airport_ypos)
    airport.up()

    # glider
    glider = make_turtle("glider_image_right.gif", "white", 0.51, 0.51, 0, 300)
    glider.up()

    #setting speed of glider
    glide = 0.2

    # score keeping
    player_1_score = 0
    gravity_score = 0

    # writer turtle
    writer = make_turtle('classic', 'white', 1, 1, -150, 269)
    writer.hideturtle()

    # write initial score
    writer.write("Player 1: 0   Gravity: 0", font=('Arial', 30, 'normal'))    

    # key binding functions 
    #make glider go left
    def go_left():
        glider.shape("glider_image_left.gif")
        glider.setheading(180)
        glider.left(10)

    #make glider go right
    def go_right():
        glider.shape("glider_image_right.gif")
        glider.setheading(0)
        glider.right(10)

    # connecting buttons to functions
    window.listen() 
    window.onkeypress(go_left, "Left")
    window.onkeypress(go_right, "Right")  

    # Main game loop
    while True:

        turtle.hideturtle()
        
        window.update()

        glider.forward(glide)

        # checking bottom bound of window and updating the score

        # checking if glider is within bounds of airport turtle and 
        # adding to player 1's score
        if (glider.xcor() < (airport.xcor() + 50)
            and glider.xcor() > (airport.xcor() - 50)
            and glider.ycor() > airport_ypos
            and glider.ycor() < (airport_ypos + 10)):

            #reset
            glider.setposition(0, 300)

            #change score
            player_1_score += 1
            writer.clear()
            score = ("Player 1:" 
                    + str(player_1_score)
                    +"    Gravity:"
                    +str(gravity_score))
            
            writer.write(score, font=('Arial', 30, 'normal'))

            # speed up glider
            glide *= 1.1

            # change position of airport to random position
            airport_xpos = random.randint(-350, 350)
            airport.setx(airport_xpos)
        
        # checking if glider goes below y cor of airport and adds to 
        # gravity's score
        elif glider.ycor() < airport_ypos:

            gravity_score += 1
            glider.setposition(0, 300)

            writer.clear()
            score = ("Player 1:" 
                    + str(player_1_score) 
                    + "    Gravity:" 
                    + str(gravity_score))

            writer.write(score, font=('Arial', 30, 'normal'))

            # speed up glider
            glide *= 1.1

            # change position of airport to random position
            airport_xpos = random.randint(-350, 350)
            airport.setx(airport_xpos)

        if gravity_score == 25:

            writer.clear()
            writer.up()
            writer.goto(-375, 0)
            writer.down()
            writer.color("red")
            writer.write("Game Over! Sorry, Gravity Won.", font=('Arial', 50, 'bold'))
            turtle.exitonclick()

        if player_1_score == 25:

            writer.clear()
            writer.up()
            writer.goto(-375, 0)
            writer.down()
            writer.color("green")
            writer.write("Game Over! Good Job. You Landed!!", font=('Arial', 40, 'bold'))
            turtle.exitonclick()
        
        
if __name__ == "__main__":
    main()
    
    turtle.hideturtle()
    turtle.exitonclick()

