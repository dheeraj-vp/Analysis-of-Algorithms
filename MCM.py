def assembly_line(a, t, e, x):
    n = len(a[0])
    dp1 = e[0] + a[0][0]
    dp2 = e[1] + a[1][0]
    for j in range(1, n):
        new_dp1 = min(dp1 + a[0][j], dp2 + t[1][j-1] + a[0][j])
        new_dp2 = min(dp2 + a[1][j], dp1 + t[0][j-1] + a[1][j])
        dp1, dp2 = new_dp1, new_dp2
    return min(dp1 + x[0], dp2 + x[1])

n = int(input("Enter number of stations: "))
a = [[int(x) for x in input(f"Enter time for line {i + 1}: ").split()] for i in range(2)]
t = [[int(x) for x in input(f"Enter transfer time from line {i + 1}: ").split()] for i in range(2)]
e = [int(x) for x in input("Enter entry times: ").split()]
x = [int(x) for x in input("Enter exit times: ").split()]
print("Minimum time to assemble car chassis:", assembly_line(a, t, e, x))