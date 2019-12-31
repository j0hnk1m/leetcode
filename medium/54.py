matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

# keep rotating matrix and deleting top row - o(n) runtime, o(n) space
spiral = []
while matrix:
    for i in matrix[0]:
        spiral.append(i)
    del matrix[0]
    matrix = list(zip(*matrix))[::-1]
return spiral

# layer-by-layer - o(n) runtime, o(n) space
def spiral(r1, r2, c1, c2):
    top = matrix[r1][c1:c2+1]
    right = [matrix[row][c2] for row in range(r1+1, r2+1)]
    bottom = matrix[r2][c1+1:c2][::-1] if r1 < r2 else []
    left = [matrix[row][c1] for row in range(r1+1, r2+1)][::-1] if c1 < c2 else []
    return top + right + bottom + left
    
if not matrix:
    return []
res = []
r1 = c1 = 0
r2 = len(matrix) - 1
c2 = len(matrix[0]) - 1
while r1 <= r2 and c1 <= c2:
    res.extend(spiral(r1, r2, c1, c2))
    r1 += 1; c1 += 1
    r2 -= 1; c2 -= 1
return res