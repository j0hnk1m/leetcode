nums = [1, 2, 3]
target = 4

# recursive - o(t^n) runtime, o(t) space
def combinationSum4(nums, target):
    if target == 0:
        return 1
    res = 0
    for i in nums:
        if target >= i:
            res += combinationSum4(nums, target-i)
    return res

# memoization - o(tn) runtime, o(t) space
def cs4(nums, target):
    if target in memo:
        return memo[target]
    elif target == 0:
        return 1
    res = 0
    for i in nums:
        if target >= i:
            res += cs4(nums, target-i)
    memo[target] = res
    return memo[target]

memo = {}
return cs4(nums, target)

# dp bottom-up - o(tn) runtime, o(t) space
dp = {0: 1}
for i in range(1, target+1):
    dp[i] = 0
    for n in nums:
        if i >= n:
            dp[i] += dp[i-n]
return dp[target]
