nums = [2,3,2]

# dp bottom-up - o(n) runtime, o(n) space
def rob_(nums):
    if not nums:
        return 0
    elif len(nums) == 1:
        return nums[0]
    dp = [0 for _ in range(len(nums))]
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])
    return dp[-1]

if not nums:
    return 0
elif len(nums) == 1:
    return nums[0]
return max(rob_(nums[:-1]), rob_(nums[1:]))
