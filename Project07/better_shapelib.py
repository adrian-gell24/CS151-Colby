
'''

better_shapelib.py
Adrian Gellert
CS151 C with Al Madi
2nd Semester
Date created: March 11, 2021
Date last modified: March 23, 2021

This file contains functions for different shapes and scenes such as a 
heart shape and a Mondrian painting. These functions can be used in 
different Python files in order to simplify the coding process in those.

'''

import turtle
import random

window = turtle.getscreen()
john = turtle.Turtle()

def goto(x, y):

    '''Changes the position of `john` to draw.'''
    
    # Uses goto and pen up/down functions to move john

    john.up()
    john.goto(x, y)
    john.down()

    john.hideturtle()


def draw_rectangle(x, y, width, height, fill = True, edgeColor = "red", fillColor = "blue", penWidth = "1"):

    '''Draws a rectangle. The rectangle begings at `x`, `y` and draws counterclockwise.'''

    # sets `john`'s pen and fill color, also sets pen size
    john.pensize(penWidth)
    john.pencolor(edgeColor) 
    john.fillcolor(fillColor) 

    turtle.tracer(10)

    #changes position of `john`
    goto(x, y)
    john.setheading(180)

    #decides to fill rectangle or not
    if fill == True:
        john.begin_fill()
    
    #draws rectangle with certain width and height
    for i in range (0,2):
        john.forward(width)
        john.left(90)
        john.forward(height)
        john.left(90)
    
    if fill == True:
        john.end_fill()

    john.hideturtle()


def mondrian(x, y, scale, numRectangles = 100):

    ''' Function draws a mondrian style painting with 40% of the 
    rectangles drawn filled. Each mondrian function called can be
    positioned and scaled.'''

    #num_rectangles = int(sys.argv[1])

    #image drawn quickly with each rectangle with edge widths 10
    john.pensize(10)
    turtle.tracer(False)

    #loop to create mondrian style painting
    for i in range(numRectangles):

        #name positional variables as random for rectangle 
        rand_x = (random.randint(-200, 200)) 
        rand_y = (random.randint(-200, 200)) 

        #name width and height variables as random for rectangle 
        rand_width = (random.randint(50, 150)) 
        rand_height = (random.randint(50, 150)) 

        #name color variables as random for rectangle
        rand_red = random.random()
        rand_blue = random.random()
        rand_green = random.random()
        rand_edgeColor = (rand_red, rand_green, rand_blue)
        rand_fillColor = (rand_red, rand_green, rand_blue)

        #if statement to draw rectangles and decide whether they will 
        # be filled or transparent. Size and placement of mondrian 
        # painting rectangles can be scaled or changed
        if random.random() <= 0.4:
            draw_rectangle((rand_x * scale) + x, (rand_y * scale) + y, rand_width * scale, rand_height * scale, True, rand_edgeColor, rand_fillColor)

        else:
            draw_rectangle((rand_x * scale) + x, (rand_y * scale) + y, rand_width * scale, rand_height * scale, False, rand_edgeColor, rand_fillColor)

    john.hideturtle()
    turtle.tracer(True)


def draw_triangle1(side_length, edgeColor = "red", fillColor = "blue", penWidth = "1"):
    '''
    Draws a triangle with any side length (`side_length`) and any
    `edgeColor` and `fillColor`. 
    '''

    #set color for pen and shape filling
    john.pensize(penWidth)
    john.pencolor(edgeColor)
    john.fillcolor(fillColor)
    
    # Loop for drawing triangle using forward and left functions
    john.begin_fill()
    for i in range (0, 3):
        john.forward(side_length)
        john.right(120)
    john.end_fill()


def draw_triangle2(x, y, side_length, edgeColor = "red", fillColor = "blue", penWidth = "1"):
    
    '''
    Draws triangle given by triangle1 at any (`x`, `y`) position and 
    scalable by `scale`. 
    This is simple shape 1 that simplifies the draw_triangle1 function.
    '''

    #calls triangle1 function with default side lengths of 100
    goto(x, y)
    draw_triangle1(side_length, edgeColor, fillColor, penWidth)

    john.hideturtle()


