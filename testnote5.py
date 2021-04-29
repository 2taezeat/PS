
columns = 3
rows = 5

board = [ [0 for i in range(columns)] for i in range(rows)]


c = 0
while(c < columns*rows):

    i = c % columns
    j = c // columns

    board[j][i] = c + 1
    c = c + 1


print(board)