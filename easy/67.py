a = "11"
b = "1"

carry = 0
binarysum = ''

while a or b:
	if not a:
		a = '0'
	elif not b:
		b = '0'

	ab = int(a[-1]) + int(b[-1]) + carry
	carry = ab // 2
	ab %= 2
	binarysum = ''.join([str(ab), binarysum])
	a = a[:-1]
	b = b[:-1]

if carry:
	binarysum = ''.join([str(carry), binarysum])

return binarysum
