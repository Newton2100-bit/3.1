
def is_safe(board, row, col):
    """
    Checks if placing a queen at board[row][col] is safe.
    A position is safe if no other queen attacks it horizontally, vertically, or diagonally.
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, n, solutions):
    """
    Recursive utility function to solve the N-Queens problem using backtracking.
    'board' is the current state of the chessboard.
    'col' is the current column being considered for placing a queen.
    'n' is the size of the board (n x n).
    'solutions' is a list to store all valid queen placements.
    """
    # Base case: If all queens are placed, add the current board configuration to solutions
    if col >= n:
        solution = []
        for r in range(n):
            for c in range(n):
                if board[r][c] == 1:
                    solution.append(f"({r}, {c})") # Store queen's position as (row, col)
        solutions.append(solution)
        return True # Indicate that a solution was found (though we continue to find all)

    res = False
    # Consider this column and try placing a queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col):
            board[i][col] = 1 # Place queen

            # Recur to place rest of the queens
            res = solve_n_queens_util(board, col + 1, n, solutions) or res

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove queen (backtrack)
            board[i][col] = 0 # Backtrack

    return res

def solve_n_queens(n):
    """
    Main function to solve the N-Queens problem.
    Initializes the board and calls the utility function.
    Prints the board positions for the first found solution.
    """
    board = [[0 for _ in range(n)] for _ in range(n)] # Initialize n x n board with zeros
    solutions = [] # List to store all found solutions

    if not solve_n_queens_util(board, 0, n, solutions):
        print(f"Solution does not exist for n = {n}")
        return

    # Display the board positions of the n queens for the first solution
    if solutions:
        print(f"Solution for {n}-Queens problem:")
        print("Board positions of queens (row, column):")
        for pos in solutions[0]: # Print only the first solution
            print(pos)
    else:
        print(f"No solutions found for n = {n}")

if __name__ == "__main__":
    try:
        n_queens = int(input("Enter the number of queens (n): "))
        if n_queens <= 0:
            print("Please enter a positive integer for n.")
        else:
            solve_n_queens(n_queens)
    except ValueError:
        print("Invalid input. Please enter an integer.")