def draw_circle(x, y, radius, extent = 360, edgeColor = "red", fillColor = "blue", tilt = 0, penWidth = "1"):

    '''
    Draws a circle at any position with given `edgeColor` and 
    `fillColor`. 
    This is my simple shape 2.
    '''

    turtle.tracer(False)

    #changes position of john and direction in which it will draw
    goto(x, y)
    john.seth(tilt)

    #set color for pen and shape filling
    john.pensize(penWidth)
    john.pencolor(edgeColor)
    john.fillcolor(fillColor)

    #draws circle with given border colors and radii. `john` goes counterclockwise
    john.begin_fill()
    john.circle(radius, extent)
    john.end_fill()

    john.hideturtle()
    turtle.tracer(True)


def draw_heart(x, y, straight_angled_bottom = 111.65, distance = 1, edgeColor = "red", fillColor = "red", penWidth = "1"):

    '''
    Function to draw a heart shape at any position with given 
    `edgeColor` and `fillColor`. 
    This is an extra, simple shape.
    '''

    turtle.tracer(False)

    #changes position to draw heart 
    goto(x, y)

    #set color for pen and shape filling
    john.pensize(penWidth)
    john.pencolor(edgeColor)
    john.fillcolor(fillColor)

    #naming variables for the values needed as part of each command to
    #draw the heart 
    for_left_side = 140
    for_right_side = 120
    ear = 200
    make_curve = 1

    #draws heart 
    #`distance` and `straight_angled_bottom` are values that if scaled
    #scale the size of the heart as a whole, so they are set as 
    #parameters of the function
    john.begin_fill()
    john.setheading(0)
    john.left(for_left_side) 
    john.forward(straight_angled_bottom)
    for i in range(ear):
        john.right(make_curve)
        john.forward(distance)
    john.left(for_right_side)
    for i in range(ear):
        john.right(1)
        john.forward(distance)
    john.forward(straight_angled_bottom)
    john.end_fill()

    john.hideturtle()
    turtle.tracer(True)


def draw_heart_card(x, y, scale_shape, fill = False, cardEdge = "black", cardColor = "white"):

    '''
    Function that draws a three of hearts card with randomly colored hearts and
    randomly colored edges of cards.
    This is my first compound shape.
    '''

    #base of rectangle, randomly chosen to position hearts within
    width = 30

    #height of rectangle, randomly chosen to position hearts within
    height = 48

    #naming random color variables
    rand_red = random.random()
    rand_blue = random.random()
    rand_green = random.random()
    rand_color = (rand_red, rand_green, rand_blue)

    turtle.tracer(False)

    john.begin_fill()
    #draws rectangular playing card with random colors 50% of the time
    if random.random() < 0.5:
        draw_rectangle(x, y, width * scale_shape, height * scale_shape, True, "black", rand_color)
    else:
        draw_rectangle(x, y, width * scale_shape, height * scale_shape, fill, cardEdge, cardColor)
    john.end_fill()
    
    #scale needed for 6 hearts to fit within boundaries of heart
    scale = .05

    #draws "accute" angle bottom of heart
    straight_angled_bottom = 111.65

    #distance for `john` to move forward within loop that draws curved 
    #ears of heart
    distance = 1

    #moves hearts to column in center of card
    #calculated by --> `width` // 2 == 15, but in lower left quadrant so
    #negative
    heart_pos_x = -15

    #moves heart2 to second row in column given by `heart_pos_x`
    #calculated by --> - (`height` // 2) - 1 = -25
    heart2_pos_y = -25

    #moves heart1 to first row in column given by `heart_pos_x`
    #calculated by --> 0 - 11
    heart1_pos_y = -11

    #moves heart3 to third row in column given by `heart_pos_x`
    #calculated by --> -`height` + 8
    heart3_pos_y = -40

    #draws three hearts within card
    draw_heart((x + heart_pos_x * scale_shape), (y + heart1_pos_y * scale_shape), (straight_angled_bottom * scale) * scale_shape, (distance * scale) * scale_shape)
    draw_heart((x + heart_pos_x * scale_shape), (y + heart2_pos_y * scale_shape), (straight_angled_bottom * scale) * scale_shape, (distance * scale) * scale_shape)
    draw_heart((x + heart_pos_x * scale_shape), (y + heart3_pos_y * scale_shape), (straight_angled_bottom * scale) * scale_shape, (distance * scale) * scale_shape)

    john.hideturtle()
    turtle.tracer(True)



