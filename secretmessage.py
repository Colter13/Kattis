from math import ceil, sqrt

for i in range(int(input())):
    s = input()
    k = ceil(sqrt(len(s)))

    M = s.ljust(k * k, '*')
    print(M)

    idx = 0
    for i in range(k):
        for j in range(k):
            if idx == len(s):
                break
            M[i][j] = s[idx]
            idx += 1

    decoded = ''
    for j in range(k):
        for i in range(k-1, -1, -1):
            ch = M[i][j]
            if ch != '*':
                decoded += ch
    
    print(decoded)