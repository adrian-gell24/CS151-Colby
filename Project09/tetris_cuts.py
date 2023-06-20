blocks = [[1, 1], [1, 2], [1, 3], [1, 4]]

print(blocks[2][0])
blocks[1][0] = blocks[0][1]
blocks[2][0] = blocks[0][2]
blocks[3][0] = blocks[0][3]
print(blocks[1][0])

print(blocks[3][0])


'''
                # clearing a full row
                # loop through every row
                for i in range(len(self.grid)):
                    #check if full row has numbers other than 0 (empty)
                    if ((self.grid[i][0] == 1 
                        or self.grid[i][0] == 2
                        or self.grid[i][0] == 3
                        or self.grid[i][0] == 4
                        or self.grid[i][0] == 5
                        or self.grid[i][0] == 6
                        or self.grid[i][0] == 7)
                        and 
                        (self.grid[i][1] == 1 
                        or self.grid[i][1] == 2
                        or self.grid[i][1] == 3
                        or self.grid[i][1] == 4
                        or self.grid[i][1] == 5
                        or self.grid[i][1] == 6
                        or self.grid[i][1] == 7)
                        and 
                        (self.grid[i][2] == 1 
                        or self.grid[i][2] == 2
                        or self.grid[i][2] == 3
                        or self.grid[i][2] == 4
                        or self.grid[i][2] == 5
                        or self.grid[i][2] == 6
                        or self.grid[i][2] == 7)
                        and 
                        (self.grid[i][3] == 1 
                        or self.grid[i][3] == 2
                        or self.grid[i][3] == 3
                        or self.grid[i][3] == 4
                        or self.grid[i][3] == 5
                        or self.grid[i][3] == 6
                        or self.grid[i][3] == 7)
                        and 
                        (self.grid[i][4] == 1 
                        or self.grid[i][4] == 2
                        or self.grid[i][4] == 3
                        or self.grid[i][4] == 4
                        or self.grid[i][4] == 5
                        or self.grid[i][4] == 6
                        or self.grid[i][4] == 7)
                        and 
                        (self.grid[i][5] == 1 
                        or self.grid[i][5] == 2
                        or self.grid[i][5] == 3
                        or self.grid[i][5] == 4
                        or self.grid[i][5] == 5
                        or self.grid[i][5] == 6
                        or self.grid[i][5] == 7)
                        and 
                        (self.grid[i][6] == 1 
                        or self.grid[i][6] == 2
                        or self.grid[i][6] == 3
                        or self.grid[i][6] == 4
                        or self.grid[i][6] == 5
                        or self.grid[i][6] == 6
                        or self.grid[i][6] == 7)
                        and 
                        (self.grid[i][7] == 1 
                        or self.grid[i][7] == 2
                        or self.grid[i][7] == 3
                        or self.grid[i][7] == 4
                        or self.grid[i][7] == 5
                        or self.grid[i][7] == 6
                        or self.grid[i][7] == 7)
                        and 
                        (self.grid[i][8] == 1 
                        or self.grid[i][8] == 2
                        or self.grid[i][8] == 3
                        or self.grid[i][8] == 4
                        or self.grid[i][8] == 5
                        or self.grid[i][8] == 6
                        or self.grid[i][8] == 7)
                        and 
                        (self.grid[i][9] == 1 
                        or self.grid[i][9] == 2
                        or self.grid[i][9] == 3
                        or self.grid[i][9] == 4
                        or self.grid[i][9] == 5
                        or self.grid[i][9] == 6
                        or self.grid[i][9] == 7)):
                        
                        # switching values back to empty
                        self.grid[i][0] = 0 
                        self.grid[i][1] = 0
                        self.grid[i][2] = 0
                        self.grid[i][3] = 0
                        self.grid[i][4] = 0
                        self.grid[i][5] = 0
                        self.grid[i][6] = 0
                        self.grid[i][7] = 0
                        self.grid[i][8] = 0
                        self.grid[i][9] = 0
'''



