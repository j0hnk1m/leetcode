text1 = "bsbininm"
text2 = "jmjkbkjkv"

# recursive - o(2^(m+n)) runtime, o(m+n) space
def longestCommonSubsequence(text1, text2):
    if not text1 or not text2:
        return 0
    elif text1[0] == text2[0]:
        return 1 + longestCommonSubsequence(text1[1:], text2[1:])
    return max(longestCommonSubsequence(text1, text2[1:]), longestCommonSubsequence(text1[1:], text2))

# memoization - o(mn) runtine, o(mn) space   
def lcs(t1, t2):
    if (t1, t2) in memo:
        res = memo[(t1, t2)]
    elif not t1 or not t2:
        res = 0
    elif t1[0] == t2[0]:
        res = 1 + lcs(t1[1:], t2[1:])
    
    res = max(lcs(t1[1:], t2), lcs(t1, t2[1:]))
    memo[(t1, t2)] = res
    return res

memo = {}
lcs(text1, text2)
return memo[(text1, text2)]

# dp bottom-up
dp = [[0 for c in range(len(text1)+1)] for r in range(len(text2)+1)]
for r in range(1, len(dp)):
    for c in range(1, len(dp[r])):
        if text1[c-1] == text2[r-1]:
            dp[r][c] = dp[r-1][c-1] + 1
        else:
            dp[r][c] = max(dp[r-1][c], dp[r][c-1])
return dp[-1][-1]
