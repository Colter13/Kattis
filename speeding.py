from math import floor

coords = [tuple(map(int, input().split())) for i in range(int(input()))]
speeds = []
for i in range(len(coords) - 1):
    x1, y1 = coords[i]
    x2, y2 = coords[i+1]
    speeds.append((y2-y1)/(x2-x1))
print(floor(max(speeds)))