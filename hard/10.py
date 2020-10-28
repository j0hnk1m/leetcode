s = "aab"
p = "c*a*b"

# recursive - o(m+n choose n) runtime, o(2^(m+n))
def isMatch(self, s: str, p: str) -> bool:
    if not p:
        return not s
    
    first_match = bool(s) and (p[0] == s[0] or p[0] == '.')
    if len(p) >= 2 and p[1] == '*':
        return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
    else:
        return first_match and self.isMatch(s[1:], p[1:])

# top-down recursive memoization - o(mn) runtime, o(mn) space
memo = {}
def dp(i, j):
    if (i, j) not in memo:
        if j == len(p):
            res = (i == len(s))
        else:
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
            if j+1 < len(p) and p[j+1] == '*':
                res = dp(i, j+2) or (first_match and dp(i+1, j))
            else:
                res = first_match and dp(i+1, j+1)
        memo[(i, j)] = res
    return memo[(i, j)]

return dp(0, 0)

# bottom-up iterative dp - o(mn) runtime, o(mn) space
dp = [[False for j in range(len(p)+1)] for i in range(len(s)+1)]
dp[-1][-1] = True
for i in range(len(s)-1, -1, -1):
    for j in range(len(p)-1, -1, -1):
        first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
        if j+1 < len(p) and p[j+1] == '*':
            dp[i][j] = dp[i][j+2] or (first_match and dp[i+1][j])
        else:
            dp[i][j] = first_match and dp[i+1][j+1]
return dp[0][0]