s = "3+2*2"

num = 0
stack = []
op = '+'
s += '#'
for i in range(len(s)):
    if s[i].isdigit():
        num = 10 * num + int(s[i])
    elif not s[i].isspace() or i == len(s) - 1:
        if op == '-':
            stack.append(-num)
        elif op == '+':
            stack.append(num)
        elif op == '*':
            stack.append(stack.pop() * num)
        else:
            stack.append(int(stack.pop() / num))
        op = s[i]
        num = 0
return sum(stack)
