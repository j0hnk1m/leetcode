class Solution:
	def reverseVowels(self, s: str) -> str:
		vowels = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1}
		stack = []
		new_str = ""

		for i in s:
			if i in vowels:
				stack.append(i)
		for i in s:
			if i in vowels:
				new_str += stack.pop()
			else:
				new_str += i
		return new_str
