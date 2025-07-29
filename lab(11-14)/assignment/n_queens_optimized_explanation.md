# N-Queens Optimized Approach

This document explains the optimized backtracking approach used to solve the N-Queens problem.

## Optimized Backtracking

Instead of checking the board for safety in every step, which is time-consuming, we can use arrays to keep track of attacked columns and diagonals. This makes the safety check much faster.

1.  **Board Representation:** We use a 1D array `board` where `board[i] = c` means a queen is placed at row `i` and column `c`.

2.  **Tracking Attacks:**
    *   **Columns:** A boolean array `cols` of size `n` is used. `cols[c]` is `True` if a queen is in column `c`.
    *   **Diagonals:** We use two boolean arrays for diagonals:
        *   `diag1`: For diagonals where the sum of the row and column indices is constant (`row + col`). The size of this array is `2 * n - 1`.
        *   `diag2`: For diagonals where the difference between the row and column indices is constant (`row - col`). The size of this array is also `2 * n - 1`.

3.  **Backtracking Logic:**
    *   We place queens row by row, from row 0 to `n-1`.
    *   For each row, we iterate through the columns to find a safe spot.
    *   A position `(row, col)` is safe if `cols[col]`, `diag1[row + col]`, and `diag2[row - col + n - 1]` are all `False`.
    *   If a safe spot is found, we place the queen, mark the corresponding column and diagonals as attacked, and recur for the next row.
    *   If the recursion doesn't lead to a solution, we backtrack by removing the queen and un-marking the column and diagonals.

This approach avoids the need to repeatedly scan the board, making the solution significantly more efficient.
