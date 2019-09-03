class Solution:
    def romanToInt(self, s: str) -> int:
		# mappings = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
		# out = 0
		# for i in range(len(s) - 1):
		# 	if mappings[s[i]] >= mappings[s[i + 1]]:
		# 		out += mappings[s[i]]
		# 	else:
		# 		out-= mappings[s[i]]
		#
		# out += mappings[s[len(s) - 1]]
		#
		# return out
		mappings = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
		   'D': 500, 'M': 1000}
		out = 0
		cooldown = False
		for h, i in enumerate(s):
			if not cooldown:
				if h == len(s) - 1:
					out += mappings[i]
				elif i + s[h + 1] in mappings:
					out += mappings[i + s[h + 1]]
					cooldown = True
				else:
					out += mappings[i]
			else:
				cooldown = False
		return out

