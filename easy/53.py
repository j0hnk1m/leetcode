nums = [-2,1,-3,4,-1,2,1,-5,4]

if not nums:
    return 0

curr_sum = nums[0]
max_sum = nums[0]
for n in nums[1:]:
    curr_sum = max(curr_sum + n, n)
    max_sum = max(curr_sum, max_sum)
return max_sum
