board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# Try all numbers at the empty square
# function to print the board with the spaces so it's easy to look at and understand for a human
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - -")

        for j in range(len(board[0])):
            # print a | behind every third element but not at the beginning
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            # when we access the last element of the row, print [i][j]
            if j == 8:
                print(board[i][j])
            # otherwise
            else:
                print(str(board[i][j]) + " ", end=" ")

# Pick an empty Square
def find_empty_value(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j     # row, column


print_board(board)