grid = [input() for i in range(4)]

d = {'A': (0, 0), 'B': (0, 1), 'C': (0, 2), 'D': (0, 3), 
     'E': (1, 0), 'F': (1, 1), 'G': (1, 2), 'H': (1, 3), 
     'I': (2, 0), 'J': (2, 1), 'K': (2, 2), 'L': (2, 3), 
     'M': (3, 0), 'N': (3, 1), 'O': (3, 2)}

scatter = 0
for i in range(4):
    for j in range(4):
        if grid[i][j].isalpha():
            coords = d[grid[i][j]]
            scatter += abs(coords[0] - i)
            scatter += abs(coords[1] - j)
print(scatter)