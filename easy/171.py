s = "AB"

out = 0

for h, i in enumerate(s):
	val = ord(i) - 64
	out += val * 26 ** (len(s) - 1 - h)

return out