'''
                # make sure tetrimino position is within bounds of self.grid
                if (a[0] < 0 
                    or b[0] < 0 
                    or c[0] < 0 
                    or d[0] < 0
                    or a[1] < 0
                    or b[1] < 0
                    or c[1] < 0
                    or d[1] < 0
                    or a[1] > len(self.grid[0]) - 1
                    or b[1] > len(self.grid[0]) - 1
                    or c[1] > len(self.grid[0]) - 1
                    or d[1] > len(self.grid[0]) - 1):
                    
                    return False
                
                # else if check if tetrimino has reached the bottom of the board
                # or if the tetrimino has touched another tetrimino
                elif (a[0] > len(self.grid) - 1 
                    or b[0] > len(self.grid) - 1
                    or c[0] > len(self.grid) - 1
                    or d[0] > len(self.grid) - 1
                    or self.grid[a[0]][a[1]] == 1
                    or self.grid[b[0]][b[1]] == 1
                    or self.grid[c[0]][c[1]] == 1
                    or self.grid[d[0]][d[1]] == 1
                    or self.grid[a[0]][a[1]] == 2
                    or self.grid[b[0]][b[1]] == 2
                    or self.grid[c[0]][c[1]] == 2
                    or self.grid[d[0]][d[1]] == 2
                    or self.grid[a[0]][a[1]] == 3
                    or self.grid[b[0]][b[1]] == 3
                    or self.grid[c[0]][c[1]] == 3
                    or self.grid[d[0]][d[1]] == 3
                    or self.grid[a[0]][a[1]] == 4
                    or self.grid[b[0]][b[1]] == 4
                    or self.grid[c[0]][c[1]] == 4
                    or self.grid[d[0]][d[1]] == 4
                    or self.grid[a[0]][a[1]] == 5
                    or self.grid[b[0]][b[1]] == 5
                    or self.grid[c[0]][c[1]] == 5
                    or self.grid[d[0]][d[1]] == 5
                    or self.grid[a[0]][a[1]] == 6
                    or self.grid[b[0]][b[1]] == 6
                    or self.grid[c[0]][c[1]] == 6
                    or self.grid[d[0]][d[1]] == 6
                    or self.grid[a[0]][a[1]] == 7
                    or self.grid[b[0]][b[1]] == 7
                    or self.grid[c[0]][c[1]] == 7
                    or self.grid[d[0]][d[1]] == 7):
                    
                    # change value of grid units where tetrimino reaches bottom
                    if self.tetrimino.check() == "S":
                        # change value of unit on grid
                        self.grid[a[0] - 1][a[1]] = 1
                        self.grid[b[0] - 1][b[1]] = 1
                        self.grid[c[0 - 1]][c[1]] = 1
                        self.grid[d[0] - 1][d[1]] = 1
                    elif self.tetrimino.check() == "Z":
                        # change value of unit on grid
                        self.grid[a[0] - 1][a[1]] = 2
                        self.grid[b[0] - 1][b[1]] = 2
                        self.grid[c[0] - 1][c[1]] = 2
                        self.grid[d[0] - 1][d[1]] = 2
                    elif self.tetrimino.check() == "I":
                        # change value of unit on grid
                        self.grid[a[0] - 1][a[1]] = 3
                        self.grid[b[0] - 1][b[1]] = 3
                        self.grid[c[0] - 1][c[1]] = 3
                        self.grid[d[0] - 1][d[1]] = 3
                    if self.tetrimino.check() == "J":
                        # change value of unit on grid
                        self.grid[a[0] - 1][a[1]] = 4
                        self.grid[b[0] - 1][b[1]] = 4
                        self.grid[c[0] - 1][c[1]] = 4
                        self.grid[d[0] - 1][d[1]] = 4
                    if self.tetrimino.check() == "L":
                        # change value of unit on grid
                        self.grid[a[0] - 1][a[1]] = 5
                        self.grid[b[0] - 1][b[1]] = 5
                        self.grid[c[0] - 1][c[1]] = 5
                        self.grid[d[0] - 1][d[1]] = 5
                    if self.tetrimino.check() == "O":
                        # change value of unit on grid
                        self.grid[a[0] - 1][a[1]] = 6
                        self.grid[b[0] - 1][b[1]] = 6
                        self.grid[c[0] - 1][c[1]] = 6
                        self.grid[d[0] - 1][d[1]] = 6
                    if self.tetrimino.check() == "T":
                        # change value of unit on grid
                        self.grid[a[0] - 1][a[1]] = 7
                        self.grid[b[0] - 1][b[1]] = 7
                        self.grid[c[0] - 1][c[1]] = 7
                        self.grid[d[0] - 1][d[1]] = 7
                        
                    # make new choice of tetrimino
                    self.tetrimino = O_tetrimino() #random.choice(self.list_tetriminos)()
'''



