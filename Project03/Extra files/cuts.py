'''
def draw_diamond_card(x, y, width, height, edgeColor = "red", fillColor = "red", penWidth = "red", scale, scale1, scale2):

    #draws a six of diamonds card

    #creating a variable for random color
    #rand_red = random.random()
    #rand_green = random.random()
    #rand_blue = random.random()
    #rand_color = (rand_red, rand_green, rand_blue)

    #draws card with random `edgeColor` and white `fillColor`
    draw_rectangle(x, y, width, height, ................................................................)

    #draws six diamonds within the border of the card
    draw_diamond((-75+x)*scale2, (-100+y)*scale2, scale1*scale2)
    draw_diamond((-75+x)*scale2, (-60+y)*scale2, scale1*scale2)
    draw_diamond((-75+x)*scale2, (-20+y)*scale2, scale1*scale2)
    draw_diamond((-35+x)*scale2, (-100+y)*scale2, scale1*scale2)
    draw_diamond((-35+x)*scale2, (-60+y)*scale2, scale1*scale2)
    draw_diamond((-35+x)*scale2, (-20+y)*scale2, scale1*scale2)

    john.hideturtle()

def draw_heart_card(x, y, width, height, edgeColor = "white", fillColor = "white", scale, scale1, scale2):

    #draws a three of hearts card

    #draws card with certain `edgeColor`and `fillColor`
    draw_playingcard((0+x)*scale2, (0+y)*scale2, width, height, scale*scale2, edgeColor, "white")

    #draws three hearts within the border of the card
    draw_heart((-50+x)*scale2, (-110+y)*scale2, scale1*scale2)
    draw_heart((-50+x)*scale2, (-70+y)*scale2, scale1*scale2)
    draw_heart((-50+x)*scale2, (-30+y)*scale2, scale1*scale2)

    john.hideturtle()


#def gaming1(x_pos, y, scale_scene, fill = True, edgeColor = "black", fillColor = "white"):

    #Function that draws a poker game scenario

    #turtle.tracer(False)

    #scale_board = 2
    #board_x = -100

    #draw playing board
    #draw_board((board_x * scale_scene + x_pos), y * scale_scene, scale_board * scale_scene)

    #setting values to variables to reduce magic numbers for drawing
    #and placing center cards
    #card1_x = -225 * scale_scene
    #card2_x = -150 * scale_scene
    #card3_x = -75 * scale_scene
    #flop1_x = -100
    #flop2_x = 200 * scale_scene
    #flop2_x = 200 
    #cardsleft_width = 100 * scale_scene
    #cardsleft_height = 120 * scale_scene
    #scale = .5 * scale_scene
    #scale = .5 
    #scale = scale_scene
 
    #draws cards in center of board/table that players use in 
    #conjunction with their cards to make a "hand" made of five cards
    #draw_rectangle((x_pos * scale_scene + card1_x), y * scale_scene, (cardsleft_width * scale) * scale_scene, (cardsleft_height * scale) * scale_scene, fill, edgeColor, fillColor)
    #draw_rectangle((x_pos * scale_scene + card2_x), y * scale_scene, (cardsleft_width * scale) * scale_scene, (cardsleft_height * scale) * scale_scene, fill, edgeColor, fillColor)
    #draw_rectangle((x_pos * scale_scene + card3_x), y * scale_scene, (cardsleft_width * scale) * scale_scene, (cardsleft_height * scale) * scale_scene, fill, edgeColor, fillColor)
    
    #draw_diamond_card((x_pos + flop2_x), y, scale, edgeColor)
    #draw_diamond_card((x_pos * scale_scene + flop2_x), y * scale_scene, scale * scale_scene, edgeColor)
    #draw_diamond_card((x_pos + flop2_x), y, scale * scale_scene, edgeColor)
    #draw_diamond_card((x_pos * scale_scene + flop2_x), y, scale, edgeColor)
    #draw_diamond_card((x_pos + flop2_x * scale_scene), y, scale, edgeColor)
    
    #modify x and y coordinates here for placement of hearts and card
    #draw_heart_card(x_pos * scale_scene, y * scale_scene, scale * scale_scene, edgeColor)
    #draw_heart_card(x_pos, y * scale_scene, scale * scale_scene, edgeColor)
    #draw_heart_card(x_pos * scale_scene, y, scale * scale_scene, edgeColor)
    #draw_heart_card(x_pos * scale_scene, y * scale_scene, scale, edgeColor)
    #draw_heart_card(x_pos * scale_scene, y * scale_scene, scale_scene, edgeColor)
    #draw_heart_card(x_pos * scale_scene, y * scale_scene, scale * scale_scene, edgeColor)
    #draw_heart_card(x_pos * scale, y * scale_scene, scale * scale_scene, edgeColor)
    #draw_heart_card(x_pos * scale_scene, y * scale, scale * scale_scene, edgeColor)
    #draw_heart_card(x_pos * scale, y * scale_scene, scale, edgeColor)
    #draw_heart_card(x_pos * scale, y * scale_scene, scale_scene, edgeColor)
    #draw_heart_card(x_pos * scale + flop1_x, y * scale_scene, scale, edgeColor)
    #draw_heart_card(x_pos + (flop1_x * scale), y * scale_scene, scale, edgeColor)

    #setting values to variables to reduce magic numbers for drawing
    #and placing playing cards
    #leftcard_x = 350
    #rightcard_x = -550
    #playerscard_y = -175
    #playerscard_width = 30
    #playerscard_height = 50

    #draws visible card for each player (each player has two cards)
    #draw_rectangle((x_pos * scale_scene + leftcard_x), (y + playerscard_y) * scale_scene, playerscard_width * scale_scene, playerscard_height * scale_scene, fill, edgeColor, fillColor) 
    #draw_rectangle((x_pos * scale_scene + rightcard_x), (y + playerscard_y) * scale_scene, playerscard_width * scale_scene, playerscard_height * scale_scene, fill, edgeColor, fillColor)

    #setting values to variables to reduce magic numbers for drawing
    #and placing players' poker chips
    #left1_x = -580
    #left2_x = -555
    #left3_x = -530
    #left4_x = -505
    #right1_x = 275
    #right2_x = 300
    #right3_x = 325
    #right4_x = 350
    #chips_y = -155
    #chips_radius = 10

    #draws poker chips that each player has
    #draw_circle((x_pos * scale_scene + left1_x), (y + chips_y) * scale_scene, chips_radius * scale_scene, 360, 0, edgeColor, "blue")
    #draw_circle((x_pos * scale_scene + left2_x), (y + chips_y) * scale_scene, chips_radius * scale_scene, 360, 0, edgeColor, "red")
    #draw_circle((x_pos * scale_scene + left3_x), (y + chips_y) * scale_scene, chips_radius * scale_scene, 360, 0, edgeColor, "green")
    #draw_circle((x_pos * scale_scene + left4_x), (y + chips_y) * scale_scene, chips_radius * scale_scene, 360, 0, edgeColor, "black")
    #draw_circle((x_pos * scale_scene + right1_x), (y + chips_y) * scale_scene, chips_radius * scale_scene, 360, 0, edgeColor, "blue")
    #draw_circle((x_pos * scale_scene + right2_x), (y + chips_y) * scale_scene, chips_radius * scale_scene, 360, 0, edgeColor, "red")
    #draw_circle((x_pos * scale_scene + right3_x), (y + chips_y) * scale_scene, chips_radius * scale_scene, 360, 0, edgeColor, "green")
    #draw_circle((x_pos * scale_scene + right4_x), (y + chips_y) * scale_scene, chips_radius * scale_scene, 360, 0, edgeColor, "black")

    #turtle.tracer(True)

'''