nums = [4, 5, 1, 8, 2]

if not nums:
    return []

res = [1 for i in range(len(nums))]
for i in range(1, len(nums)):
    res[i] = res[i-1] * nums[i-1]

prod = 1
for i in reversed(range(len(nums))):
    res[i] *= prod
    prod *= nums[i]

return res
