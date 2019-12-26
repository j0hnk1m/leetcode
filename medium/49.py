strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# using sort to check anagrams - o(nklogk) runtime, o(nk) space
import collections as c
anagrams = c.defaultdict(list)
for i in strs:
    anagrams[tuple(sorted(i))].append(i)
return anagrams.values()

# using hashmap to check anagrams - o(nk) runtime, o(nk) space
import collections as c
anagrams = c.defaultdict(list)
for i in strs:
    letters = [0 for i in range(26)]
    for char in i:
        letters[ord(char)-ord('a')] += 1
    anagrams[tuple(letters)].append(i)
return anagrams.values()
