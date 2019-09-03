class Solution:
	def isPalindrome(self, s: str) -> bool:
		import re
		s = re.compile('[^a-zA-Z0-9]').sub('', s).lower()
		if not s or len(s) == 1:
			return True

		mid = len(s) // 2
		if len(s) % 2 == 0:
			return s[:mid] == s[mid:][::-1]
		return s[:mid] == s[mid + 1:][::-1]
