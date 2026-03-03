n = int(input())
x, y = map(float, input().split())

dirs = {
    "N": (0, 1),
    "S": (0, -1),
    "W": (-1, 0),
    "E": (1, 0),
    "NE": (0.7071067811865476, 0.7071067811865476),
    "NW": (-0.7071067811865476, 0.7071067811865476),
    "SE": (0.7071067811865476, -0.7071067811865476),
    "SW": (-0.7071067811865476, -0.7071067811865476)
}

for i in range(n-1):
    direction, dist = input().split()
    dist = int(dist)
    x += dirs[direction][0] * dist
    y += dirs[direction][1] * dist
    
print(x, y)