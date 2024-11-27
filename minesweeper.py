rows, columns, mines = map(int, input().split())
coords = []
for i in range(mines):
    coords.append(tuple((map(int, input().split()))))

M = [['.' for i in range(columns)] for j in range(rows)]

for i, j in coords:
    M[i-1][j-1] = '*'

for row in M:
    print(''.join(row))