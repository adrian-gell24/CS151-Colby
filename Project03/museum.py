
'''

museum.py
Adrian Gellert
CS151 C with Al Madi
2nd Semester
Date created: March 17, 2021
Date last modified: March 23, 2021

This file draws a museum scene using functions from better_shapelib.py

'''

import turtle
import better_shapelib as bsl

window = turtle.getscreen()

window.setup(width = 1000, height = 1000)

def museum(): 
    '''Function for drawing a scene that looks like a museum'''

    #draw floor
    bsl.draw_rectangle(500, -100, 1000, 300, True, "saddle brown", "saddle brown")

    #draws background wall
    bsl.draw_rectangle(500, 500, 1000, 600, True, "cyan", "cyan")

    #draw right frame with mondrian painting in it
    bsl.draw_rectangle(300, 300, 250, 250, True, "red", "white")
    bsl.mondrian(200, 200, .43)

    #draw frame for scene of another museum room left of right frame
    bsl.draw_rectangle(-200, 350, 250, 300, True, "dim grey", "burlywood")

    #draw floor of museum in left frame
    bsl.draw_rectangle(-200, 100, 250, 50, True, "dim grey", "brown")

    #draw window with outside scene in left frame
    bsl.draw_rectangle(-220, 330, 200, 100, True, "red", "blue")
    bsl.draw_rectangle(-220, 260, 200, 30, True, "green", "green")
    bsl.draw_rectangle(-250, 290, 15, 50, True, "brown", "brown")
    bsl.draw_triangle2(-243, 285, 30, "green", "green")
    bsl.draw_circle(-370, 285, 15, 360, "gold", "gold")

    #draw poker scene in frame in left, outer frame
    bsl.draw_rectangle(-240, 205, 160, 80)
    #bsl.gaming1(-500, 500, .3)
    bsl.gaming2(-270, 190, 1)

    #draw person watching poker game
    bsl.draw_person(-240, 120, .3)

    #draw person looking at painting containing person watching poker 
    #game with window in the background
    bsl.draw_person(-300, -60, .7)

    #draw couple connected by a heart left of the bench
    bsl.draw_heart(260, -80, 111.65 * .2, 1 * .2)
    bsl.draw_person(240, -190, 1)
    bsl.draw_person(340, -190, 1)

    #draw bench to sit down
    bsl.draw_rectangle(16, -230, 240, 20, True, "goldenrod", "goldenrod")
    bsl.draw_rectangle(8, -250, 220, 5, True, "goldenrod", "goldenrod")
    bsl.draw_rectangle(-10, -230, 20, 100, True, "goldenrod", "goldenrod")
    bsl.draw_rectangle(-170, -230, 20, 100, True, "goldenrod", "goldenrod")




museum()
turtle.hideturtle()
turtle.exitonclick()


