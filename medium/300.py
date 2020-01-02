nums = [9, 1, 3, 8, 4, 5]

# recursive - o(2^n) runtime, o(n^2) space
def lis(nums, submax, i):
    if i == len(nums):
        return 0
    
    skip = lis(nums, submax, i+1)
    if nums[i] > submax:
        include = 1 + lis(nums, nums[i], i+1)
        return max(skip, include)
    return skip

return lis(nums, float('-inf'), 0)

# memoization - o(n^2) runtime, o(n^2) space
def lis(nums, submax, i):
    if (submax, i) in memo:
        return memo[(submax, i)]
    elif i == len(nums):
        return 0
    
    skip = lis(nums, submax, i+1)
    if nums[i] > submax:
        include = 1 + lis(nums, nums[i], i+1)
        memo[(submax, i)] = max(skip, include)
    else:
        memo[(submax, i)] = skip
    return memo[(submax, i)]

memo = {}
return lis(nums, float('-inf'), 0)

# dp bottom-up - o(n^2) runtime, o(n) space
if not nums:
    return 0

dp = [0 for i in range(len(nums))]
dp[0] = 1
for i in range(len(nums)):
    dp[i] = 1
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], 1+dp[j])
return max(dp)
