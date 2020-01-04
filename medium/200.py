grid = [
    list('11110'),
    list('11010'),
    list('11000'),
    list('00000')
]

# recursive dfs - o(n) runtime, o(1) space
islands = 0
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == '1':
            dfs(grid, r, c)
            islands += 1
return islands

def dfs(grid, r, c):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[r]) or grid[r][c] != '1':
        return
    grid[r][c] = '#'
    dfs(grid, r+1, c)
    dfs(grid, r-1, c)
    dfs(grid, r, c+1)
    dfs(grid, r, c-1)

# iterative bfs - o(n) runtime, o(1) space
islands = 0
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == '1':
            islands += 1
            q = [(r, c)]
            for rr, cc in q:
                if rr >= 0 and cc >= 0 and rr < len(grid) and cc < len(grid[r]) and grid[rr][cc] == '1':
                    grid[rr][cc] = '#'
                    q.extend([(rr+1, cc), (rr-1, cc), (rr, cc-1), (rr, cc+1)])
return islands
