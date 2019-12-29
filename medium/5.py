s = 'babbad'

def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1
    

start = end = 0
for i in range(len(s)):
    len1 = expand(s, i, i)
    len2 = expand(s, i, i+1)
    len3 = max(len1, len2)
    
    if len3 > end - start:
        start = i - (len3-1)// 2
        end = start + len3 - 1
return s[start:end+1]
