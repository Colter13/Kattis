from collections import deque

for _ in range(int(input())):
    s = int(input())

    d = {}

    for __ in range(s):
        i, *x = input().split()
        d[i] = x
    
    stack = deque(["1"])

    fav_endings = 0
    while stack:
        curr = stack.pop()
        l = d[curr]
        if len(l) == 1:
            if l[0] == 'favourably':
                fav_endings += 1
        else:
            stack.extend(l)
    
    print(fav_endings)