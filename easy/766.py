class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        prev = None
        for i in matrix:
            if prev:
                if i[1:] != prev:
                    return False
            prev = i[:-1]
        return True
