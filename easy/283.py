class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for n in nums:
            if n != 0:
                nums[i] = n
                i += 1
        
        for i in range(i, len(nums)):
            nums[i] = 0
