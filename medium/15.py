nums = [-1, 0, 1, 2, -1, -4]

if len(nums) < 3:
    return []

nums.sort()
sols = []
for i in range(len(nums)-2):
    l = i + 1
    r = len(nums) - 1
    if i != 0 and nums[i] == nums[i-1]:
        continue

    while l < r:
        if nums[l] + nums[r] == -nums[i]:
            sols.append([nums[i], nums[l], nums[r]])
            l += 1
            r -= 1
            while l < r and nums[l] == nums[l-1]: l += 1
            while l < r and nums[r] == nums[r+1]: r -= 1
        elif nums[l] + nums[r] < -nums[i]:
            l += 1
        else:
            r -= 1
return sols
