nums = [2,7, 11, 15]
target = 9

hashmap = {}
for i, n in enumerate(nums):
    if target - n in hashmap:
        return [hashmap[target - n], i]
    else:
        hashmap[n] = i