def draw_diamond(x, y, side_length, edgeColor = "red", fillColor = "red", penWidth = "1"):

    
    '''Function that draws a diamond from two triangles. 
    This is an extra compound shape.'''
    

    #changes pen color and color to fill diamond
    john.pencolor(edgeColor)
    john.fillcolor(fillColor)

    turtle.tracer(False)

    #sets heading of `john` back to east so that turning angles between
    #each drawn triangle are correct for drawing the diamond
    john.setheading(0)

    #set variable for angle needed to turn for drawing bottom triangle
    bottomtriangle = 60

    #naming random color variables
    rand_red = random.random()
    rand_blue = random.random()
    rand_green = random.random()
    rand_color = (rand_red, rand_green, rand_blue)

    #draws diamond with red as border and fill color
    draw_triangle2(x, y, side_length, edgeColor, fillColor, penWidth)
    john.left(bottomtriangle)
    draw_triangle2(x, y, side_length, edgeColor, fillColor, penWidth)
    john.end_fill()

    john.hideturtle()
    turtle.tracer(True)


def draw_diamond_card(x, y, scale, fill = False, cardEdge = "black", cardColor = "white"):

    
    '''Function that draws a six of diamonds card with randomly colored 
    diamonds and randomly colored edge of cards. 
    This is my second compound shape.'''

    #sets x_position of diamonds relative to placement of top right 
    #corner of rectangle
    #calculated by - ((width - (1/3) * width) + (side_length / 2)) 
    first_column = -22
    second_column = -12
    
    #sets y_position of diamonds in middle row relative to placement of
    #top right corner of rectangle
    #calculated by -(height / 2)
    second_row = -24

    #sets y_position of diamonds in first and third row relative to 
    #height of the rectangle
    #calculated by -((height - (1/4) * height) - (side_length / 2))
    first_row = -10
    third_row = -38
    
    #sets width and height of playing card, randomly chosen for ideal 
    #size in relation to board scaled to two times its size
    width = 30
    height = 48

    #sets randomly given side length for triangles that make up diamond
    #in order to figure out fixed scale to fit diamonds in blank playing 
    #card before scaling the whole playing card
    side_length = 4

    #naming random color variables
    rand_red = random.random()
    rand_blue = random.random()
    rand_green = random.random()
    rand_color = (rand_red, rand_green, rand_blue)

    turtle.tracer(False)

    john.begin_fill()
    #draws rectangular playing card with random fill colors 50% of the time
    if random.random() < 0.5:
        draw_rectangle(x, y, width * scale, height * scale, True, "black", rand_color)
    else:
        draw_rectangle(x, y, width * scale, height * scale, fill, cardEdge, cardColor)
    john.end_fill()

    #draw_rectangle(x, y, width * scale, height * scale, fill, cardEdge, cardColor)

    #draws six diamonds of random color within the border of the card
    draw_diamond((first_column * scale + x), (first_row * scale + y) , side_length * scale)
    draw_diamond((first_column * scale + x), (second_row * scale + y), side_length * scale)
    draw_diamond((first_column  * scale + x), (third_row * scale + y), side_length * scale)
    draw_diamond((second_column * scale + x), (first_row * scale + y), side_length * scale)
    draw_diamond((second_column * scale + x), (second_row * scale + y), side_length * scale)
    draw_diamond((second_column * scale + x), (third_row * scale + y), side_length * scale)

    john.hideturtle()
    turtle.tracer(True)


