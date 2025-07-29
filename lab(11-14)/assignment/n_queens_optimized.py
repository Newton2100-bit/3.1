
def solve_n_queens_optimized(n):
    """
    Solves the N-Queens problem using an optimized backtracking algorithm.
    """
    solutions = []
    # board[i] = c means a queen is at (i, c)
    board = [-1] * n
    
    # Keep track of attacked columns and diagonals
    # No need for a 'rows' array because we place one queen per row
    cols = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)

    def backtrack(row):
        if row == n:
            # All queens are placed, so we have a solution
            solution = []
            for r in range(n):
                solution.append(f"({r}, {board[r]})")
            solutions.append(solution)
            return

        for col in range(n):
            # Check if the current position is safe
            if cols[col] or diag1[row + col] or diag2[row - col + n - 1]:
                continue

            # Place the queen
            board[row] = col
            cols[col] = True
            diag1[row + col] = True
            diag2[row - col + n - 1] = True

            # Recur for the next row
            backtrack(row + 1)

            # Backtrack: remove the queen
            cols[col] = False
            diag1[row + col] = False
            diag2[row - col + n - 1] = False

    backtrack(0)
    return solutions

if __name__ == "__main__":
    try:
        n_queens = int(input("Enter the number of queens (n): "))
        if n_queens <= 0:
            print("Please enter a positive integer for n.")
        else:
            solutions = solve_n_queens_optimized(n_queens)
            if solutions:
                print(f"Found {len(solutions)} solution(s) for the {n_queens}-Queens problem.")
                print("Board positions of queens (row, column) for the first solution:")
                for pos in solutions[0]:
                    print(pos)
            else:
                print(f"No solutions found for n = {n_queens}")
    except ValueError:
        print("Invalid input. Please enter an integer.")
