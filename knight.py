from collections import deque

n = int(input())
g = [list(input()) for i in range(n)]

shifts = [(1, 2), (2, 1),
          (-1, 2), (2, -1),
          (1, -2), (-2, 1),
          (-1, -2), (-2, -1)]

start = tuple()

for i in range(n):
    for j in range(n):
        if g[i][j] == "K":
            start = (i, j) # 0-indexed
            break

q = deque([start])

g[start[0]][start[1]] = 0

while q:
    x, y = q.pop()

    for shift in shifts:
        if x + shift[0] < n and x + shift[0] >= 0 and y + shift[1] < n and y + shift[1] >= 0:
            if g[x + shift[0]][y + shift[1]] == '.':
                g[x + shift[0]][y + shift[1]] = g[x][y] + 1
                q.appendleft((x + shift[0], y + shift[1]))
            elif type(g[x + shift[0]][y + shift[1]]) == int:
                if g[x][y] + 1 < g[x + shift[0]][y + shift[1]]:
                    g[x + shift[0]][y + shift[1]] = g[x][y] + 1
                    q.appendleft((x + shift[0], y + shift[1]))

if type(g[0][0]) == int:
    print(g[0][0])
else:
    print(-1)