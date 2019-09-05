class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curr_sum = nums[0]
        max_sum = nums[0]
        for n in nums[1:]:
            curr_sum = max(curr_sum + n, n)
            max_sum = max(curr_sum, max_sum)
        return max_sum
