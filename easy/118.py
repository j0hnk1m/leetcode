class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return

        pascal = [[0, 1, 0]]
        for i in range(numRows - 1):
            prevrow = pascal[-1]
            newrow = [0]

            for h in range(len(prevrow) - 1):
                newrow.append(prevrow[h + 1] + prevrow[h])
            newrow.append(0)
            pascal[-1][:] = pascal[-1][1:-1]
            pascal.append(newrow)

        pascal[-1][:] = pascal[-1][1:-1]
        return pascal
