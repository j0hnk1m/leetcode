class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        new = {}
        for i in nums:
            try:
                new.pop(i)
            except KeyError:
                new[i] = 1
        return new.popitem()[0]
            