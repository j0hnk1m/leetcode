nums = [0,1,0,3,12]

i = 0
for n in nums:
    if n != 0:
        nums[i] = n
        i += 1

for i in range(i, len(nums)):
    nums[i] = 0
