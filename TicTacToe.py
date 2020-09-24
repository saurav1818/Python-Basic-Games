
# -------GLOBAL VARIABLES-------
# Game board
board = ['_', '_', '_',
         '_', '_', '_',
         '_', '_', '_']

# check if game is still going
game_still_going = True

# check current player
current_player = 'X'

# check winner
winner = None

# Display Game Board
def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

# Handle turn
def handle_turn(player):
    print(player + '\'s turn')
    postion = input('Choose a value from 1-9: ')

    valid = False
    while not valid:
        while postion not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            postion = input('Choose a value from 1-9: ')


        postion = int(postion) - 1

        if board[postion] == '_':
            valid = True
        else:
            print("You can't go there")

    board[postion] = player
    display_board()

# Check for winner
def check_for_winner():
    global winner
    row_winner = check_rows()

    columns_winner = check_columns()

    diagonals_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif columns_winner:
        winner = columns_winner
    elif diagonals_winner:
        winner = diagonals_winner
    else:
        winner = None
    return

def check_rows():
    global game_still_going

    row_1 = board[0] == board[1] == board[2] != '_'
    row_2 = board[3] == board[4] == board[5] != '_'
    row_3 = board[6] == board[7] == board[8] != '_'

    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return

def check_columns():
    global game_still_going

    col_1 = board[0] == board[3] == board[6] != '_'
    col_2 = board[1] == board[4] == board[7] != '_'
    col_3 = board[2] == board[5] == board[8] != '_'

    if col_1 or col_2 or col_3:
        game_still_going = False

    if col_1:
        return board[0]
    if col_2:
        return board[1]
    if col_3:
        return board[2]
    return

def check_diagonals():
    global game_still_going

    diag_1 = board[0] == board[4] == board[8] != '_'
    diag_2 = board[2] == board[4] == board[6] != '_'

    if diag_1 or diag_2:
        game_still_going = False

    if diag_1:
        return board[0]
    if diag_2:
        return board[2]
    return


def check_if_tie():
    global game_still_going

    if '_' not in board:
        game_still_going = False
    return


def check_if_game_over():
    check_for_winner()
    check_if_tie()

def flip_player():
    global current_player

    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return

# Main loop of game
def play_game():
    display_board()
    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()
    if winner == 'X' or winner == 'O':
        print(winner + ' Won')
    elif winner == None:
        print('Tie')


play_game()