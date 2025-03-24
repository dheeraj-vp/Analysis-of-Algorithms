def knapsack(weights, values, capacity, n, selected=[], optimal=[[]]):
    if n == 0 or capacity == 0:
        if sum(values[i] for i in selected) > sum(values[i] for i in optimal[0]):
            optimal[0] = selected[:]  # Update the optimal solution
        return sum(values[i] for i in selected)  # Return total value of selected items
    
    if weights[n-1] > capacity:
        return knapsack(weights, values, capacity, n-1, selected, optimal)
    
    # Include the item
    selected.append(n-1)
    include = knapsack(weights, values, capacity - weights[n-1], n-1, selected, optimal)
    selected.pop()  # Backtrack
    
    # Exclude the item
    exclude = knapsack(weights, values, capacity, n-1, selected, optimal)
    
    return max(include, exclude)

# Example usage
weights = [6,10,12,15,14]
values = [10,20,30,40,35]
capacity = 38
n = len(weights)
optimal_solution = [[]]  # Using a list to store the best solution
max_value = knapsack(weights, values, capacity, n, selected=[], optimal=optimal_solution)

print("Selected Weights:", [weights[i] for i in optimal_solution[0]])
print("Selected Values:", [values[i] for i in optimal_solution[0]])
print("Maximum Value:", max_value)
