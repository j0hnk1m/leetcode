coins = [1, 2, 5]
amount = 11

# recursive - o(a^c) runtime, o(a) space
def coinChange(coins, amount):
    if amount == 0:
        return 0
    elif amount < 0:
        return float('-inf')
    
    res = -1
    for c in coins:
        subres = 1 + coinChange(coins, amount-c)
        if subres > 0:
            if res == -1:
                res = subres
            else:
                res = min(res, subres)
    return res

# memoization - o(ac) runtime, o(a) space
memo = {}
def coinChange(coins, amount):
    if amount in memo:
        return memo[amount]
    elif amount == 0:
        return 0
    elif amount < 0:
        return float('-inf')
    
    res = -1
    for c in coins:
        subres = 1 + coinChange(coins, amount-c)
        if subres > 0:
            if res == -1:
                res = subres
            else:
                res = min(res, subres)
    memo[amount] = res
    return res

# dp bottom-up - o(ac) runtime, o(a) space
dp = [0] + [float('inf') for _ in range(amount)]
for i in range(1, amount+1):
    for c in coins:
        if i >= c:
            dp[i] = min(dp[i], 1+dp[i-c])

if dp[-1] == float('inf'):
    return -1
return dp[-1]
