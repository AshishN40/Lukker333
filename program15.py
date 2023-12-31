"""Q15)Write a computer program to play tic-tac-toe game. (Game Theory)"""
# Tic-Tac-Toe Game

# Initialize the board
board = [' ' for _ in range(9)]

# Function to print the Tic-Tac-Toe board
def print_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])

# Function to check if the board is full
def is_board_full():
    return ' ' not in board

# Function to check if a player has won
def check_winner(player):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to get available moves
def get_available_moves():
    return [i for i, space in enumerate(board) if space == ' ']

# Function to make a player's move
def make_move(player, position):
    board[position] = player

# Main game loop
current_player = 'X'
while True:
    print_board()
    print(f"Player {current_player}'s turn. Enter your move (0-8): ")
    move = int(input())

    if move < 0 or move > 8 or board[move] != ' ':
        print("Invalid move. Try again.")
        continue

    make_move(current_player, move)

    if check_winner(current_player):
        print_board()
        print(f"Player {current_player} wins!")
        break
    elif is_board_full():
        print_board()
        print("It's a tie!")
        break

    current_player = 'O' if current_player == 'X' else 'X'
