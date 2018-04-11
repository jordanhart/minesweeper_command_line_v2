import random

def play():
    board, length, width, num_mines = set_up()
    selected = set()
    winner = -1
    while (winner < 0):
        winner = take_turn(board, length, selected, num_mines)
    if (winner == 0):
        print("You lost!")
    elif (winner == 1):
        print("congrats! You won!")
    
    print_board(board, length, range(len(board)))

def set_up():
    board_selection = False
    while (board_selection != 1 and board_selection !=2 and board_selection != 3):
        board_selection = int(input("what size board do you want to play with? \n 1) 8x8 \n 2) 16x16 \n 3) 16x30 \n "))
    if (board_selection == 1):
        board_length = 8
        board_width = 8
        num_mines = 10
    elif (board_selection == 2):
        board_length = 16
        board_width = 16
        num_mines = 40
    elif (board_selection == 3):
        board_length = 16
        board_width = 30
        num_mines = 99
    else:
        return -1, -1, -1, -1
    board = fill_board(board_length, board_width, num_mines)
    return board, board_length, board_width, num_mines
def fill_board(board_length, board_width, num_mines):
    mines = random.sample(range(0, board_length * board_width), num_mines)
    board_size = board_length * board_width
    board = [0 for i in range(board_size)]
    for s in mines:
        board[s] = 'x'
    for s in range(board_size):
        if board[s] != 'x':
            board[s] = get_num_mines_nearby(board, s, board_length)
    return board

def get_num_mines_nearby(board, s, length):
    if (s % length == 0): #at beginning column of board
        nearby = [s+1, s + length, s + length + 1, s - length, s - length + 1]
    elif (s % length - 1 == 0): #at ending column of board
        nearby = [s-1, s + length, s+length - 1, s - length, s - length - 1]
    else: #inbetween
        nearby = [s - 1, s + 1, s + length, s - length, s + length + 1, s + length - 1, s - length - 1, s - length + 1]
    total = 0
    for s in nearby:
        if s >= 0 and s < len(board) and board[s] == 'x':
            total += 1
    return total

def print_board(board, length, selected):
    for i in range(len(board)):
        if i not in selected:
            letter = "_"
        else:
            letter = str(board[i])
        if (i % length == 0): #at beginning
            beginning = "\n|"
        else:
            beginning = ""
        print(beginning + str(letter), end="|")
    print()
def take_turn(board, length, selected, num_mines):
    select = -1
    while(select == -1 or select in selected):
        print_board(board, length, selected)
        select = int(input("please select a square from 1 to " + str(len(board)) + ": ")) - 1 #0 indexed
    selected.add(select)
    return determine_game_state(board, select, num_mines, selected)

def determine_game_state(board, s, num_mines, selected):
    if (board[s] == 'x'):
        return 0
    elif (len(board) - len(selected) == num_mines):
        return 1
    else:
        return -1


play()
