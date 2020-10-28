nums = [5,7,7,8,8,10]
target = 8

if not nums:
    return [-1, -1]

start = end = -1

# find the left-most target
l = 0
r = len(nums) - 1
while l <= r:
    mid = l+(r-l)//2
    if nums[mid] == target:
        start = mid
        r = mid - 1
    elif nums[mid] > target:
        r = mid - 1
    else:
        l = mid + 1
        

# find the right-most target
l = 0
r = len(nums) - 1
while l <= r:
    mid = l+(r-l)//2
    if nums[mid] == target:
        end = mid
        l = mid + 1
    elif nums[mid] > target:
        r = mid - 1
    else:
        l = mid + 1

return [start, end]