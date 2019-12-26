matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

for i in range(len(matrix)):
    for j in range(i, len(matrix)):
        tmp = matrix[i][j]
        matrix[i][j] = matrix[j][i]
        matrix[j][i] = tmp

for i in range(len(matrix)):
    # matrix[i].reverse()
    l = 0
    r = len(matrix[i]) - 1
    while l <= r:
        tmp = matrix[i][l]
        matrix[i][l] = matrix[i][r]
        matrix[i][r] = tmp
        l += 1
        r -= 1

