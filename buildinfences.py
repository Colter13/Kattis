miny = 1e6
maxy = 0
minx = 1e6
maxx = 0
for i in range(int(input())):
    x, y = map(int, input().split())
    miny = min(miny, y)
    maxy = max(maxy, y)
    minx = min(minx, x)
    maxx = max(maxx, x)
print(2*(maxy-miny+2) + 2*(maxx-minx+2))