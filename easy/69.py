class Solution:
	def mySqrt(self, x: int) -> int:
		if x == 0 or x == 1:
			return x

		start = 1
		end = x
		while start <= end:
			mid = (start + end) // 2

			if mid ** 2 == x:
				return mid
			elif mid ** 2 < x:
				start = mid + 1
				ans = mid
			else:
				end = mid - 1
		return ans
