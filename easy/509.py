N = 2

# recursive - o(2^n) runtime, o(n) space
def fib(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    return fib(N-1) + fib(N-2)

# memoization - o(n) runtime, o(n) space
def fib_(N):
    if N in memo:
        return memo[N]
    elif N == 0:
        return 0
    elif N == 1:
        return 1
    
    memo[N] = fib_(N-1) + fib_(N-2)
    return memo[N]

memo = {}
return fib_(N)

# dp bottom-up - o(n) runtime, o(n) space
dp = {0: 0, 1: 1}
if N < 2:
    return dp[N]

for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]
return dp[N]
