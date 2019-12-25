nums1 = [4,9,5]
nums2 = [9,4,9,8,4]


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
