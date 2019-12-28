
# using trienode
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root.children
        for i in word:
            if i not in cur:
                cur[i] = TrieNode()
            prev = cur[i]
            cur = cur[i].children
        prev.end = True
    
    def search(self, word):
        cur = self.root.children
        for i in word:
            if i not in cur:
                return False
            prev = cur[i]
            cur = cur[i].children
        return prev.end
        
    def startsWith(self, prefix):
        cur = self.root.children
        for i in prefix:
            if i not in cur:
                return False
            else:
                cur = cur[i].children
        return True

# without using trienode
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

    def search(self, word):
        trie = self.trie
        for i in word:
            if i not in trie:
                return False
            trie = trie[i]
        return '-' in trie

    def startsWith(self, prefix):
        trie = self.tire
        for i in prefix:
            if i not in trie: 
                return False
            trie = trie[i]
        return True


trie = Trie()
trie.insert("apple")
trie.search("apple")
trie.search("app")
trie.startsWith("app")
trie.insert("app");   
trie.search("app")
