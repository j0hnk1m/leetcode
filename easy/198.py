nums = [2,7,9,3,1]

# recursive - o(2^n) runtime, o(n) space
def rob(nums):
    if not nums:
        return 0
    return max(nums[0] + rob(nums[2:]), rob(nums[1:]))

# memoization - o(n) runtime, o(n) space
def rob(nums, i):
    if i in memo:
        return memo[i]
    elif i < 0:
        return 0
    memo[i] = max(nums[i] + rob(nums, i-2), rob(nums, i-1))
    return memo[i]

memo = {}
return rob(nums, len(nums) - 1)

# dp bottom-up - o(n) runtime, o(n) space
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
