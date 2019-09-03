class Solution:
	def containsDuplicate(self, nums: List[int]) -> bool:
		# if not nums or len(nums) == 1:
		# 	return False
		#
		# new = {}
		# for i in nums:
		# 	if i in new:
		# 		return True
		# 	else:
		# 		new[i] = 1
		# return False

		if len(set(nums)) < len(nums):
			return True
		return False
