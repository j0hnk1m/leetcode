nums = [1,2,3,4,5,6,7]
k = 3

# # 1. using extra array and modulus reassignment
new = [0 for i in range(len(nums))]
for i, n in enumerate(nums):
	new[(i + k) % len(nums)] = nums[i]
nums[:] = new

# # 2. in-place cyclic replacement
n_assignments = 0
used_idx = {}
idx = 0
tmp1, tmp2 = None, None
while n_assignments < len(nums):
	if idx in used_idx:
		idx += 1
		tmp1 = nums[idx]
	else:
		used_idx[idx] = 1

		if n_assignments == 0:
			tmp1 = nums[idx]

		tmp2 = nums[(idx + k) % len(nums)]
		nums[(idx + k) % len(nums)] = tmp1
		tmp1 = tmp2
		idx = (idx+k)%len(nums)
		n_assignments += 1


# # 3. reversing parts of array
nums[:] = nums[::-1]
nums[:k%len(nums)] = nums[:k%len(nums)][::-1]
nums[k%len(nums):] = nums[k%len(nums):][::-1]
