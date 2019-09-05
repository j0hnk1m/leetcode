class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = None
        i = 0
        while i < len(nums):
            if nums[i] == cur:
                del nums[i]
            else:
                cur = nums[i]
                i += 1
        return len(nums)
