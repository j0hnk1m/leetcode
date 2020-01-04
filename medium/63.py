obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

# recursive - o(2^mn) runtime, o(mn) space
def uniquePathsWithObstacles(grid, r, c):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 1:
        print(f"{r}, {c}")
        return 0
    elif r == len(grid)-1:
        return uniquePathsWithObstacles(grid, r, c+1)
    elif c == len(grid[0])-1:
        return uniquePathsWithObstacles(grid, r+1, c)
    return 1 + uniquePathsWithObstacles(grid, r, c+1) + uniquePathsWithObstacles(grid, r+1, c)

return uniquePathsWithObstacles(obstacleGrid, 0, 0)

# dp bottom-up - o(mn) runtime, o(mn) space
dp = [[1 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
for c in reversed(range(len(obstacleGrid))):
    for r in reversed(range(len(obstacleGrid[0]))):
