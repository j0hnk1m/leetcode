board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        trie = self.trie
        for i in word:
            if i not in trie: 
                trie[i] = {}
            trie = trie[i]
        trie['-'] = True

def dfs(board, i, j, trie, pre):
    print(trie)
    print(pre)
    print()
    if '-' in trie and trie['-']:
        found.append(pre)
        trie['-'] = False
        return
    elif i < 0 or j < 0 or i >= len(board) or j >= len(board[i]):
        return
    if board[i][j] in trie and (i, j) not in visited:
        visited[(i, j)] = 1
        dfs(board, i+1, j, trie[board[i][j]].trie, pre+board[i][j])
        dfs(board, i-1, j, trie[board[i][j]].trie, pre+board[i][j])
        dfs(board, i, j+1, trie[board[i][j]].trie, pre+board[i][j])
        dfs(board, i, j-1, trie[board[i][j]].trie, pre+board[i][j])
        del visited[(i, j)]

trie = Trie()
for word in words:
    trie.insert(word)
found = []
visited = {}
for i in range(len(board)):
    for j in range(len(board[i])):
        dfs(board, i, j, trie.trie, '')
return found