'''
        for i in range(len(self.grid)):
            #check if full row has numbers other than 0 (empty)
             if ((self.grid[i][0] == 1 
                or self.grid[i][0] == 2
                or self.grid[i][0] == 3
                or self.grid[i][0] == 4
                or self.grid[i][0] == 5
                or self.grid[i][0] == 6
                or self.grid[i][0] == 7)
                and 
                (self.grid[i][1] == 1 
                or self.grid[i][1] == 2
                or self.grid[i][1] == 3
                or self.grid[i][1] == 4
                or self.grid[i][1] == 5
                or self.grid[i][1] == 6
                or self.grid[i][1] == 7)
                and 
                (self.grid[i][2] == 1 
                or self.grid[i][2] == 2
                or self.grid[i][2] == 3
                or self.grid[i][2] == 4
                or self.grid[i][2] == 5
                or self.grid[i][2] == 6
                or self.grid[i][2] == 7)
                and 
                (self.grid[i][3] == 1 
                or self.grid[i][3] == 2
                or self.grid[i][3] == 3
                or self.grid[i][3] == 4
                or self.grid[i][3] == 5
                or self.grid[i][3] == 6
                or self.grid[i][3] == 7)
                and 
                (self.grid[i][4] == 1 
                or self.grid[i][4] == 2
                or self.grid[i][4] == 3
                or self.grid[i][4] == 4
                or self.grid[i][4] == 5
                or self.grid[i][4] == 6
                or self.grid[i][4] == 7)
                and 
                (self.grid[i][5] == 1 
                or self.grid[i][5] == 2
                or self.grid[i][5] == 3
                or self.grid[i][5] == 4
                or self.grid[i][5] == 5
                or self.grid[i][5] == 6
                or self.grid[i][5] == 7)
                and 
                (self.grid[i][6] == 1 
                or self.grid[i][6] == 2
                or self.grid[i][6] == 3
                or self.grid[i][6] == 4
                or self.grid[i][6] == 5
                or self.grid[i][6] == 6
                or self.grid[i][6] == 7)
                and 
                (self.grid[i][7] == 1 
                or self.grid[i][7] == 2
                or self.grid[i][7] == 3
                or self.grid[i][7] == 4
                or self.grid[i][7] == 5
                or self.grid[i][7] == 6
                or self.grid[i][7] == 7)
                and 
                (self.grid[i][8] == 1 
                or self.grid[i][8] == 2
                or self.grid[i][8] == 3
                or self.grid[i][8] == 4
                or self.grid[i][8] == 5
                or self.grid[i][8] == 6
                or self.grid[i][8] == 7)
                and 
                (self.grid[i][9] == 1 
                or self.grid[i][9] == 2
                or self.grid[i][9] == 3
                or self.grid[i][9] == 4
                or self.grid[i][9] == 5
                or self.grid[i][9] == 6
                or self.grid[i][9] == 7)):
                
                # clear writing
                self.turt.clear()

                # increase value of counter
                counter += 100
                
                # rewrite score
                self.turt.penup()
                self.turt.goto(-100, (turtle.window_height() / 2) - 100)
                self.turt.pendown()
                self.turt.write("Player Score: " + str(counter), font=("Verdana", 20, "normal"))
                        
                # switching values back to empty
                self.grid[i][0] = 0 
                self.grid[i][1] = 0
                self.grid[i][2] = 0
                self.grid[i][3] = 0
                self.grid[i][4] = 0
                self.grid[i][5] = 0
                self.grid[i][6] = 0
                self.grid[i][7] = 0
                self.grid[i][8] = 0
                self.grid[i][9] = 0
'''



                    # # checking whether cell in grid is empty and drawing a white square there if it is
                    # if block != [row, col]:
                        
                    #     # draw empty square in that position
                    #     self.draw_square(tile_size, "white", True)
                
                ################### below here until multi-line code commented out part
                # make sure tetrimino position is within bounds of self.grid
                # if (a[0] < 0 
                #     or b[0] < 0 
                #     or c[0] < 0 
                #     or d[0] < 0
                #     or a[1] < 0
                #     or b[1] < 0
                #     or c[1] < 0
                #     or d[1] < 0
                #     or a[1] > len(self.grid[0]) - 1
                #     or b[1] > len(self.grid[0]) - 1
                #     or c[1] > len(self.grid[0]) - 1
                #     or d[1] > len(self.grid[0]) - 1):
                    
                #     return False
                
                # else if check if tetrimino has reached the bottom of the board
                # or if the tetrimino has touched another tetrimino
                # elif (a[0] > len(self.grid) - 1 
                #     or b[0] > len(self.grid) - 1
                #     or c[0] > len(self.grid) - 1
                #     or d[0] > len(self.grid) - 1
                #     or self.grid[a[0]][a[1]] == 1
                #     or self.grid[b[0]][b[1]] == 1
                #     or self.grid[c[0]][c[1]] == 1
                #     or self.grid[d[0]][d[1]] == 1
                #     or self.grid[a[0]][a[1]] == 2
                #     or self.grid[b[0]][b[1]] == 2
                #     or self.grid[c[0]][c[1]] == 2
                #     or self.grid[d[0]][d[1]] == 2
                #     or self.grid[a[0]][a[1]] == 3
                #     or self.grid[b[0]][b[1]] == 3
                #     or self.grid[c[0]][c[1]] == 3
                #     or self.grid[d[0]][d[1]] == 3
                #     or self.grid[a[0]][a[1]] == 4
                #     or self.grid[b[0]][b[1]] == 4
                #     or self.grid[c[0]][c[1]] == 4
                #     or self.grid[d[0]][d[1]] == 4
                #     or self.grid[a[0]][a[1]] == 5
                #     or self.grid[b[0]][b[1]] == 5
                #     or self.grid[c[0]][c[1]] == 5
                #     or self.grid[d[0]][d[1]] == 5
                #     or self.grid[a[0]][a[1]] == 6
                #     or self.grid[b[0]][b[1]] == 6
                #     or self.grid[c[0]][c[1]] == 6
                #     or self.grid[d[0]][d[1]] == 6
                #     or self.grid[a[0]][a[1]] == 7
                #     or self.grid[b[0]][b[1]] == 7
                #     or self.grid[c[0]][c[1]] == 7
                #     or self.grid[d[0]][d[1]] == 7):
                    
                #     # change value of grid units where tetrimino reaches bottom
                #     if self.tetrimino.check() == "S":
                #         # change value of unit on grid
                #         self.grid[a[0] - 1][a[1]] = 1
                #         self.grid[b[0] - 1][b[1]] = 1
                #         self.grid[c[0 - 1]][c[1]] = 1
                #         self.grid[d[0] - 1][d[1]] = 1
                #     elif self.tetrimino.check() == "Z":
                #         # change value of unit on grid
                #         self.grid[a[0] - 1][a[1]] = 2
                #         self.grid[b[0] - 1][b[1]] = 2
                #         self.grid[c[0] - 1][c[1]] = 2
                #         self.grid[d[0] - 1][d[1]] = 2
                #     elif self.tetrimino.check() == "I":
                #         # change value of unit on grid
                #         self.grid[a[0] - 1][a[1]] = 3
                #         self.grid[b[0] - 1][b[1]] = 3
                #         self.grid[c[0] - 1][c[1]] = 3
                #         self.grid[d[0] - 1][d[1]] = 3
                #     if self.tetrimino.check() == "J":
                #         # change value of unit on grid
                #         self.grid[a[0] - 1][a[1]] = 4
                #         self.grid[b[0] - 1][b[1]] = 4
                #         self.grid[c[0] - 1][c[1]] = 4
                #         self.grid[d[0] - 1][d[1]] = 4
                #     if self.tetrimino.check() == "L":
                #         # change value of unit on grid
                #         self.grid[a[0] - 1][a[1]] = 5
                #         self.grid[b[0] - 1][b[1]] = 5
                #         self.grid[c[0] - 1][c[1]] = 5
                #         self.grid[d[0] - 1][d[1]] = 5
                #     if self.tetrimino.check() == "O":
                #         # change value of unit on grid
                #         self.grid[a[0] - 1][a[1]] = 6
                #         self.grid[b[0] - 1][b[1]] = 6
                #         self.grid[c[0] - 1][c[1]] = 6
                #         self.grid[d[0] - 1][d[1]] = 6
                #     if self.tetrimino.check() == "T":
                #         # change value of unit on grid
                #         self.grid[a[0] - 1][a[1]] = 7
                #         self.grid[b[0] - 1][b[1]] = 7
                #         self.grid[c[0] - 1][c[1]] = 7
                #         self.grid[d[0] - 1][d[1]] = 7
                        
                    # make new choice of tetrimino
                    # self.tetrimino = random.choice(self.list_tetriminos)()


                # # making old tetrimino stay where it last stopped
                # if self.grid[row][col] == 1:
                #     color = "green"
                #     self.draw_square(tile_size, color, True)
                # elif self.grid[row][col] == 2:
                #     color = "red"
                #     self.draw_square(tile_size, color, True)
                # elif self.grid[row][col] == 3:
                #     color = "blue"
                #     self.draw_square(tile_size, color, True)
                # elif self.grid[row][col] == 4:
                #     color = "purple"
                #     self.draw_square(tile_size, color, True)
                # elif self.grid[row][col] == 5:
                #     color = "orange"
                #     self.draw_square(tile_size, color, True)
                # elif self.grid[row][col] == 6:
                #     color = "yellow"
                #     self.draw_square(tile_size, color, True)
                # elif self.grid[row][col] == 7:
                #     color = "pink"
                #     self.draw_square(tile_size, color, True)
                
                
                ###################################
                # # checking whether rows and cols in loop over whole grid
                # # are valid values within self.tetrimino blocks
                # if ((row == a[0] or row == b[0] or row == c[0] or row == d[0])
                #     and (col == a[1] or col == b[1] or col == c[1] or col == d[1])):
                #     # looping over each index of self.tetrimino blocks 
                #     for index in range(4):
                #         # checking whether the values at each index are equal
                #         # to a row and col pair
                #         if [row, col] == self.tetrimino.blocks[index]:
                #             # checking which tetrimino piece is being drawn 
                #             # changing color of drawn square to corresponding tetrimino
                #             if self.tetrimino.check() == "S": 
                #                 #print("works")
                #                 color = "green"
                #                 self.draw_square(tile_size, color, True)
                #             elif self.tetrimino.check() == "Z": 
                #                 #print("works")
                #                 color = "red"
                #                 self.draw_square(tile_size, color, True)
                #             elif self.tetrimino.check() == "I": 
                #                 #print("works")
                #                 color = "blue"
                #                 self.draw_square(tile_size, color, True)
                #             elif self.tetrimino.check() == "J": 
                #                 #print("works")
                #                 color = "purple"
                #                 self.draw_square(tile_size, color, True)
                #             elif self.tetrimino.check() == "L": 
                #                 #print("works")
                #                 color = "orange"
                #                 self.draw_square(tile_size, color, True)
                #             elif self.tetrimino.check() == "O": 
                #                 #print("works")
                #                 color = "yellow"
                #                 self.draw_square(tile_size, color, True)
                #             elif self.tetrimino.check() == "T": 
                #                 #print("works")
                #                 color = "pink"
                #                 self.draw_square(tile_size, color, True)


    # def draw_board(self, window, x_offset, y_offset, tile_size):
    #     ''' draws tetris board with specific tile_size by implementing draw_square function '''

    #     # making things on screen draw quickly
    #     window.tracer(False)

    #     # go over every cell in the grid
    #     for row in range(len(self.grid)):
    #         for col in range(len(self.grid[row])):

    #             # find x, y for drawing cell
    #             x_cor = (tile_size * col) + x_offset
    #             y_cor = -((tile_size * row) - y_offset)

    #             # move turtle to the position of the cell in the grid
    #             self.turt.up() 
    #             self.turt.goto(x_cor, y_cor)
    #             self.turt.down()

    #             # setting variables to each list in self.tetrimino blocks
    #             a = self.tetrimino.blocks[0] 
    #             b = self.tetrimino.blocks[1]
    #             c = self.tetrimino.blocks[2]
    #             d = self.tetrimino.blocks[3]
    #             list_letters = [a, b, c, d]
                
    #             ################### below here until multi-line code commented out part
    #             # make sure tetrimino position is within bounds of self.grid
    #             if (a[0] < 0 
    #                 or b[0] < 0 
    #                 or c[0] < 0 
    #                 or d[0] < 0
    #                 or a[1] < 0
    #                 or b[1] < 0
    #                 or c[1] < 0
    #                 or d[1] < 0
    #                 or a[1] > len(self.grid[0]) - 1
    #                 or b[1] > len(self.grid[0]) - 1
    #                 or c[1] > len(self.grid[0]) - 1
    #                 or d[1] > len(self.grid[0]) - 1):
                    
    #                 return False
                
    #             # else if check if tetrimino has reached the bottom of the board
    #             # or if the tetrimino has touched another tetrimino
    #             elif (a[0] > len(self.grid) - 1 
    #                 or b[0] > len(self.grid) - 1
    #                 or c[0] > len(self.grid) - 1
    #                 or d[0] > len(self.grid) - 1
    #                 or self.grid[a[0]][a[1]] == 1
    #                 or self.grid[b[0]][b[1]] == 1
    #                 or self.grid[c[0]][c[1]] == 1
    #                 or self.grid[d[0]][d[1]] == 1
    #                 or self.grid[a[0]][a[1]] == 2
    #                 or self.grid[b[0]][b[1]] == 2
    #                 or self.grid[c[0]][c[1]] == 2
    #                 or self.grid[d[0]][d[1]] == 2
    #                 or self.grid[a[0]][a[1]] == 3
    #                 or self.grid[b[0]][b[1]] == 3
    #                 or self.grid[c[0]][c[1]] == 3
    #                 or self.grid[d[0]][d[1]] == 3
    #                 or self.grid[a[0]][a[1]] == 4
    #                 or self.grid[b[0]][b[1]] == 4
    #                 or self.grid[c[0]][c[1]] == 4
    #                 or self.grid[d[0]][d[1]] == 4
    #                 or self.grid[a[0]][a[1]] == 5
    #                 or self.grid[b[0]][b[1]] == 5
    #                 or self.grid[c[0]][c[1]] == 5
    #                 or self.grid[d[0]][d[1]] == 5
    #                 or self.grid[a[0]][a[1]] == 6
    #                 or self.grid[b[0]][b[1]] == 6
    #                 or self.grid[c[0]][c[1]] == 6
    #                 or self.grid[d[0]][d[1]] == 6
    #                 or self.grid[a[0]][a[1]] == 7
    #                 or self.grid[b[0]][b[1]] == 7
    #                 or self.grid[c[0]][c[1]] == 7
    #                 or self.grid[d[0]][d[1]] == 7):
                    
    #                 # change value of grid units where tetrimino reaches bottom
    #                 if self.tetrimino.check() == "S":
    #                     # change value of unit on grid
    #                     self.grid[a[0] - 1][a[1]] = 1
    #                     self.grid[b[0] - 1][b[1]] = 1
    #                     self.grid[c[0 - 1]][c[1]] = 1
    #                     self.grid[d[0] - 1][d[1]] = 1
    #                 elif self.tetrimino.check() == "Z":
    #                     # change value of unit on grid
    #                     self.grid[a[0] - 1][a[1]] = 2
    #                     self.grid[b[0] - 1][b[1]] = 2
    #                     self.grid[c[0] - 1][c[1]] = 2
    #                     self.grid[d[0] - 1][d[1]] = 2
    #                 elif self.tetrimino.check() == "I":
    #                     # change value of unit on grid
    #                     self.grid[a[0] - 1][a[1]] = 3
    #                     self.grid[b[0] - 1][b[1]] = 3
    #                     self.grid[c[0] - 1][c[1]] = 3
    #                     self.grid[d[0] - 1][d[1]] = 3
    #                 if self.tetrimino.check() == "J":
    #                     # change value of unit on grid
    #                     self.grid[a[0] - 1][a[1]] = 4
    #                     self.grid[b[0] - 1][b[1]] = 4
    #                     self.grid[c[0] - 1][c[1]] = 4
    #                     self.grid[d[0] - 1][d[1]] = 4
    #                 if self.tetrimino.check() == "L":
    #                     # change value of unit on grid
    #                     self.grid[a[0] - 1][a[1]] = 5
    #                     self.grid[b[0] - 1][b[1]] = 5
    #                     self.grid[c[0] - 1][c[1]] = 5
    #                     self.grid[d[0] - 1][d[1]] = 5
    #                 if self.tetrimino.check() == "O":
    #                     # change value of unit on grid
    #                     self.grid[a[0] - 1][a[1]] = 6
    #                     self.grid[b[0] - 1][b[1]] = 6
    #                     self.grid[c[0] - 1][c[1]] = 6
    #                     self.grid[d[0] - 1][d[1]] = 6
    #                 if self.tetrimino.check() == "T":
    #                     # change value of unit on grid
    #                     self.grid[a[0] - 1][a[1]] = 7
    #                     self.grid[b[0] - 1][b[1]] = 7
    #                     self.grid[c[0] - 1][c[1]] = 7
    #                     self.grid[d[0] - 1][d[1]] = 7
                        
    #                 # make new choice of tetrimino
    #                 self.tetrimino = random.choice(self.list_tetriminos)()
                
    #             '''
    #             for letter in list_letters:
    #                 # make sure tetrimino position is within bounds of self.grid
    #                 if (letter[0] < 0 
    #                     or letter[1] < 0
    #                     or letter[1] > len(self.grid[0]) - 1):
                    
    #                     return False
                
    #                 # else if check if tetrimino has reached the bottom of the board
    #                 # or if the tetrimino has touched another tetrimino
    #                 elif (letter[0] > len(self.grid) - 1 
    #                     or self.grid[letter[0]][letter[1]] == 1
    #                     or self.grid[letter[0]][letter[1]] == 2
    #                     or self.grid[letter[0]][letter[1]] == 3
    #                     or self.grid[letter[0]][letter[1]] == 4
    #                     or self.grid[letter[0]][letter[1]] == 5
    #                     or self.grid[letter[0]][letter[1]] == 6
    #                     or self.grid[letter[0]][letter[1]] == 7):
                
    #                     # change value of grid units where tetrimino reaches bottom
    #                     if self.tetrimino.check() == "S":
    #                         # change value of unit on grid
    #                         for letter in list_letters:
    #                             self.grid[letter[0] - 1][letter[1]] = 1
    #                     elif self.tetrimino.check() == "Z":
    #                         # change value of unit on grid
    #                         for letter in list_letters:
    #                             self.grid[letter[0] - 1][letter[1]] = 2
    #                     elif self.tetrimino.check() == "I":
    #                         # change value of unit on grid
    #                         for letter in list_letters:
    #                             self.grid[letter[0] - 1][letter[1]] = 3
    #                     if self.tetrimino.check() == "J":
    #                         # change value of unit on grid
    #                         for letter in list_letters:
    #                             self.grid[letter[0] - 1][letter[1]] = 4
    #                     if self.tetrimino.check() == "L":
    #                         # change value of unit on grid
    #                         for letter in list_letters:
    #                             self.grid[letter[0] - 1][letter[1]] = 5
    #                     if self.tetrimino.check() == "O":
    #                         # change value of unit on grid
    #                         for letter in list_letters:
    #                             self.grid[letter[0] - 1][letter[1]] = 6
    #                     if self.tetrimino.check() == "T":
    #                         # change value of unit on grid
    #                         for letter in list_letters:
    #                             self.grid[letter[0] - 1][letter[1]] = 7
                        
    #                     # make new choice of tetrimino
    #                     self.tetrimino = random.choice(self.list_tetriminos)()
    #             '''


    #             # making old tetrimino stay where it last stopped
    #             if self.grid[row][col] == 1:
    #                 color = "green"
    #                 self.draw_square(tile_size, color, True)
    #             elif self.grid[row][col] == 2:
    #                 color = "red"
    #                 self.draw_square(tile_size, color, True)
    #             elif self.grid[row][col] == 3:
    #                 color = "blue"
    #                 self.draw_square(tile_size, color, True)
    #             elif self.grid[row][col] == 4:
    #                 color = "purple"
    #                 self.draw_square(tile_size, color, True)
    #             elif self.grid[row][col] == 5:
    #                 color = "orange"
    #                 self.draw_square(tile_size, color, True)
    #             elif self.grid[row][col] == 6:
    #                 color = "yellow"
    #                 self.draw_square(tile_size, color, True)
    #             elif self.grid[row][col] == 7:
    #                 color = "pink"
    #                 self.draw_square(tile_size, color, True)
                
                
    #             ###################################
    #             # checking whether rows and cols in loop over whole grid
    #             # are valid values within self.tetrimino blocks
    #             if ((row == a[0] or row == b[0] or row == c[0] or row == d[0])
    #                 and (col == a[1] or col == b[1] or col == c[1] or col == d[1])):
    #                 # looping over each index of self.tetrimino blocks 
    #                 for index in range(4):
    #                     # checking whether the values at each index are equal
    #                     # to a row and col pair
    #                     if [row, col] == self.tetrimino.blocks[index]:
    #                         # checking which tetrimino piece is being drawn 
    #                         # changing color of drawn square to corresponding tetrimino
    #                         if self.tetrimino.check() == "S": 
    #                             #print("works")
    #                             color = "green"
    #                             self.draw_square(tile_size, color, True)
    #                         elif self.tetrimino.check() == "Z": 
    #                             #print("works")
    #                             color = "red"
    #                             self.draw_square(tile_size, color, True)
    #                         elif self.tetrimino.check() == "I": 
    #                             #print("works")
    #                             color = "blue"
    #                             self.draw_square(tile_size, color, True)
    #                         elif self.tetrimino.check() == "J": 
    #                             #print("works")
    #                             color = "purple"
    #                             self.draw_square(tile_size, color, True)
    #                         elif self.tetrimino.check() == "L": 
    #                             #print("works")
    #                             color = "orange"
    #                             self.draw_square(tile_size, color, True)
    #                         elif self.tetrimino.check() == "O": 
    #                             #print("works")
    #                             color = "yellow"
    #                             self.draw_square(tile_size, color, True)
    #                         elif self.tetrimino.check() == "T": 
    #                             #print("works")
    #                             color = "pink"
    #                             self.draw_square(tile_size, color, True)
    #             elif (self.grid[row][col] != 1 
    #                 and self.grid[row][col] != 2 
    #                 and self.grid[row][col] != 3
    #                 and self.grid[row][col] != 4
    #                 and self.grid[row][col] != 5
    #                 and self.grid[row][col] != 6
    #                 and self.grid[row][col] != 7):

    #                 # draw empty square in that position
    #                 self.draw_square(tile_size, "white", True)