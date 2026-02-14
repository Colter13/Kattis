alphabet = "ABCDEFGHIJKLMNOP"
corr={alphabet[i]: alphabet[15-i] for i in range(16)}
total = 0
while total < 8:
    inp = input().split()
    total += len(inp)
    print(*map(lambda x: corr[x], inp))
    