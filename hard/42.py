height = [0,1,0,2,1,0,1,3,2,1,2,1]

# brute force - o(n^2) runtime, o(1) space
res = 0
for i in range(len(height)-1):
    max_left = max_right = 0
    for j in range(i):
        max_left = max(max_left, height[j])
    for j in range(i+1, len(height)):
        max_right = max(max_right, height[j])
    res += max(0, min(max_left, max_right) - height[i])
return res

# dp - o(n) runtime, o(n) space
dp_left = {0: 0}
for i in range(1, len(height)-1):
    dp_left[i] = max(height[i-1], dp_left[i-1])

dp_right = {len(height)-1: 0}
for i in reversed(range(len(height)-1)):
    dp_right[i] = max(height[i+1], dp_right[i+1])

res = 0
for i in range(len(height)-1):
    res += max(0, min(dp_left[i], dp_right[i]) - height[i])
return res

# two pointers - o(n) runtime, o(1) space
res = 0
l = 0
r = len(height) - 1
max_left = max_right = 0
while l < r:
    if height[l] < height[r]:
        max_left = max(max_left, height[l])
        res += max_left - height[l]
        l += 1
    else:
        max_right = max(max_right, height[r])
        res += max_right - height[r]
        r -= 1
return res
