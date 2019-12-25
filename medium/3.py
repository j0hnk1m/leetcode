s = "abcabcbb"

used = {}
start = 0
end = 0
max_len = 0

while end < len(s):
    if s[end] not in used:
        used[s[end]] = 1
        end += 1
    else:
        del used[s[start]]
        start += 1
    max_len = max(max_len, len(used))

return max_len
