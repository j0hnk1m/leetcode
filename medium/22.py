n = 3

# dfs recursive - o((2n-2)!!) time, o() space
def dfs(seq, pairs):
    if pairs == 0:
        if seq and seq not in res:
            res[seq] = 1
        return
    elif not seq:
        dfs('()', pairs-1)
        return

    for i in range(len(seq)):
        dfs(seq[:i] + '()' + seq[i:], pairs-1)

res = {}
dfs('', n)
return res.keys()


# dfs recursive with backtracking/memoization - o(n!) time, o(n!) space
def dfs(seq, pairs):
    if pairs == 0:
        if seq and seq not in res:
            res[seq] = 1
        return
    elif not seq:
        dfs('()', pairs-1)
        return
    
    if seq in visited:
        return
    
    visited[seq] = 1
    for i in range(len(seq)):
        dfs(seq[:i] + '()' + seq[i:], pairs-1)

res = {}
visited = {}
dfs('', n)
return res.keys()
