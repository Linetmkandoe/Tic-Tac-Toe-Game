# initialze the board as a 3*3 grid filled with empty spaces
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]
# list comprehension to create the grid
def display_board(board):
    #  takes the current state of the boardand display it
    for row in board:
        print('|'.join(row))
        print('-' * 5)
def check_winner(board, player):
    0
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False
def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))
def take_turn(board, player):
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
def play_game():
    board = initialize_board()
    players = ['X', 'O']
    current_player = 0
    while True:
        display_board(board)
        player = players[current_player]
        print(f"Player {player}'s turn.")
        take_turn(board, player)
        if check_winner(board, player):
            display_board(board)
            print(f"Player {player} wins!")
            break
        elif is_board_full(board):
            display_board(board)
            print("It's a draw!")
            break
        current_player = (current_player + 1) % 2
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == 'yes':
        play_game()
    else:
        print("Thanks for playing!")
if __name__ == "__main__":
    play_game()