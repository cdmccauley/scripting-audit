from random import randrange

def display_board(board):
    for row in board:
        for cell in row:
            print(cell, end=" ")
        print()

def enter_move(board):
    move = int(input("Enter your move: "))
    for row in range(len(board)):
        for column in range(len(board[row])):
            if move == board[row][column]:
                board[row][column] = "O"
                break

def make_list_of_free_fields(board):
    free_fields = []
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] != "X" and board[row][column] != "O":
                free_fields.append((row, column))
    return free_fields

def victory_for(board, sign):
    # horizontal
    for row in board:
        if row[0] == sign and row[1] == sign and row[2] == sign:
            return True
    # vertical
    for column in range(len(board[0])):
        if board[0][column] == sign and board[1][column] == sign and board[2][column] == sign:
            return True
    # diagonal
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    # no victory
    return False

def draw_move(board):
    move = randrange(len(make_list_of_free_fields(board)))
    row, column = make_list_of_free_fields(board)[move]
    board[row][column] = "X"

gBoard = [[0, 1, 2], [3, "X", 5], [6, 7, 8]]
display_board(gBoard)

while True:
    if victory_for(gBoard, "X"):
        print("The computer won...")
        break
    if len(make_list_of_free_fields(gBoard)) == 0:
        print("It's a draw...")
        break
    else:
        enter_move(gBoard)
        display_board(gBoard)
        print()
        
    if victory_for(gBoard, "O"):
        print("You won!")
        break
    if len(make_list_of_free_fields(gBoard)) == 0:
        print("It's a draw...")
        break
    else:
        draw_move(gBoard)
        display_board(gBoard)
        