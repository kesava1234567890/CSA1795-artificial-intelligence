def is_safe(board, row, col):
    # Check if there is a queen in the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_queens(board, col):
    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_queens(board, col + 1):
                return True

            board[i][col] = 0  # Backtrack if placing a queen does not lead to a solution

    return False

def print_solution(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=" ")
        print()

# Function to solve the 8 Queens Problem
def solve_8queens():
    board = [[0 for _ in range(8)] for _ in range(8)]

    if not solve_queens(board, 0):
        print("No solution exists")
        return

    print("Solution:")
    print_solution(board)

# Solve and print the solution
solve_8queens()
