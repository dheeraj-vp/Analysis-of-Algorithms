SIZE = 4

def display_board(board):
    print("\n=== Arrangement ===\n")
    for row in board:
        print(" ".join("R" if cell else "." for cell in row))
    print()

def place_rooks(board, col, solutions):
    if col == SIZE:
        solutions.append([row[:] for row in board])
        display_board(board)
        return
    
    for row in range(SIZE):
        if all(board[row][c] == 0 for c in range(col)):  # Check if placement is valid
            board[row][col] = 1
            place_rooks(board, col + 1, solutions)
            board[row][col] = 0  # Backtrack

board = [[0] * SIZE for _ in range(SIZE)]
solutions = []
place_rooks(board, 0, solutions)
print(f"Total Arrangements Displayed: {len(solutions)}")