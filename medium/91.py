s = "226"

# recursive - o(2^n) runtime, o(n) space
def numDecodings(s):
    if not s:
        return 0
    elif len(s) == 1:
        return 1 if int(s) >= 1 else 0
    return numDecodings(s[0]) + numDecodings(s[1:])

# memoization - o(n) runtime, o(n) space
def numDecodings(s):
    if s in memo:
        return memo[s]
    elif not s:
        memo[s] = 0
    elif len(s) == 1:
        memo[s] = 1 if int(s) >= 1 else 0
    else:
        memo[s] = numDecodings(s[0]) + numDecodings(s[1:])
    return memo[s]

memo = {}
return numDecodings(s)

# dp bottom-up - o(n) runtime, o(n) space
dp = [0 for _ in range(len(s)+1)]
dp[0] = 1
dp[1] = 0 if s[0] == '0' else 1
for i in range(2, len(s)+1):
    if int(s[i-1:i]) >= 1:
        dp[i] += dp[i-1]
    if int(s[i-2:i]) >= 10 and int(s[i-2:i]) <= 26:
        dp[i] += dp[i-2]
return dp[-1]
