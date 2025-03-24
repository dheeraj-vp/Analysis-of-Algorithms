def print_solution(subset):
    print(" ".join(map(str, subset)))

def subset_sum(index, curr_sum, start, subset):
    if curr_sum == target_sum:
        print_solution(subset)
        return

    for i in range(start, n):
        if curr_sum + numbers[i] <= target_sum:
            # print(f"{curr_sum} + {numbers[i]} <= {target_sum}")  # Fixed line
            # print(index + 1, curr_sum + numbers[i], i + 1, subset + [numbers[i]])
            subset_sum(index + 1, curr_sum + numbers[i], i + 1, subset + [numbers[i]])

# Input
n = int(input("Enter the number of elements: "))
numbers = list(map(int, input("Enter the elements: ").split()))
print(numbers)
target_sum = int(input("Enter the target sum: "))

print(f"Subsets with sum {target_sum}:")
subset_sum(0, 0, 0, [])
