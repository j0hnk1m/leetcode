nums = [-2, 3, -2, 4]

if not nums:
    return 0

res = max_prod = min_prod = nums[0]
for i in nums[1:]:
    tmp = max_prod
    max_prod = max(i, max(max_prod*i, min_prod*i))
    min_prod = min(i, min(tmp*i, min_prod*i))
    res = max(res, max_prod)

return res
