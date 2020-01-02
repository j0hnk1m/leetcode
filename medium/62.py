m = 3
n = 2

# recursive - o(2^mn) runtime, o(mn) space
def uniquePaths(m, n):
    if m == 1 and n == 1:
        return 1
    elif m == 1:
        return uniquePaths(m, n-1)
    elif n == 1:
        return uniquePaths(m-1, n)
    return uniquePaths(m, n-1) + uniquePaths(m-1, n)

# memoization - o(mn) runtime, o(mn) space
def uniquePaths(m, n):
    if (m, n) in memo:
        return memo[(m, n)]
    elif m == 1 and n == 1:
        memo[(m, n)] = 1
    elif m == 1:
        memo[(m, n)] = uniquePaths(m, n-1)
    elif n == 1:
        memo[(m, n)] = uniquePaths(m-1, n)
    else:
        memo[(m, n)] = uniquePaths(m, n-1) + uniquePaths(m-1, n)
    return memo[(m, n)]

memo = {}
return uniquePaths(m, n)

# dp bottom-up - o(mn) runtime, o(mn) space
dp = [[1 for i in range(m)] for j in range(n)]
for r in reversed(range(n-1)):
    for c in reversed(range(m-1)):
        dp[r][c] = dp[r+1][c] + dp[r][c+1]
return dp[0][0]
