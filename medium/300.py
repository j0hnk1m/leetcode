nums = [10,9,2,5,3,7,101,18]

# dp bottom-up
if not nums:
    return 0

dp = [0 for i in range(len(nums))]
dp[0] = 1
for i in range(len(nums)):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j]+1)
    dp[i] = max(1, dp[i])
return max(dp)
