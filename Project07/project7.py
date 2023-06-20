
'''
project7.py
Adrian Gellert
CS151 C with Al Madi
2nd Semester
Date created: April 7, 2021
Date last modified: April 23, 2021

This file uses python's turtle library, an imported shape library, and 
Google's imported speech recognition module to draw different shapes 
and move across turtle's window. 
'''

import turtle 
import speech_to_text as ST
import better_shapelib as bsl

def main():
    assistant = turtle.Turtle()

    while True:
        
        # listening for speech
        input("press enter to talk")
        speech = ST.text_from_speech()

        # up command
        if "up" in speech:
            assistant.up()

        # down command
        if "down" in speech:
            assistant.down()
        
        
        # goto if command
        if "go to" in speech:

            tokens = speech.split(' ')

            # finding x and y coordinates or asking for them
            # and changing coordinates to integers from strings
            if "and" in tokens:
                x_cor_index = tokens.index("and") - 1
                x_cor = int(tokens[x_cor_index])
                y_cor_index = tokens.index("and") + 1
                y_cor = int(tokens[y_cor_index])
            elif "+" in tokens:
                x_cor_index = tokens.index("+") - 1
                x_cor = int(tokens[x_cor_index])
                y_cor_index = tokens.index("+") + 1
                y_cor = int(tokens[y_cor_index])
            else:
                x_cor_index = input("What is the x-coordinate? ")
                x_cor = int(x_cor_index)
                y_cor_index = input("What is the y-coordinate? ")
                y_cor = int(y_cor_index)

            # moving turtle to position without drawing on window
            assistant.up()
            assistant.goto(x_cor, y_cor)
            assistant.down()
        
        # moving forward/backward if statement
        if "move" in speech or "go" in speech:
            
            # forward command
            if "forward" in speech or "forwards" in speech: 

                tokens = speech.split(' ')

                # checking for number of units to move turtle or 
                # asking for user to input number of units
                if "by" in tokens: 
                    units_index = tokens.index("by") + 1
                    units = int(tokens[units_index])
                elif "forward" in tokens:
                    length = len(tokens)
                    if length > 2:
                        units_index = tokens.index("forward") + 1
                        units = int(tokens[units_index])
                    else:
                        units_index = input("Please input a distance:")
                        units = int(units_index)
                elif "forwards" in tokens:
                    length = len(tokens)
                    if length > 2:
                        units_index = tokens.index("forwards") + 1
                        units = int(tokens[units_index])
                    else:
                        units_index = input("Please input a distance:")
                        units = int(units_index)

                assistant.forward(units)
            
            # backward command
            elif "backward" in speech or "backwards" in speech:

                tokens = speech.split(' ')

                # checking for number of units to move turtle or 
                # asking for user to input number of units
                if "by" in tokens: 
                    units_index = tokens.index("by") + 1
                    units = int(tokens[units_index])
                elif "backward" in tokens:
                    length = len(tokens)
                    if length > 2:
                        units_index = tokens.index("backward") + 1
                        units = int(tokens[units_index])
                    else:
                        units_index = input("Please input a distance:")
                        units = int(units_index)
                elif "backwards" in tokens:
                    length = len(tokens)
                    if length > 2:
                        units_index = tokens.index("backwards") + 1
                        units = int(tokens[units_index])
                    else:
                        units_index = input("Please input a distance:")
                        units = int(units_index)

                assistant.backward(units)

        #set heading cardinal directions
        if "heading" in speech or "Heading" in speech or "head" in speech or "Head" in speech:

            tokens = speech.split(' ')

            if "north" in tokens or "North" in tokens:
                assistant.setheading(90)
            elif "south" in tokens or "South" in tokens:
                assistant.setheading(270)
            elif "west" in tokens or "West" in tokens:
                assistant.setheading(180)
            elif "east" in tokens or "East" in tokens:
                assistant.setheading(0)
        elif "turn south" in speech or "turn South" in speech:
                assistant.setheading(270)
        elif "turn north" in speech or "turn North" in speech:
            assistant.setheading(90)
        elif "turn west" in speech or "turn West" in speech:
            assistant.setheading(180)
        elif "turn east" in speech or "turn East" in speech:
            assistant.setheading(0)

        # other rotation commands
        elif "turn" in speech or "Turn" in speech:

            tokens = speech.split(' ')
            
            # checking for number of degrees to move by
            if len(tokens) > 2:
                if "degrees" in tokens:
                    degrees_index = tokens.index("degrees") - 1
                    #degrees = int(tokens[degrees_index])
                elif "degree" in tokens:
                    degrees_index = tokens.index("degree") - 1
                    #degrees = int(tokens[degrees_index])
                elif "by" in tokens:
                    degrees_index = tokens.index("by") + 1
                    #degrees = int(tokens[degrees_index])

            degrees = int(degrees_index)

            # checking which direction 
            if "right" in tokens:
                assistant.right(degrees)
            elif "left" in tokens:
                assistant.left(degrees)
        

        # draw circle, square, triangle, diamond, heart, or mondrian
        # command
        if "make" in speech or "draw" in speech or "create" in speech or "Make" in speech or "Draw" in speech or "Create" in speech:
            
            #list of valid colors
            print("List of colors: ", "LightPink,", "Pink,", "Crimson,", 
                  "LavenderBlush,", "PaleVioletRed,", "HotPink,", 
                  "DeepPink,", "MediumVioletRed,", "Orchid,", 
                  "Thistle,", "Plum,", "Violet,", "Magenta,", 
                  "Fuchsia,", "DarkMagenta,", "Purple,", 
                  "MediumOrchid,", "DarkViolet,", "DarkOrchid,", 
                  "Indigo,", "BlueViolet,", "MediumPurple,", 
                  "MediumSlateBlue,", "SlateBlue,", "DarkSlateBlue,", 
                  "Lavender,", "GhostWhite,", "Blue,", "MediumBlue,", 
                  "MidnightBlue,", "DarkBlue,", "Navy,", "RoyalBlue,", 
                  "CornflowerBlue,", "LightSteelBlue,", 
                  "LightSlateGray,", "SlateGray,", "DodgerBlue,", 
                  "AliceBlue,", "SteelBlue,", "LightSkyBlue,", 
                  "SkyBlue,", "DeepSkyBlue,", "LightBlue,", 
                  "PowderBlue,", "CadetBlue,", "Azure,", "LightCyan,",
                  "PaleTurquoise,", "Cyan,", "Aqua,", "DarkTurquoise,",
                  "DarkSlateGray,", "DarkCyan,", "Teal,", 
                  "MediumTurquoise,", "LightSeaGreen,", "Turquoise,", 
                  "Aquamarine,", "MediumAquamarine,", 
                  "MediumSpringGreen,", "MintCream,", "SpringGreen,", 
                  "MediumSeaGreen,", "SeaGreen,", "Honeydew,", 
                  "LightGreen,", "PaleGreen,", "DarkSeaGreen,", 
                  "LimeGreen,", "Lime,", "ForestGreen,", "Green,", 
                  "DarkGreen,", "Chartreuse,", "LawnGreen,", 
                  "GreenYellow,", "DarkOliveGreen,", "YellowGreen,", 
                  "OliveDrab,", "Beige,", "LightGoldenrodYellow,", 
                  "Ivory,", "LightYellow,", "Yellow,", "Olive,", 
                  "DarkKhaki,", "LemonChiffon,", "PaleGoldenrod,", 
                  "Khaki,", "Gold,", "Cornsilk,", "Goldenrod,", 
                  "DarkGoldenrod,", "FloralWhite,", "OldLace,", 
                  "Wheat,", "Moccasin,", "Orange,", "PapayaWhip,", 
                  "BlanchedAlmond,", "NavajoWhite,", "AntiqueWhite,", 
                  "Tan,", "BurlyWood,", "Bisque,", "DarkOrange,", 
                  "Linen,", "Peru,", "PeachPuff,", "SandyBrown,", 
                  "Chocolate,", "SaddleBrown,", "Seashell,", "Sienna,", 
                  "LightSalmon,", "Coral,", "OrangeRed,", "DarkSalmon,", 
                  "Tomato,", "MistyRose,", "Salmon,", "Snow,", 
                  "LightCoral,", "RosyBrown,", "IndianRed,", "Red,", 
                  "Brown,", "FireBrick,", "DarkRed,", "Maroon,", 
                  "White,", "WhiteSmoke,", "Gainsboro,", "LightGrey,", 
                  "Silver,", "DarkGray,", "Gray,", "DimGray,", "Black")
                  
            tokens = speech.split(' ')

            current_x = assistant.xcor()
            current_y = assistant.ycor()

            # drawing square/rectangle
            if "square" in tokens:
                
                # asking for width and height and changing to integer values
                width_string = input("Please type a width: ")
                height_string = input("Please type a height: ")
                width = int(width_string)
                height = int(height_string)

                # asking for edge and fill color
                edgeColor = input("Please input a color from the list (edge): ")
                fillColor = input("Please input a color from the list (fill): ")

                # using better_shapelib.py rectangle function to draw 
                bsl.draw_rectangle(current_x, current_y, height, width, True, edgeColor, fillColor, 2)
            elif "rectangle" in tokens:
                
                # asking for width and height and changing to integer values
                width_string = input("Please type a width: ")
                height_string = input("Please type a height: ")
                width = int(width_string)
                height = int(height_string)

                # asking for edge and fill color
                edgeColor = input("Please input a color from the list (edge): ")
                fillColor = input("Please input a color from the list (fill): ")

                # using better_shapelib.py rectangle function to draw 
                bsl.draw_rectangle(current_x, current_y, height, width, True, edgeColor, fillColor, 2)
            
            # drawing mondrian with given number of squares/rectangles
            if "rectangles" in tokens:

                # looking for number of rectangles in speech and 
                # changing string to integer
                num_rectangles = tokens.index("rectangles") - 1
                rectangles = int(tokens[num_rectangles])

                # asking for size (scaling)
                size_string = input("How large (scaling)? ")
                size = float(size_string)

                # using better_shapelib.py mondrian function to draw
                bsl.mondrian(current_x, current_y, size, rectangles)
            elif "squares" in tokens:

                # looking for number of squares in speech and 
                # changing string to integer
                num_squares = tokens.index("squares") - 1
                squares = int(tokens[num_squares])

                # asking for size (scaling)
                size_string = input("How large (scaling)? ")
                size = float(size_string)

                # using better_shapelib.py mondrian function to draw
                bsl.mondrian(current_x, current_y, size, squares)

            # drawing mondrian with 100 squares/rectangles
            elif "mondrian" in tokens or "Mondrian" in tokens:

                # asking for size (scaling)
                size_string = input("How large (scaling? ")
                size = float(size_string)

                # using better_shapelib.py mondrian function to draw
                bsl.mondrian(current_x, current_y, size)

            # drawing a circle
            if "circle" in tokens:
                
                # looking for specific degrees of circle with words 
                # other than a number
                # in addition, asking for a radius, and edge/fill color
                if (tokens.index("circle") - 1) == "half":

                    # asking for radius and changing to integer
                    radius_string = input("Please input a radius:")
                    radius = int(radius_string)

                    # asking for edge and fill color
                    edgeColor = input("Please input a color from the list (edge): ")
                    fillColor = input("Please input a color from the list (fill): ")

                    # using better_shapelib.py circle function to draw
                    bsl.draw_circle(current_x, current_y, radius, 180, edgeColor, fillColor, 3)
                elif (tokens.index("circle") - 1) == "quarter":

                    # asking for radius and changing to integer
                    radius_string = input("Please input a radius:")
                    radius = int(radius_string)

                    # asking for edge/fill color
                    edgeColor = input("Please input a color from the list (edge): ")
                    fillColor = input("Please input a color from the list (fill): ")

                    # using better_shapelib.py circle function to draw
                    bsl.draw_circle(current_x, current_y, radius, 90, edgeColor, fillColor, 3)

                # else asking for a radius
                else:

                    # asking for radius and changing to integer
                    radius_string = input("Please input a radius:")
                    radius = int(radius_string)

                    # asking for edge/fill color
                    edgeColor = input("Please input a color from the list (edge): ")
                    fillColor = input("Please input a color from the list (fill): ")

                    # using better_shapelib.py circle function to draw
                    bsl.draw_circle(current_x, current_y, radius, 360, edgeColor, fillColor, 3)

            # drawing a part of circle with user inputted extent, radius, and edge/fill color
            elif "curved" in tokens:

                # asking for radius and changing to integer
                radius_string = input("Please input a radius:")
                radius = int(radius_string)

                # asking for edge and fill color
                edgeColor = input("Please input a color from the list (edge): ")
                fillColor = input("Please input a color from the list (fill): ")

                # asking for extent
                extent_string = input("What number of degrees of a full circle? ")
                extent = int(extent_string)

                # using better_shapelib.py circle function to draw
                bsl.draw_circle(current_x, current_y, radius, extent, edgeColor, fillColor)
            elif "round" in tokens:

                # asking for radius and changing to integer
                radius_string = input("Please input a radius:")
                radius = int(radius_string)

                # asking for edge and fill color
                edgeColor = input("Please input a color from the list (edge): ")
                fillColor = input("Please input a color from the list (fill): ")

                # asking for extent
                extent_string = input("What number of degrees of a full circle? ")
                extent = int(extent_string)

                # using better_shapelib.py circle function to draw
                bsl.draw_circle(current_x, current_y, radius, extent, edgeColor, fillColor)

            # drawing a triangle
            if "triangle" in tokens:

                # asking for side length and changing to integer
                side_length_string = input("Please input side length: ")
                side_length = int(side_length_string)

                # asking for edge and fill color
                edgeColor = input("Please input a color from the list (edge): ")
                fillColor = input("Please input a color from the list (fill): ")

                # using better_shapelib.py circle function to draw
                bsl.draw_triangle2(current_x, current_y, side_length, edgeColor, fillColor)

            # drawing a person
            if "person" in tokens:

                # asking for size (scaling)
                size_string = input("How large (scaling)? ")
                size = float(size_string)

                # using better_shapelib.py person function to draw
                bsl.draw_person(current_x, current_y, size)


if __name__ == "__main__":
    turtle.hideturtle()
    main()
    
