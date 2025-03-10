x = input()
t = 0
h = 0
for ch in x:
    if ch == 'T':
        t += 1
    elif ch == 'H':
        h += 1
    if (h >= 11 or t >= 11) and abs(h-t) >= 2:
        t = 0
        h = 0
print(f"{t}-{h}")