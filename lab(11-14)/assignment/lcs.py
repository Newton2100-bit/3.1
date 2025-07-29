def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)

    # Create a table to store lengths of LCSs for subproblems
    # dp[i][j] will store the length of the LCS of X[0..i-1] and Y[0..j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the dp table in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to reconstruct the LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # The LCS is constructed backwards, so reverse it
    return "".join(reversed(lcs))

if __name__ == '__main__':
    # Example usage:
    string1 = "AGGTAB"
    string2 = "GXTXAYB"
    
    lcs = longest_common_subsequence(string1, string2)
    
    print(f"The Longest Common Subsequence is: {lcs}")
