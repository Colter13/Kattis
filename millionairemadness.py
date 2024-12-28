rows, cols = map(int, input().split())

def dfs(a, v, i, j):
    if (i,j) == (rows-1,cols-1):
        return True
    v[i][j] = 1
    for neighbor in a[(i,j)]:
        if v[neighbor[0]][neighbor[1]] == 0 and dfs(a, v, neighbor[0], neighbor[1]):
            return True
    return False

def path(length):
    a = {}
    stack = [(0, 0)]
    p = [[0 for i in range(cols)] for i in range(rows)]
    while len(stack):
        i, j = stack.pop()
        a[(i,j)] = []
        if i+1 < rows and m[i][j] >= m[i+1][j] - length:
            a[(i,j)].append((i+1,j))
            if p[i+1][j] != 1:
                stack.append((i+1,j))
            p[i+1][j] = 1
        if j+1 < cols and m[i][j] >= m[i][j+1] - length:
            a[(i,j)].append((i,j+1))
            if p[i][j+1] != 1:
                stack.append((i,j+1))
            p[i][j+1] = 1
        if i-1 >= 0 and m[i][j] >= m[i-1][j] - length:
            a[(i,j)].append((i-1,j))
            if p[i-1][j] != 1:
                stack.append((i-1,j))
            p[i-1][j] = 1
        if j-1 >= 0 and m[i][j] >= m[i][j-1] - length:
            a[(i,j)].append((i,j-1))
            if p[i][j-1] != 1:
                stack.append((i,j-1))
            p[i][j-1] = 1
    v = [[0 for i in range(cols)] for i in range(rows)]
    if p[rows-1][cols-1] and dfs(a, v, 0, 0):
        return True
    return False

# initialize matrix
m = [list(map(int, input().split())) for i in range(rows)]

min_length = 0
max_length = 1E9
mid_length = -1

# check to override the baseline length
length1 = 0
length2 = 0
if rows > 1 and m[rows-2][cols-1] < m[rows-1][cols-1]:
    length1 = m[rows-1][cols-1] - m[rows-2][cols-1]
if cols > 1 and m[rows-1][cols-2] < m[rows-1][cols-1]:
    length2 = m[rows-1][cols-1] - m[rows-1][cols-2]
min_length = min(length1, length2)

while True:
    mid_length = (min_length + max_length) // 2
    if path(mid_length):
        max_length = mid_length
    else:
        min_length = mid_length
    if max_length == min_length:
        print(int(min_length))
        break
    if (max_length - min_length) == 1:
        if path(min_length):
            print(int(min_length))
        else:
            print(int(max_length))
        break



"""
Use binary search to find the optimal length.
"""