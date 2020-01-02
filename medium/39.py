candidates = [2,3,6,7]
target = 7

# recursive/backtracking - o(t^n) runtime, o(t) space
def cs(candidates, target, path):
    if target == 0:
        res.append(path)
        return
    for i in range(len(candidates)):
        if target >= i:
            cs(candidates[i:], target-candidates[i], path+[candidates[i]])

res = []
candidates.sort()
cs(candidates, target, [])
return res
