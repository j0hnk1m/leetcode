class Solution:
	def plusOne(self, digits: List[int]) -> List[int]:
		if not digits:
			return

		rev = digits[::-1]
		for i, r in enumerate(rev):
			if r == 9:
				rev[i] = 0
				if i == len(rev) - 1:
					rev.append(1)
					break
			else:
				rev[i] += 1
				break

		return rev[::-1]
