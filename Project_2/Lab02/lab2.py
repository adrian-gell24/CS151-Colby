
'''

lab2.py
Adrian Gellert
CS151 C with Al Madi
2nd Semester
February 25, 2021

This file draws an equilateral triangle starting at its lower-left
corner and first drawing the base of the triangle.

'''

import turtle
window = turtle.getscreen()
tr = turtle.Turtle()

def draw_triangle1(side_length):
    '''
    Draws a triangle with any side length (`side_length`)
    '''
    
    # Loop for drawing triangle using forward and left functions

    for i in range (0,3):
        tr.forward(side_length)
        tr.left(120)


def goto(x, y):
    '''
    Changes the position of tr. 
    '''
    
    # Uses goto and pen up/down functions to move tr

    print('goto(): going to', x, y)
    print('goto(): before move, turtle at', tr.position())
    tr.up()
    tr.goto(x,y)
    tr.down()
    print('goto(): after move, turtle now at', tr.position())


def draw_triangle2(x, y, scale):
    
    '''
    Draws a triangle at any (`x`, `y`) position and scale (`scale`)

    By default, the side lengths are 100 (when `scale` = 1)
    '''

    #calls triangle1 function with default eastward direction
    #calls triangle1 function with default side lengths of 100
    
    goto(x, y)
    draw_triangle1(100*scale)


def draw_triangleStack(x, y, scale):

    '''
    Draws three triangles on top of each other.

    Smaller triangles are placed on top of larger ones
    '''

    # Largest triangle

    draw_triangle2((0 + x)*scale, (0 + y)*scale, 2*scale)

    # Medium triangle in middle

    draw_triangle2((50 + x)*scale, (173.2 + y)*scale, 1*scale)

    # Small triangle on top of stack

    draw_triangle2((75 + x)*scale, (259.81 + y)*scale, 0.5*scale)


#maincode 


#sets tr's drawing direction and drawing speed

tr.setheading(0)
tr.speed(6)

#draws three triangles on window using triangle1 and goto function

#goto(0, 0)
#draw_triangle1(100)
#goto(-100, 100)
#draw_triangle1(100)
#goto(100, 100)
#draw_triangle1(100)

#draws three differently scaled triangles using triangle2 function

#draw_triangle2(0, 0, 1)
#draw_triangle2(-50, 0, 2)
#draw_triangle2(-100, 0, 3)

#triangleStack(0, 0, 1)

#draws three side-by-side triangle stacks with different scalings

draw_triangleStack(-200, 0, 1)
draw_triangleStack(0, 0, 1/2)
draw_triangleStack(300, 0, 1/3)

turtle.hideturtle()
turtle.exitonclick()