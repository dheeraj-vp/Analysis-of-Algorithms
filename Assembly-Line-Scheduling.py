def assembly_line_scheduling(n, a, t, e, x):
    T1, T2 = [0] * n, [0] * n
    L1, L2, path = [0] * n, [0] * n, [0] * n

    T1[0], T2[0] = e[0] + a[0][0], e[1] + a[1][0]

    for i in range(1, n):
        if T1[i - 1] <= T2[i - 1] + t[1][i - 1]:
            T1[i], L1[i] = T1[i - 1] + a[0][i], 1
        else:
            T1[i], L1[i] = T2[i - 1] + t[1][i - 1] + a[0][i], 2

        if T2[i - 1] <= T1[i - 1] + t[0][i - 1]:
            T2[i], L2[i] = T2[i - 1] + a[1][i], 2
        else:
            T2[i], L2[i] = T1[i - 1] + t[0][i - 1] + a[1][i], 1

    if T1[-1] + x[0] <= T2[-1] + x[1]:
        final_time, final_line = T1[-1] + x[0], 1
    else:
        final_time, final_line = T2[-1] + x[1], 2

    print(f"Output: Minimum time = {final_time}")
    print(f"Final Line: {final_line}")

    path[-1] = final_line
    for i in range(n - 1, 0, -1):
        path[i - 1] = L1[i] if path[i] == 1 else L2[i]

    print("Path:", " -> ".join(f"Station {i+1} on Line {path[i]}" for i in range(n)))

n = int(input("Enter number of stations: "))
a = [list(map(int, input("Enter station times for Line 1: ").split())),
     list(map(int, input("Enter station times for Line 2: ").split()))]
t = [list(map(int, input("Enter transfer times from Line 1 to Line 2: ").split())),
     list(map(int, input("Enter transfer times from Line 2 to Line 1: ").split()))]
e = list(map(int, input("Enter entry times for both lines: ").split()))
x = list(map(int, input("Enter exit times for both lines: ").split()))

assembly_line_scheduling(n, a, t, e, x)