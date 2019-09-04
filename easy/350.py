class Solution:
	def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
		if not nums1 or not nums2:
			return []
		elif nums1 == nums2:
			return nums1
		else:
			import collections
			counter1 = dict(collections.Counter(nums1))
			counter2 = dict(collections.Counter(nums2))

			com = []
			for k in counter1.keys():
				if k in counter2:
					com.extend([k]*min(counter1[k], counter2[k]))
			return com
