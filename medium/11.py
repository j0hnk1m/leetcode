height = [1,2,4,3]

# brute force
max_area = 0
for i, h1 in enumerate(height):
    for j, h2 in enumerate(height[i:]):
        cur_area = min(h1, h2) * j
        max_area = max(cur_area, max_area)

return max_area

# optimized
max_area = 0
start = 0
end = len(height) - 1
while end > start:
    curr_area = min(height[start], height[end]) * (end - start)
    max_area = max(curr_area, max_area)
    if height[start] < height[end]:
        start += 1
    else:
        end -= 1

return max_area
