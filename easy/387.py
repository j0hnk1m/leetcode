class Solution:
	def firstUniqChar(self, s: str) -> int:
		import collections
		counter, i = dict(collections.Counter(s)), -1

		for k in counter.keys():
			if counter[k] == 1:
				i = s.index(k)
				break
		return i