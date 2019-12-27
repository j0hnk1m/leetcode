nums = [3,4,5,1,2] 

# binary search - o(logn) runtime, o(1) space
if not nums:
    return -1

l = 0
r = len(nums) - 1
while l < r:
    mid = l + (r-l)//2
    if nums[mid] > nums[r]:
        l = mid + 1
    else:
        r = mid

return nums[l]