nums = [4,1,2,1,2]

new = {}
for i in nums:
    try:
        new.pop(i)
    except KeyError:
        new[i] = 1
return new.popitem()[0]
            