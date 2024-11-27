def in_circle(point, x, y, r):
    distance = ((point[0]-x)**2 + (point[1]-y)**2)**0.5
    return distance <= r
def in_rectangle(point, x1, y1, x2, y2):
    return ((x1 <= point[0] <= x2) or (x2 <= point[0] <= x1)) and ((y1 <= point[1] <= y2) or (y2 <= point[1] <= y1))


shapes = []
points = []
for i in range(int(input())):
    shapes.append(input().split())
for i in range(int(input())):
    points.append(tuple(map(int, input().split())))
for i in range(len(points)):
    total = 0
    for j in range(len(shapes)):
        if shapes[j][0] == "rectangle":
            x1, y1, x2, y2 = (int(shapes[j][k]) for k in range(1, 5))
            total += in_rectangle(points[i], x1, y1, x2, y2)
        else:
            x, y, r = int(shapes[j][1]), int(shapes[j][2]), int(shapes[j][3])
            total += in_circle(points[i], x, y, r)
    print(total)
