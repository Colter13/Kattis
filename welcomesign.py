r, c = map(int, input().split())
words = [input() for i in range(r)]
extra = 0
for word in words:
    s = ['.' for i in range(c)]
    gap = (c - len(word))//2
    if (c - len(word)) % 2 == 1:
        if extra == 0:
            extra = 1
        else:
            extra = 0
        for j in range(len(word)):
            s[gap + j + extra] = word[j]
    else:
        for j in range(len(word)):
            s[gap + j] = word[j]
    print(''.join(s))