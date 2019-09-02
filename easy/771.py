class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        if not J or not S:
            return len(S)
        
        hashmap = {}
        for i in J:
            hashmap[i] = 0
        
        jewels = 0
        for i in S:
            if i in hashmap:
                jewels +=1
                
        return jewels
