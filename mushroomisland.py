def distance(x1, y1, x2, y2):
    return (abs(x1-x2)**2 + abs(y1-y2)**2)**0.5
def valid(point1, point2):
    return distance(point1[0], point1[1], point2[0], point2[1]) >= 10000 
    
n = int(input())
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y, i+1))
    
mushroom = set(points)
while True:
    temp = set()
    mushroom = list(mushroom)
    point1 = mushroom.pop()
    
    for point2 in mushroom:
        if valid(point1, point2):
            temp.add(point2)
    if len(temp) == len(mushroom):
        print(point1[2])
        break
    elif len(temp) == 1:
        print(temp.pop()[2])
        break
    mushroom = temp

