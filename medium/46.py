nums = [1,2,3]

# top-down memoization dfs - o(n!) time, o(n!) space
memo = {}
def dfs(nums, nums_left):
	if not nums_left:
		memo[tuple(nums)] = nums
		return
	elif not nums:
		dfs([nums_left[0]], nums_left[1:])
		return
	
	for i in range(len(nums)+1):
		dfs(nums[:i] + [nums_left[0]] + nums[i:], nums_left[1:])

dfs([], nums)
return list(memo.values())
