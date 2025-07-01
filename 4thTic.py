def print_board(board):
    """Print the current state of the Tic-Tac-Toe board"""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """Check if the specified player has won the game"""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    """Check if the board is full"""
    return all(cell != ' ' for row in board for cell in row)

def tic_tac_toe():
    """Main function to play the game"""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
        except ValueError:
            print("Please enter valid numbers!")
            continue

        if 0 <= row <= 2 and 0 <= col <= 2:
            if board[row][col] == ' ':
                board[row][col] = current_player
            else:
                print("That cell is already taken. Try again.")
                continue
        else:
            print("Invalid input! Please enter numbers between 1 and 3.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
