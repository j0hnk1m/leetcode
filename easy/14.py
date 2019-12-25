strs = ["flower","flow","flight"]

if not strs:
    return ""

pre = ''
for i, char in enumerate(min(strs, key=len)):
    if all(char == s[i] for s in strs):
        pre += char
    else:
        break
return pre
