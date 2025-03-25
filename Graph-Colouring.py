MAX = 20
COLORS = 4
color_names = ["Red", "Green", "Violet", "Blue"]

graph = [[0] * MAX for _ in range(MAX)]
color = [-1] * MAX

V = int(input("Enter the number of vertices: "))

print("Enter the adjacency matrix:")
graph = [list(map(int, input().split())) for _ in range(V)]

def is_safe(v, c, V):
    for i in range(V):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def graph_coloring(v, V):
    if v == V:
        return True

    for c in range(COLORS):
        if is_safe(v, c, V):
            color[v] = c
            if graph_coloring(v + 1, V):
                return True
            color[v] = -1
    return False

def print_solution(V):
    print("Solution with minimum colors:")
    for i in range(V):
        print(f"Vertex {i} -> {color_names[color[i]]}")

if graph_coloring(0, V):
    print_solution(V)
else:
    print("Solution is not possible with the given 4 colors for the given graph.")