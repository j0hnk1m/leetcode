nums = [10,9,2,5,3,7,101,18]

if not nums:
    return 0

dp = [0 for i in range(len(nums))]
dp[0] = 1
lis = 1
for i in range(len(nums)):
    max_val = 0
    for j in range(i):
        if nums[j] < nums[i]:
            max_val = max(max_val, dp[j])
    dp[i] = max_val + 1
    lis = max(lis, dp[i])

return lis 
