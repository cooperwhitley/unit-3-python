########### variables

# declare board as matrix of strings with default value of space 
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


# declare turn with starting value of 1 (O's turn)
turn = 1
# declare winner with starting value of 0
winner = 0

# create score counter using scores[0] for O and scores[1] for x
scores = [0, 0]

# opening message printer function
def open_message():
    print("-------------------------")
    print("| let's play py-pac-poe |")
    print("-------------------------")

# function to print the current board
def board_printer(board):
    print('    A   B   C')
    print(f'1   {board[0][0]} | {board[0][1]} | {board[0][2]}')
    print('   -----------')
    print(f'2   {board[1][0]} | {board[1][1]} | {board[1][2]}')
    print('   -----------')
    print(f'3   {board[2][0]} | {board[2][1]} | {board[2][2]}')

# function to clear board
def board_clearer():
    global board
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

# declare function to handle moves
def move_handler(move):
    global board, turn, scores
    # list of letter and number options so that i can grab their indices to correspond to the board matrix
    letter_nums = ['a', 'b', 'c']
    num_nums = ['1', '2', '3']
    # check to make sure that the move is valid
    if len(move) > 2 or move[0] not in letter_nums or move[1] not in num_nums:
        print(' ')
        print('invalid move due to improper syntax.')
        return turn_handler()
    # set value of converted move variable to be list containing corresponding indices of choices
    converted_move = [move[0], move[1]]
    converted_move[0] = letter_nums.index(converted_move[0])
    converted_move[1] = num_nums.index(converted_move[1])
    # check to make sure cell is not already occupied
    if board[converted_move[1]][converted_move[0]] != ' ':
        print(' ')
        print('invalid move due to it already being played.')
        return turn_handler()
    # establish player character
    player_char = ''
    # set based on turn value
    if turn == 1:
        player_char = 'O'
    elif turn == -1:
        player_char = 'X'
    # set selected board cell to player_char
    board[converted_move[1]][converted_move[0]] = player_char
    # check for a winner or a tie
    check_winner(player_char)
    # advance to next turn if no winner yet
    if winner == 0:
        turn *= -1
        return turn_handler()
    # messages for each outcome plus reinitializing the game
    elif winner == 1:
        scores[0] += 1
        board_printer(board)
        print("-------------------------")
        print("|        O wins!        |")
        print("|   PLAY AGAIN OR ELSE  |")
        print(f"|        O:{scores[0]} X:{scores[1]}        |")
        print("-------------------------")
        init()
    elif winner == -1:
        scores[1] += 1
        board_printer(board)
        print("-------------------------")
        print("|        X wins!        |")
        print("|   PLAY AGAIN OR ELSE  |")
        print(f"|        O:{scores[0]} X:{scores[1]}        |")
        print("-------------------------")
        init()
    elif winner == 2:
        board_printer(board)
        print("-------------------------")
        print("|       It's a tie      |")
        print("|     do better guys    |")
        print("|   PLAY AGAIN OR ELSE  |")
        print(f"|        O:{scores[0]} X:{scores[1]}        |")
        print("-------------------------")
        init()

def turn_handler():
    print(' ')
    print("-------------------------")
    print(' ')
    board_printer(board)
    if turn == 1:
        print("O's turn")
    elif turn == -1:
        print("X's turn")
    # pass a console input for the move
    move_handler(input('Enter a move (ex. A3): ').lower())

def check_winner(char):
    global winner
    # check for diagonal winners
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != ' ' or board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] != ' ':
        winner = turn
        return
    for idx in range(3):
        # check for horizontal winners first, then vertical
        if board[idx][0] == board[idx][1] and board[idx][0] == board[idx][2] and board[idx][0] != ' ' or board[0][idx] == board[1][idx] and board[0][idx] == board[2][idx] and board[0][idx] != ' ':
            winner = turn
            return
    # if all spaces are occupied and there's no winner, it's a tie
    if ' ' not in board[0] and ' ' not in board[1] and ' ' not in board[2]:
        winner = 2

def init():
    global winner, turn
    winner = 0
    turn = 1
    board_clearer()
    turn_handler()

open_message()
init()