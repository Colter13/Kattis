x = input().split()
stack = []
for ch in x:
    if ch.isdigit():
        stack.append(int(ch))
    else:
        left = stack.pop()
        right = stack.pop()
        stack.append(eval(f"{left}{ch}{right}"))
print(stack[0])
        