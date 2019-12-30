text1 = "abcde"
text2 = "ace" 

# recursive - o(2^(m+n)) runtime, o(m+n) space
def longestCommonSubsequence(text1, text2):
    if not text1 or not text2:
        return 0
    elif text1[0] == text2[0]:
        return 1 + longestCommonSubsequence(text1[1:], text2[1:])
    return max(longestCommonSubsequence(text1, text2[1:]), longestCommonSubsequence(text1[1:], text2))

# recursive w/ memoization - o(mn) runtine, o(mn) space
def longestCommonSubsequence(text1, text2):
    memo = {}
    lcs(text1, text2)
    return memo[(text1, text2)]

def lcs(t1, t2):
    if not t1 or not t2:
        res = 0
    elif (t1, t2) in memo:
        res = memo[(t1, t2)]
    elif t1[0] == t2[0]:
        res = 1 + lcs(t1[1:], t2[1:])
    else:
        res = max(lcs(t1[1:], t2), lcs(t1, t2[1:]))
    
    memo[(t1, t2)] = res
    return res

