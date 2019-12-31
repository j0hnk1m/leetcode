coins = [1, 2, 5]
amount = 11

# recursive (doesn't work for edge cases)
def coinChange(coins, amount):
    if amount == 0:
        return 0
    res = []
    for c in coins:
        if amount-c >= 0:
            res.append(1 + coinChange(coins, amount-c))
    return min(res)

# dp bottom-up - o(ac) runtime, o(a) space
dp = [0] + [float('inf') for i in range(amount+1)]
for coin in coins:
    for i in range(coin, amount+1):
        dp[i] = min(dp[i], dp[i-coin]+1)

if dp[-1] != float('inf'):
    return dp[-1]
return -1