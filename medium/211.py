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
        def find(word, trie):
            if type(trie) is bool:
                return False
            elif not word:
                return '-' in trie
            
            char, word = word[0], word[1:]
            if char != '.':
                return char in trie and find(word, trie[char])
            return any(find(word, i) for i in trie.values() if i)
        
        return find(word, self.trie)

d = WordDictionary()
d.addWord("bad")
d.addWord("dad")
d.addWord("mad")
d.search("pad")  # false
d.search("bad")  # true
d.search(".ad")  # true
d.search("b..")  # true
d.search('....')