s = "leetcode"
wordDict = ["leet", "code"]

# recursive
wordDict = {k: 1 for k in wordDict}
def wordBreak(s, wordDict):
    if not s: 
        return True
    res = []
    for i in range(1, len(s)+1):
        res.append(s[:i] in wordDict and wordBreak(s[i:], wordDict))
    return any(res)

# dp