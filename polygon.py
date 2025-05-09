def area(points):
    m = len(points)
    a = 0
    for i in range(m):
        next = (i + 1) % m
        x1, y1 = points[i]
        x2, y2 = points[next]
        a += x1*y2 - x2*y1
    return a / 2

n = int(input())
for i in range(n):
    m, *rest = map(int, input().split())
    points = list(zip(rest[::2], rest[1::2]))
    print(area(points))
