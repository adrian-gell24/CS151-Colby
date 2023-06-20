blocks = [[1, 1], [1, 2], [1, 3], [1, 4]]

print(blocks[2][0])
blocks[1][0] = blocks[0][1]
blocks[2][0] = blocks[0][2]
blocks[3][0] = blocks[0][3]
print(blocks[1][0])

print(blocks[3][0])