points = int(input())
area = 0
x1, y1 = map(float, input().split())
for i in range(points - 1):
    x2, y2 = map(float, input().split())
    area += ((y1 + y2) / 2) * (x2 - x1)
    x1, y1 = x2, y2
print(area / 1000)
