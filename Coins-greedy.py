def sort_descending(coins):
    coins.sort(reverse=True)

def greedy_coin_change(coins, amount):
    used_coins = []
    greedy_count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            used_coins.append(coin)
            greedy_count += 1
    print(f"Total coins needed (by greedy strategy) = {greedy_count} ({'+'.join(map(str, used_coins))}).")
    return greedy_count

def dp_coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    used_coins = [-1] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] != float('inf'):
                if dp[i] > dp[i - coin] + 1:
                    dp[i] = dp[i - coin] + 1
                    used_coins[i] = coin
    
    return dp[amount] if dp[amount] != float('inf') else -1, used_coins

def find_optimal_combination(coins, amount):
    dp, used_coins = dp_coin_change(coins, amount)
    if dp == -1:
        print("No valid combination found.")
        return dp
    
    print(f"Minimum coins needed (by DP) = {dp} (", end="")
    temp_amount = amount
    first = True
    while temp_amount > 0:
        if not first:
            print("+", end="")
        print(used_coins[temp_amount], end="")
        temp_amount -= used_coins[temp_amount]
        first = False
    print(").")
    return dp

n = int(input("Enter number of denominations: "))
coins = list(map(int, input("Enter denominations: ").split()))
amount = int(input("Enter value: "))

sort_descending(coins)

greedy_count = greedy_coin_change(coins, amount)
dp_count = find_optimal_combination(coins, amount)

if dp_count == -1:
    print("No, greedy strategy is not giving the optimum for this given problem.")
elif greedy_count == dp_count:
    print("Yes, greedy strategy gives the optimum result for this given problem.")
else:
    print("No, greedy strategy is not giving the optimum for this given problem.")
