digits = "23"

keys = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}


# recursive - o(3^n * 4^m) time, o((m+n)*(3^n * 4^m)) space
def dfs(comb, digs):
    if len(digs) == 0:
        res.append(comb)
    else:
        for i in keys[digs[0]]:
            dfs(comb+i, digs[1:])

res = []
if digits:
    dfs('', digits)
return res


# iterative - o(3^n * 4^m) time, o((m+n)*(3^n * 4^m)) space
if not digits:
    return []

res = ['']
for i in range(len(digits)):
    new_res = []
    for letter in keys[digits[i]]:
        for r in res:
            new_res.append(r+letter)
    res = new_res
return res