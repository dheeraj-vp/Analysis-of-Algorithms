def lcs(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    
    # Fill DP table
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to find LCS string
    i, j = len(a), len(b)
    lcs_str = []
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            lcs_str.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(lcs_str[::-1])

a = input("Enter first sequence: ")
b = input("Enter second sequence: ")
print("LCS:", lcs(a, b), "Len:",len(lcs(a,b)))
