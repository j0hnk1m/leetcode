matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

# additional memory - o(mn) runtime, o(m+n) space
rows = {}
cols = {}
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] == 0:
            rows[r] = 1
            cols[c] = 1
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if r in rows or c in cols:
            matrix[r][c] = 0

# in-place - o(mn(m+n)) runtime, o(1) space
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] == 0:
            for col in range(len(matrix[r])):
                if matrix[r][col] != 0:
                    matrix[r][col] = float('inf')
            for row in range(len(matrix)):
                if matrix[row][c] != 0:
                    matrix[row][c] = float('inf')
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] == float('inf'):
            matrix[r][c] = 0
