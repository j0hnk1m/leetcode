n = 3

# recursive - o(2^n) runtime, o(n) space
def climbStairs(n):
    if n == 0 or n == 1:
        return 1
    return climbStairs(n-1) + climbStairs(n-2)

# recursive w/ memoization - o(n) runtime, o(n) space
def climbStairs(n):
    memo = {0: 1, 1: 1}
    res = helper(n, memo)
    return res
    
def helper(n, memo):
    if n not in memo:
        memo[n] = helper(n-1, memo) + helper(n-2, memo)
    return memo[n]

# dp - o(n) runtime, o(n) space
dp = {0: 1, 1: 1}
if n >= 2:
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
return dp[n]
