
'''

better_shapelib.py
Adrian Gellert
CS151 C with Al Madi
2nd Semester
Date created: March 11, 2021
Date last modified: March 17, 2021

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
        john.left(120)
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


def draw_heart(x, y, straight_angled_bottom = 111.65, distance = 1, edgeColor = "red", fillColor = "red", penWidth = "1"):

    '''
    Function to draw a heart shape at any position with given 
    `edgeColor` and `fillColor`. 
    This is an extra, simple shape.
    '''

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


def draw_heart_card(x, y, scale_shape, fill = True, cardEdge = "black", cardColor = "white"):

    '''
    Function that draws a three of hearts card with randomly colored hearts and
    randomly colored edges of cards.
    This is my first compound shape.
    '''

    #base of rectangle, randomly chosen to position hearts within
    width = 30

    #height of rectangle, randomly chosen to position hearts within
    height = 48


    rand_red = random.random()
    rand_blue = random.random()
    rand_green = random.random()
    rand_color = (rand_red, rand_green, rand_blue)

    if random.random() <= 0.5:
        draw_rectangle(x, y, width * scale_shape, height * scale_shape, True, "black", rand_color)
    else:
        draw_rectangle(x, y, width * scale_shape, height * scale_shape, False, "black", "black")

    #draws blank playing card with random border color
    draw_rectangle(x, y, width * scale_shape, height * scale_shape, fill, cardEdge, cardColor)
    
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
    turtle.tracer(False)
    draw_heart((x + heart_pos_x * scale_shape), (y + heart1_pos_y * scale_shape), (straight_angled_bottom * scale) * scale_shape, (distance * scale) * scale_shape)
    draw_heart((x + heart_pos_x * scale_shape), (y + heart2_pos_y * scale_shape), (straight_angled_bottom * scale) * scale_shape, (distance * scale) * scale_shape)
    draw_heart((x + heart_pos_x * scale_shape), (y + heart3_pos_y * scale_shape), (straight_angled_bottom * scale) * scale_shape, (distance * scale) * scale_shape)

    john.hideturtle()
    turtle.tracer(True)



def draw_diamond(x, y, side_length, edgeColor = "red", fillColor = "red", penWidth = "1"):

    
    '''Function that draws a diamond from two triangles. 
    This is my second compound shape.'''
    

    #changes pen color and color to fill diamond
    john.pencolor(edgeColor)
    john.fillcolor(fillColor)

    #sets heading of `john` back to east so that turning angles between
    #each drawn triangle are correct for drawing the diamond
    john.setheading(0)

    #set variable for angle needed to turn for drawing bottom triangle
    bottomtriangle = 60

    #draws diamond with red as border and fill color
    john.begin_fill()
    draw_triangle2(x, y, side_length, edgeColor, fillColor, penWidth)
    john.right(bottomtriangle)
    draw_triangle2(x, y, side_length, edgeColor, fillColor, penWidth)
    john.end_fill()

    john.hideturtle()


def draw_diamond_card(x, y, scale, edgeColor = "black", fill = True, fillColor = "white"):

    
    '''Function that draws a six of diamonds card with randomly colored 
    diamonds and randomly colored edge of cards. 
    This is an extra compound shape.'''
    

    #setting values to variables to reduce magic numbers for drawing a
    #six of diamonds card 

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

    #turtle.tracer(10)

    #draws blank, white, playing card with random border color
    draw_rectangle(x, y, width * scale, height * scale, fill, edgeColor, fillColor)

    #draws six diamonds of random color within the border of the card
    turtle.tracer(False)
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


def gaming1(x, y, scale_scene, edgeColor = "green", y_community = 0, extent = 360):

    '''function that draws a poker game scenario'''

    #ideal size of playing board
    scale_board = 2 

    #draws playing board
    draw_board(x / 2 * scale_scene, y / 2 * scale_scene, scale_board * scale_scene)

    #dimensions of community cards (cards in center)
    width_community = 30                                                 
    height_community = 48
    scale = 1

    #x coordinates of community cards (`x3_community` relative to center of board, 
    #rest of cards relative to `x3_community`)
    x1_community = -100
    x2_community = -50
    x3_community = 0
    x4_community = 50
    x5_community = 100

    #draws five cards community cards (two cards are 
    #turned over and have shapes)
    draw_rectangle((x1_community + x) * scale_scene, (y_community + y) * scale_scene, (width_community * scale) * scale_scene, (height_community * scale) * scale_scene)
    draw_rectangle((x2_community + x) * scale_scene, (y_community + y) * scale_scene, (width_community * scale) * scale_scene, (height_community * scale) * scale_scene)
    draw_rectangle((x3_community + x) * scale_scene, (y_community +y) * scale_scene, (width_community * scale) * scale_scene, (height_community * scale) * scale_scene)

    #ideal size of card relative to board
    scale_card = 1

    #two turned over cards (flops)
    draw_diamond_card((x4_community + x) * scale_scene, (y_community + y) * scale_scene, scale_card * scale_scene)
    draw_heart_card((x5_community + x) * scale_scene, (y_community + y) * scale_scene, scale_card * scale_scene)

    #dimensions of hole cards (width and height of community swapped)
    #hole cards are cards for each player
    width_holes = 48
    height_holes = 30

    #x and y positions of hole cards (relative to center of semicircle 
    #edges of board)
    x1_hole = -537.5
    y1_hole = 37.5
    x2_hole = 561.5
    y2_hole = -37.5

    #draws hole cards (stack containing two cards)
    draw_rectangle((x1_hole + x) * scale_scene, (y1_hole + y) * scale_scene, width_holes * scale_card * scale_scene, height_holes * scale_card * scale_scene)
    draw_rectangle((x2_hole + x) * scale_scene, (y2_hole + y) * scale_scene, width_holes * scale_card * scale_scene, height_holes * scale_card * scale_scene)

    #desired radius of chips in relation to cards (height_holes / 2)
    radius = 5

    #x coordinate of chip stacks for player 1 
    x1_chip = -537.5

    #y coordinates of four separate stacks for player 1
    y1_stack1 = -42.5
    y1_stack2 = -62.5
    y1_stack3 = -82.5
    y1_stack4 = -102.5

    #x coordinate of chip stacks for player 2
    x2_chip = 500

    #y coordinates of four separate stacks for player 2
    y2_stack1 = 12.5
    y2_stack2 = -12.5
    y2_stack3 = -32.5
    y2_stack4 = -52.5

    #fill colors for each stack of chips
    fillColor1 = "white"
    fillColor2 = "blue"
    fillColor3 = "gray"
    fillColor4 = "orange"

    #draws poker chips for each players (stack of four different colors)
    draw_circle((x1_chip + x) * scale_scene, (y1_stack1 + y) * scale_scene, radius * scale_scene, extent, edgeColor, fillColor1)
    draw_circle((x1_chip + x) * scale_scene, (y1_stack2 + y) * scale_scene, radius * scale_scene, extent, edgeColor, fillColor2)
    draw_circle((x1_chip + x) * scale_scene, (y1_stack3 + y) * scale_scene, radius * scale_scene, extent, edgeColor, fillColor3)
    draw_circle((x1_chip + x) * scale_scene, (y1_stack4 + y) * scale_scene, radius * scale_scene, extent, edgeColor, fillColor4)
    draw_circle((x2_chip + x) * scale_scene, (y2_stack1 + y) * scale_scene, radius * scale_scene, extent, edgeColor, fillColor1)
    draw_circle((x2_chip + x) * scale_scene, (y2_stack2 + y) * scale_scene, radius * scale_scene, extent, edgeColor, fillColor2)
    draw_circle((x2_chip + x) * scale_scene, (y2_stack3 + y) * scale_scene, radius * scale_scene, extent, edgeColor, fillColor3)
    draw_circle((x2_chip + x) * scale_scene, (y2_stack4 + y) * scale_scene, radius * scale_scene, extent, edgeColor, fillColor4)
    

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
    #draw_board(0, -100, 1)

    ###############################################right rectangle border coverred by circle fill but not left
    #draw_board(-500, 200, .5, "red", "gold")


    #testing gaming scene
    #gaming1(0, 0, 1)
    #gaming1(100, 0, 1)
    gaming1(0, 100, 1)
    #gaming1(0, 0, .5)
    #gaming1(100, -50, .5, "black")

    ###############################################turtle in center won't go away
    john.hideturtle()
    turtle.hideturtle()

    turtle.exitonclick()