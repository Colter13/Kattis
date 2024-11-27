x, y, x1, y1, x2, y2 = map(int, input().split())

if x in range(x1, x2+1):
    print(min(abs(y-y1), abs(y-y2)))
elif y in range(y1, y2+1):
    print(min(abs(x-x1), abs(x-x2)))
else:
    minx = min(abs(x-x1), abs(x-x2))
    miny = print(min(abs(y-y1), abs(y-y2)))
    print((minx**2 + miny**2)**0.5)
