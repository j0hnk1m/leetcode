s = "aaa"

def expand(l, r, s):
    while l >= 0 and r < len(s) and l <= r and s[l] == s[r]:
        l -= 1
        r += 1
    return r-l-1

count = 0
for i in range(len(s)):
    count += 1
    len1 = expand(i, i, s)
    len2 = expand(i, i+1, s)
    if len1 > 1:
        count += len1//2
    if len2 > 1:
        count += len2//2
return count

