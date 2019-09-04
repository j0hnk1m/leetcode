class Solution:
    def isHappy(self, n: int) -> bool:
        cycle = {}
        while n not in cycle:
            cycle[n] = 1
            n = str(n)
            sum_digits = 0
            for i in n:
                sum_digits += int(i) ** 2

            if sum_digits == 1:
                return True
            n = sum_digits
        return False
