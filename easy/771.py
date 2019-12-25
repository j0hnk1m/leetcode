J = "aA"
S = "aAAbbbb"

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