def draw_board(x_shape, y_shape, scale, edgeColor = "green", fillColor = "green", fill = True):

    '''draws a playing board/table. this is an extra compound shape.'''

    turtle.tracer(False)
    
    #position values placing table's center at (0,0)
    x_midsection = 250
    y_midsection = 75

    #desired size of table
    width = 500
    height = 150

    #draws rectangle for main mid-section of the table
    draw_rectangle((x_midsection + x_shape) * scale, (y_midsection + y_shape) * scale, width * scale, height * scale, fill, edgeColor, fillColor)

    #for left half-circle edge of table, negative of table's x position
    #y position is the same
    #for right edge of table, same x position but negative of table's y
    #position
    #radius of circles is half the height of the table, so equal to
    #y_midsection
    x_leftedge = -250
    y_rightedge = -75
    sidecircle_radius = height // 2

    #make circle a half circle
    extent = 180

    #make left half circle in right position and direction
    tiltleft = 180
    
    #draws half-circle starting at top left corner of rectangle
    draw_circle((x_leftedge + x_shape) * scale, (y_midsection + y_shape) * scale, sidecircle_radius * scale, extent, edgeColor, fillColor, tiltleft) 

    #draws half-circle starting at bottom right corner of rectangle
    draw_circle((x_midsection + x_shape) * scale, (y_rightedge + y_shape) * scale, sidecircle_radius * scale, extent, edgeColor, fillColor)

    john.hideturtle()
    turtle.tracer(True)


def draw_person(x_position, y_position, scale):
    '''function that draws a person'''

    #draws person's head
    draw_circle(x_position - (30 * scale), y_position + (19 * scale), 30 * scale, 360, "beige", "beige")

    #draws person's neck
    draw_rectangle(x_position - (20 * scale), y_position + (20 * scale), 20 * scale, 30 * scale, True, "beige", "beige")

    #draws person's torso
    draw_rectangle(x_position, y_position, 60 * scale, 100 * scale, True, "beige", "beige")

    #draws a person's arm
    draw_rectangle(x_position, y_position, 100 * scale, 20 * scale, True, "beige", "beige")
    draw_rectangle(x_position + (40 * scale), y_position, 100 * scale, 20 * scale, True, "beige", "beige")

    #draws persons legs
    draw_rectangle(x_position, y_position - (100 * scale), 20 * scale, 70 * scale, True, "beige", "beige")
    draw_rectangle(x_position - (40 * scale), y_position - (100 * scale), 20 * scale, 70 * scale, True, "beige", "beige")
    

def gaming2(x_position, y_position, scale):

    '''function that draws a poker game scene'''

    #green rectangle with scalable position, width, and height
    draw_rectangle(x_position, y_position, 100 * scale, 50 * scale, True, "green", "green")

    #green half circle with scalable position and radius, for curved 
    # edges of table
    draw_circle(x_position, y_position - (50 * scale), 25 * scale, 180, "green", "green")
    draw_circle(x_position - (100 * scale), y_position, 25 * scale, 180, "green", "green", 180)

    #three center rectangles (community cards) with scalable position, 
    # width and height
    draw_rectangle(x_position - (75 * scale), y_position - (15 * scale), 10 * scale, 16.5 * scale, True)
    draw_rectangle(x_position - (60 * scale), y_position - (15 * scale), 10 * scale, 16.5 * scale, True)
    draw_rectangle(x_position - (45 * scale), y_position - (15 * scale), 10 * scale, 16.5 * scale, True)

    #one diamond and one heart center card with scalable position, width 
    # and height
    draw_diamond_card(x_position - (30 * scale), y_position - (15 * scale), .35 * scale, True)
    draw_heart_card(x_position - (15 * scale), y_position - (15 * scale), .35 * scale, True)

    #two players' cards with scalable position, width, and height
    draw_rectangle(x_position - (105 * scale), y_position - (20 * scale), 16.5 * scale, 10 * scale, True)
    draw_rectangle(x_position + (20 * scale), y_position - (20 * scale), 16.5 * scale, 10 * scale, True)

    #four stacks of poker chip circles with different colors for left 
    #player
    draw_circle(x_position - (100 * scale), y_position - (15 * scale), 3 * scale, 360, "green", "white")
    draw_circle(x_position - (100 * scale), y_position - (23 * scale), 3 * scale, 360, "green", "blue")
    draw_circle(x_position - (100 * scale), y_position - (31 * scale), 3 * scale, 360, "green", "gray")
    draw_circle(x_position - (100 * scale), y_position - (39 * scale), 3 * scale, 360, "green", "orange")

    #four stacks of poker chip circles with different colors for right 
    #player
    draw_circle(x_position - (1 * scale), y_position - (15 * scale), 3 * scale, 360, "green", "white")
    draw_circle(x_position - (1 * scale), y_position - (23 * scale), 3 * scale, 360, "green", "blue")
    draw_circle(x_position - (1 * scale), y_position - (31 * scale), 3 * scale, 360, "green", "gray")
    draw_circle(x_position - (1 * scale), y_position - (39 * scale), 3 * scale, 360, "green", "orange")


