obstacleGrid = [
    [0,0],
    [1,1],
    [0,0]
]

# recursive - o(2^mn) runtime, o(mn) space
def uniquePathsWithObstacles(grid, r, c):
    if grid[r][c] == 1:
        return 0
    elif r == len(grid)-1 and c == len(grid[0])-1:
        return 1
    elif r == len(grid)-1:
        return uniquePathsWithObstacles(grid, r, c+1)
    elif c == len(grid[0])-1:
        return uniquePathsWithObstacles(grid, r+1, c)
    return uniquePathsWithObstacles(grid, r+1, c) + uniquePathsWithObstacles(grid, r, c+1)

return uniquePathsWithObstacles(obstacleGrid, 0, 0)

# memoization - o(mn) runtime, o(mn) space
def uniquePathsWithObstacles(grid, r, c):
    if (r, c) in memo:
        return memo[(r, c)]
    elif grid[r][c] == 1:
        memo[(r, c)] = 0
    elif r == len(grid)-1 and c == len(grid[0])-1:
        memo[(r, c)] = 1
    elif r == len(grid)-1:
        memo[(r, c)] = uniquePathsWithObstacles(grid, r, c+1)
    elif c == len(grid[0])-1:
        memo[(r, c)] = uniquePathsWithObstacles(grid, r+1, c)
    else:
        memo[(r, c)] = uniquePathsWithObstacles(grid, r+1, c) + uniquePathsWithObstacles(grid, r, c+1)
    return memo[(r, c)]

memo = {}
return uniquePathsWithObstacles(obstacleGrid, 0, 0)

# dp bottom-up - o(mn) runtime, o(mn) space
if not obstacleGrid or obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
    return 0

dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
dp[0][0] = 1
for r in range(1, len(obstacleGrid)):
    dp[r][0] = dp[r-1][0] * (1 - obstacleGrid[r][0])
for c in range(1, len(obstacleGrid[0])):
    dp[0][c] = dp[0][c-1] * (1 - obstacleGrid[0][c])

for r in range(1, len(obstacleGrid)):
    for c in range(1, len(obstacleGrid[0])):
        dp[r][c] = (dp[r][c-1] + dp[r-1][c]) * (1 - obstacleGrid[r][c])
return dp[-1][-1]
