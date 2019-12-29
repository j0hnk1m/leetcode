board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"

# iterative dfs
visited = {}
def exist(board, word: str) -> bool:
    for r in range(len(board)):
        for c in range(len(board[r])):
            if dfs(board, r, c, word):
                return True
    return False

def dfs(board, r, c, word):
    if not word:
        return True
    elif r < 0 or r >= len(board) or c < 0 or c >= len(board[r]) or word[0] != board[r][c] or (r, c) in visited:
        return False
    
    visited[(r, c)] = 1
    res = dfs(board, r+1, c, word[1:]) or dfs(board, r-1, c, word[1:]) or dfs(board, r, c+1, word[1:]) or dfs(board, r, c-1, word[1:])
    if not res:
        del visited[(r, c)]
    return res
    