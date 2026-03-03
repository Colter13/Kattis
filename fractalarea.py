import math

for i in range(int(input())):
    r, n = map(int, input().split())
    area = math.pi * (r**2)
    curr = 1
    for i in range(n-1):
        r /= 2
        if i == 0:
            curr *= 4
        else:
            curr *= 3
        area += curr * math.pi * (r**2)
    print(area)