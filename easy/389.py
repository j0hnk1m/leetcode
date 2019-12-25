s = "abcd"
t = "abcde"

hashmap = {}
for i in s:
	if i in hashmap:
		hashmap[i] += 1
	else:
		hashmap[i] = 1

for i in t:
	if i in hashmap:
		hashmap[i] -= 1
	else:
		hashmap[i] = 1

unique = ''
for k in hashmap.keys():
	if hashmap[k] != 0:
		unique = k
return unique
