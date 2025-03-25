def matrix_chain_order(p):
    n = len(p) - 1  
    dp = [[0] * (n + 1) for _ in range(n + 1)]  # DP table for costs
    split = [[0] * (n + 1) for _ in range(n + 1)]  # Table for parenthesization
    
    for l in range(2, n + 1):  # Chain length
        for i in range(1, n - l + 2):  
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i, j):  
                cost = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k  # Store optimal split point

    return dp, split

def get_parenthesization(split, i, j):
    """Recursively constructs the optimal parenthesization."""
    if i == j:
        return f"M{i}"
    else:
        k = split[i][j]
        left_part = get_parenthesization(split, i, k)
        right_part = get_parenthesization(split, k + 1, j)
        return f"({left_part} × {right_part})"

# Input handling
n = int(input("Enter number of matrices: "))
dimensions = [int(input(f"Enter dimension {i + 1}: ")) for i in range(n + 1)]

# Compute DP table and splits
dp, split = matrix_chain_order(dimensions)

# Get result
print("Minimum scalar multiplications:", dp[1][n])
print("Optimal Parenthesization:", get_parenthesization(split, 1, n))