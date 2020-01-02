s = "leetcode"
wordDict = ["leet", "code"]

# recursive - o(2^n) runtime, o(n) space
wordDict = {k: 1 for k in wordDict}
def wb(s, wordDict):
    if not s: 
        return True
    res = []
    for i in range(1, len(s)+1):
        res.append(s[:i] in wordDict and wb(s[i:], wordDict))
    return any(res)

# memoization - o(n^2) runtime, o(n) space
def wb(s, wordDict):
    if s in memo:
        return memo[s]
    elif not s: 
        return True
    res = []
    for i in range(1, len(s)+1):
        res.append(s[:i] in wordDict and wb(s[i:], wordDict))
    memo[s] = any(res)
    return memo[s]

memo = {}
wordDict = {k: 1 for k in wordDict}
return wb(s, wordDict)

# dp - o(n^2) runtime, o(n) space
dp = [False for _ in range(len(s))]
wordDict = {k: 1 for k in wordDict}
for i in range(len(s)):
    if s[:i+1] in wordDict:
        dp[i] = True
    else:
        for j in range(i):
            if dp[j] and s[j+1:i+1] in wordDict:
                dp[i] = True
                break
return dp[-1]
