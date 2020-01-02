nums = [3,2,1,0,4]

# recursive - o(2^n) runtime, o(n) space
def canJump(nums, pos):
    if pos == len(nums)-1:
        return True
    maxJump = min(pos+nums[pos], len(nums)-1)
    for i in range(pos+1, maxJump):
        if canJump(nums, i):
            return True
    return False

# memoization - o(n^2) runtime, o(n) space
def canJump(nums, pos):
    if pos in memo:
        return memo[pos]
    elif pos == len(nums)-1:
        memo[pos] = True
    else:
        memo[pos] = False
        maxJump = min(pos+nums[pos], len(nums)-1)
        for i in range(pos+1, maxJump):
            if canJump(nums, i):
                memo[pos] = True
                break
    return memo[pos]

memo = {}
return canJump(nums, 0)

# dp bottom-up - o(n^2) runtime, o(n) space
dp = [False for _ in range(len(nums))]
dp[-1] = True
for i in reversed(range(len(nums))):
    maxJump = min(i+nums[i], len(nums)-1)
    for j in range(i+1, maxJump+1):
        if dp[j]:
            dp[i] = True
            break
return dp[0]

# dp/greedy - o(n) runtime, o(1) space
lastGoodPos = len(nums)-1
for i in reversed(range(len(nums))):
    maxJump = i+nums[i]
    if maxJump >= lastGoodPos:
        lastGoodPos = i
return lastGoodPos == 0
