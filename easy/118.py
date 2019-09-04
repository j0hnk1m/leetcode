class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return

        pascal = [[1]]
        for i in range(numRows - 1):
            prevrow = pascal[-1]
            newrow = [1]

            for h in range(len(prevrow) - 1):
                newrow.append(prevrow[h + 1] + prevrow[h])
            newrow.append(1)
            pascal.append(newrow)

        return pascal