if __name__== '__main__':

    #turtle.tracer(False)

    #draw_rectangle(0, 0, 100, 50)

    #testing `mondrian` function
    #mondrian(0, 0, .1)
    #mondrian(0, 500, 1)
    #mondrian(500, 0, 1)
    #mondrian(-200, -200, .3)

    #testing `draw_triangle1` function
    #draw_triangle1(50)
    #draw_triangle1(50, "black")
    #draw_triangle1(50, "black", "red")
    #draw_triangle1(50, "black", "red", 5)

    #testing `draw_triangle2` function
    #draw_triangle2(0, 0, 10)
    #draw_triangle2(100, 0, 50)
    #draw_triangle2(0, 100, 50)
    #draw_triangle2(-200, 40, 50, "black")
    #draw_triangle2(-200, 40, 50, "black", "turquoise")
    #draw_triangle2(-200, 40, 50, "black", "turquoise", 3)

    #testing `draw_circle` function
    #draw_circle(0, 0, 50)
    #draw_circle(100, 0, 50
    #draw_circle(0, 100, 50
    #draw_circle(0, 0, 50, 180)
    #draw_circle(0, 0, 50, 180, 30)
    #draw_circle(200, -50, 50, 180, 30, "black", "yellow", 5)

    #testing `draw_heart` function
    #turtle.tracer(False)
    #draw_heart(0, 0)
    #draw_heart(100, 0)
    #draw_heart(0, 100)
    #draw_heart(-370, 89, "black", "blue")
    #turtle.tracer(True)

    #testing `draw_heart_card` function
    #draw_heart_card(0, 0, 1)
    #draw_heart_card(0, 0, .5)
    #draw_heart_card(100, 0, 1)
    #draw_heart_card(0, 100, 1)
    #draw_heart_card(-100, -200, .5)
    #draw_heart_card(20, -10, 2)
    #draw_heart_card(0, 0, 1, True, "black")
    #draw_heart_card(0, 0, 2, False, "black")
    #draw_heart_card(300, 400, .5, True, "red", "gold")
    #draw_heart_card(300, 400, 1, False, "red", "gold")

    #testing `draw_diamond` function
    #draw_diamond(0, 0, 50)
    #draw_diamond(100, 0, 50)
    #draw_diamond(0, 100, 50)
    #draw_diamond(300, 300, 50, "brown", "gold", 3)

    #testing `draw_diamond_card` function
    #draw_diamond_card(0, 0, 1)
    #draw_diamond_card(100, 0, 1)
    #draw_diamond_card(0, 100, 1)
    #draw_diamond_card(0, 0, .5)
    #draw_diamond_card(-500, 200, .5, "blue", True, "black")
    #draw_diamond_card(-200, 100, 2, "blue", False, "black")

    #testing board
    #draw_board(0, 0, 1)
    #draw_board(0, 0, .5)
    #draw_board(100, 0, 1)
    #draw_board(0, -100, .5)
    #draw_board(-500, 200, .5, "red", "gold")

    #testing gaming2
    gaming2(0, 0, 1)
    gaming2(400, 400, 4)
    gaming2(-300, -200, 2)

    john.hideturtle()
    turtle.hideturtle()

    turtle.exitonclick()