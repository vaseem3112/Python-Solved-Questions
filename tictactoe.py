import random

# Initialize the board
def initialize_board():
    return [" " for _ in range(9)]

# Function to print the board
def print_board(board):
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print(" | ".join(row))
        print("-" * 9)

# Function to check for a win
def check_win(board, player):
    win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_patterns)

# Function to check for a tie
def check_tie(board):
    return " " not in board

# Function for bot's move (random)
def bot_move(board):
    available_moves = [i for i in range(9) if board[i] == " "]
    return random.choice(available_moves)

# Function for player vs. bot game
def play_vs_bot():
    board = initialize_board()
    player_symbol = "X"
    bot_symbol = "O"

    while True:
        print_board(board)

        # Player's turn
        move = input(f"Player's turn ({player_symbol}). Enter a position (1-9): ")

        if not move.isdigit() or not (1 <= int(move) <= 9) or board[int(move) - 1] != " ":
            print("Invalid move. Try again.")
            continue

        board[int(move) - 1] = player_symbol

        if check_win(board, player_symbol):
            print_board(board)
            print("Player wins! Congratulations!")
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        # Bot's turn
        bot_position = bot_move(board)
        board[bot_position] = bot_symbol

        if check_win(board, bot_symbol):
            print_board(board)
            print("Bot wins! Better luck next time!")
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

# Function for player vs. player game
def play_vs_player():
    board = initialize_board()
    player1_symbol = "X"
    player2_symbol = "O"
    current_player = player1_symbol

    while True:
        print_board(board)

        print(f"Player {current_player}'s turn. Enter a position (1-9): ")
        move = input()

        if not move.isdigit() or not (1 <= int(move) <= 9) or board[int(move) - 1] != " ":
            print("Invalid move. Try again.")
            continue

        board[int(move) - 1] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins! Congratulations!")
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch players
        current_player = player2_symbol if current_player == player1_symbol else player1_symbol

# Main menu
def main_menu():
    while True:
        print("Welcome to Tic Tac Toe!")
        print("1. Play against Bot")
        print("2. Play between two Players")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            play_vs_bot()
        elif choice == "2":
            play_vs_player()
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()
