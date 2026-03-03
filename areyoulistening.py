import math

x, y, n = map(int, input().split())

def calc_dist(x1, y1, d):
    x2 = abs(x-x1)
    y2 = abs(y-y1)
    h = (x2**2 + y2**2)**0.5
    return h - d

l = []
for i in range(n):
    x1, y1, d = map(int, input().split())
    l.append(calc_dist(x1, y1, d))
l.sort()
print(max(0, math.floor(l[2])))