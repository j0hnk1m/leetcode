candidates = [2,3,6,7]
target = 7

def dfs(path, candidates, target, res):
    if target < 0:
        return
    elif target == 0:
        res.append(path)
        return 
    
    for i in range(len(candidates)):
        dfs(path+[candidates[i]], candidates[i:], target-candidates[i], res)

res = []
candidates.sort()
dfs([], candidates, target, res)
return res
