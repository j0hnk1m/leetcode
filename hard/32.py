s = ")()())"

# brute force - o(n^3) time, o(1) space
def isValid(sub):
    pairs = {'(': ')'}
    stack = []
    for i in sub:
        if i in pairs:
            stack.append(i)
        else:
            if not stack or i != pairs[stack.pop()]:
                return False
    return not stack

maxlen = 0
for i in range(len(s)):
    for j in range(i, len(s)+1):
        if isValid(s[i:j]):
            maxlen = max(maxlen, len(s[i:j]))
return maxlen

# 