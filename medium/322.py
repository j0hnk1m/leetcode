coins = [1, 2, 5]
amount = 11

dp = [0] + [float('inf') for i in range(amount+1)]

for coin in coins:
    for i in range(coin, amount+1):
        dp[i] = min(dp[i], dp[i-coin]+1)

if dp[-1] != float('inf'):
    return dp[-1]
return -1
