def dfs(a, v, i, j, rows, cols):
    if (i,j) == (rows-1,cols-1):
        return True
    v[i][j] = 1
    for neighbor in a[(i,j)]:
        if v[neighbor[0]][neighbor[1]] == 0 and dfs(a, v, neighbor[0], neighbor[1], rows, cols):
            return True
    return False

rows, cols = map(int, input().split())

# initialize matrix
m = [list(map(int, input().split())) for i in range(rows)]

length = 0
if max(m[rows-2][cols-1], m[rows-1][cols-2]) < m[rows-1][cols-1]:
    length = m[rows-1][cols-1] - max(m[rows-2][cols-1], m[rows-1][cols-2])

while True:
    a = {}
    for i in range(rows):
        for j in range(cols):
            a[(i,j)] = []
            if i+1 < rows and m[i][j] >= m[i+1][j] - length:
                a[(i,j)].append((i+1,j))
            if j+1 < cols and m[i][j] >= m[i][j+1] - length:
                a[(i,j)].append((i,j+1))
            if i-1 >= 0 and m[i][j] >= m[i-1][j] - length:
                a[(i,j)].append((i-1,j))
            if j-1 >= 0 and m[i][j] >= m[i][j-1] - length:
                a[(i,j)].append((i,j-1))
    v = [[0 for i in range(cols)] for i in range(rows)]
    target_neighbors = []
    if (rows == 1 or (rows-1,cols-1) in a[(rows-2,cols-1)]) or (cols == 1 or (rows-1,cols-1) in a[(rows-1,cols-2)]):
        if dfs(a, v, 0, 0, rows, cols):
            print(length)
            exit()
    length += 1