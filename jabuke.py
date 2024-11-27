def triangle_area(triangle):
    (xa, ya), (xb, yb), (xc, yc) = triangle
    return abs(xa*(yb-yc) + xb*(yc-ya) + xc*(ya-yb)) / 2

def is_in_triangle(triangle, point, area):
    test1 = [point, triangle[1], triangle[2]]
    test2 = [triangle[0], point, triangle[2]]
    test3 = [triangle[0], triangle[1], point]
    area -= triangle_area(test1) + triangle_area(test2) + triangle_area(test3)
    return area == 0

# Input
triangle = []
for x in range(3):
    x, y = map(int, input().split())
    triangle.append((x, y))
points = []
for i in range(int(input())):
    x, y = map(int, input().split())
    points.append((x, y))

# Calculate area
area = triangle_area(triangle)

# Output
print(triangle_area(triangle))
print(sum(1 for point in points if is_in_triangle(triangle, point, area)))
