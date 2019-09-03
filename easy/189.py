class Solution:
	def rotate(self, nums: List[int], k: int) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		# # 1. using extra array and modulus reassignment
		new = [0 for i in range(len(nums))]
		for i, n in enumerate(nums):
			new[(i + k) % len(nums)] = nums[i]
		nums[:] = new

		# # 2. in-place by storing previous value
		# n_assignments = 0
		# idx = 0
		# tmp1, tmp2 = None, None
		# while n_assignments < len(nums):
		# 	if n_assignments == 0:
		# 		tmp1 = nums[idx]
		# 	else:
		# 		tmp1 = tmp2
		#
		# 	tmp2 = nums[(idx + k) % len(nums)]
		# 	nums[(idx + k) % len(nums)] = tmp1
		# 	idx = (idx+k)%len(nums)
		# 	n_assignments += 1


		# # 3. reversing parts of array
		# nums[:] = nums[::-1]
		# nums[:k%len(nums)] = nums[:k%len(nums)][::-1]
		# nums[k%len(nums):] = nums[k%len(nums):][::-1]
