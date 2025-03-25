def assembly_line(a, t, e, x):
    n = len(a[0])
    dp1 = e[0] + a[0][0]
    dp2 = e[1] + a[1][0]
    
    prev_line0 = [-1] * n
    prev_line1 = [-1] * n
    
    for j in range(1, n):
        # Calculate for line 1 (0-based)
        option1_line0 = dp1 + a[0][j]
        option2_line0 = dp2 + t[1][j-1] + a[0][j]
        if option1_line0 <= option2_line0:
            new_dp1 = option1_line0
            prev_line0[j] = 0
        else:
            new_dp1 = option2_line0
            prev_line0[j] = 1
        
        # Calculate for line 2 (0-based)
        option1_line1 = dp2 + a[1][j]
        option2_line1 = dp1 + t[0][j-1] + a[1][j]
        if option1_line1 <= option2_line1:
            new_dp2 = option1_line1
            prev_line1[j] = 1
        else:
            new_dp2 = option2_line1
            prev_line1[j] = 0
        
        dp1, dp2 = new_dp1, new_dp2
    
    exit0 = dp1 + x[0]
    exit1 = dp2 + x[1]
    
    if exit0 <= exit1:
        exit_line = 0
        total_time = exit0
    else:
        exit_line = 1
        total_time = exit1
    
    # Backtrack to find the optimal path
    current_line = exit_line
    current_j = n - 1
    path = [(current_line, current_j)]
    
    while current_j > 0:
        if current_line == 0:
            prev_l = prev_line0[current_j]
        else:
            prev_l = prev_line1[current_j]
        current_j -= 1
        current_line = prev_l
        path.append((current_line, current_j))
    
    # Reverse to get the path from start to end and convert to 1-based
    path = path[::-1]
    optimal_path = [(line + 1, station + 1) for (line, station) in path]
    
    return total_time, optimal_path

n = int(input("Enter number of stations: "))
a = [[int(x) for x in input(f"Enter time for line {i + 1}: ").split()] for i in range(2)]
t = [[int(x) for x in input(f"Enter transfer time from line {i + 1}: ").split()] for i in range(2)]
e = [int(x) for x in input("Enter entry times: ").split()]
x = [int(x) for x in input("Enter exit times: ").split()]
time, path = assembly_line(a, t, e, x)
print("Minimum time to assemble car chassis:", time)
print("Optimal path:")
for step in path:
    print(f"Line {step[0]}, Station {step[1]}")