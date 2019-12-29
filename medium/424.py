s = "AABABBA"
k = 1

# sliding window
import collections
max_len = max_count = left = right = 0
counter = collections.Counter()
for right in range(len(s)):
    counter[s[right]] += 1
    max_count = max(max_count, counter[s[right]])
    if (right-left+1)-max_count > k:
        counter[s[left]] -= 1
        left += 1
    max_len = max(max_len, right-left+1)
return max_len
