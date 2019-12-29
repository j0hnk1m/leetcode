s = "ABAACBAB"
t = "ABC"

# sliding window - o(s+t) runtime, o(s+t) space
if not t or not s:
    return ''

import collections
tchars = collections.Counter(t)
need = len(tchars)  # number of letters we need from t
used = collections.Counter()  # dict of current chars in window
res = (float('inf'), 0, 0)
l = r = have = 0
while r < len(s):
    used[s[r]] += 1
    if s[r] in tchars and used[s[r]] == tchars[s[r]]:
        have += 1

    while l <= r and have == need:  # contract from left
        if r-l+1 < res[0]:
            res = (r-l+1, l, r)
        used[s[l]] -= 1
        if s[l] in tchars and tchars[s[l]] > used[s[l]]:
            have -= 1
        l += 1
    r += 1

if res[0] == float('inf'):
    return ''
return s[res[1]:res[2]+1]
