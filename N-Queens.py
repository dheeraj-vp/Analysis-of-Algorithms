def solveNQueens(n):
    col = set()
    postdiag = set()
    negdiag = set()
    
    res = []
    board = [["."] * n for _ in range(n)]
    
    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return
        
        for c in range(n):
            if c in col or (r + c) in postdiag or (r - c) in negdiag:
                continue
            
            col.add(c)
            postdiag.add(r + c)
            negdiag.add(r - c)
            board[r][c] = "Q"
            
            backtrack(r + 1)
            
            col.remove(c)
            postdiag.remove(r + c)
            negdiag.remove(r - c)
            board[r][c] = "."
    
    backtrack(0)
    return res

def print_solutions(solutions):
    for i, sol in enumerate(solutions):
        print(f"Solution {i + 1}:")
        for row in sol:
            print(row)
        print()

n = int(input("Enter the value of N: "))
solutions = solveNQueens(n)
print_solutions(solutions)
