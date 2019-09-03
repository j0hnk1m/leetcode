class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		if len(s) != len(t):
			return False

		used = {}
		for i in s:
			if i not in used:
				used[i] = 1
			else:
				used[i] += 1
		for i in t:
			if i not in used:
				return False
			else:
				used[i] -= 1

		for v in used.values():
			if v != 0:
				return False
		return True
