class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        trie = self.trie
        for i in word:
            if i not in trie:
                trie[i] = {}
            trie = trie[i]
        trie['-'] = True
    
    def search(self, word: str) -> bool:
        def helper(t, w):
            for h, i in enumerate(w):
                if i not in t:
                    if i == '.':
                        if '-' in t:
                            return False
                        else:
                            if any(helper(t, k+w[h+1:]) for k in t.keys()):
                                return True
                    else:
                        return False
                else:
                    t = t[i]
            if '-' in t:
                return t['-']
            return False
        
        trie = self.trie
        return helper(trie, word)

d = WordDictionary()
d.addWord("bad")
d.addWord("dad")
d.addWord("mad")
d.search("pad")  # false
d.search("bad")  # true
d.search(".ad")  # true
d.search("b..")  # true

d.search("....")  # should be false...
