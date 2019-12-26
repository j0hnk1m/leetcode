nums = [4,5,6,7,0,1,2]
target = 0

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

start = l
l = 0
r = len(nums) - 1
if target >= nums[start] and target <= nums[r]:
    l = start
else:
    r = start
while l <= r:
    mid = l + (r-l)//2
    if target == nums[mid]:
        return mid
    elif target > nums[mid]:
        l = mid + 1
    else:
        r = mid - 1
return -1