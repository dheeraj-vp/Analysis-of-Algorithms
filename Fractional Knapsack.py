def fractional_knapsack(items, capacity):
    # Sort by value-to-weight ratio in descending order
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0
    for value, weight in items:
        if capacity == 0:
            break
        fraction = min(weight, capacity)  # Take full weight if possible, otherwise partial
        total_value += fraction * (value / weight)
        capacity -= fraction
        print(f"Item({value}, {weight}) -> Fraction: {fraction / weight:.2f}")

    return total_value

n = int(input("Enter number of items: "))
items = [tuple(map(int, input("Enter value and weight: ").split())) for _ in range(n)]
capacity = int(input("Enter knapsack capacity: "))
print("Maximum value of the knapsack:", fractional_knapsack(items, capacity))
