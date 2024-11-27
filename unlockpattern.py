def find_position(grid, target):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == target:
                return (i, j)

grid = [list(map(int, input().split())) for i in range(3)]

distance = 0

for i in range(1, 9):
    start = find_position(grid, i)
    end = find_position(grid, i+1)
    distance += ((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2) ** 0.5

print(distance)