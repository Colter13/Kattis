import math

for i in range(int(input())):
    p, r, f = map(int, input().split())
    count = 0
    while True:
        if p > f:
            print(count)
            break
        p *= r
        count += 1