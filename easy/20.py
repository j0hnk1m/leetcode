s = '{[]}'

stack = []
brackets = {"{": "}", "(": ")", "[": "]"}
for i in s:
	if i in brackets:
		stack.append(i)
	else:
		if not stack or brackets[stack.pop()] != i:
			return False

return not stack
