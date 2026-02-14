r, c = map(int, input().split())
M = [list(input()) for i in range(r)]
dir = {'E': (0, 1),
        'W': (0, -1),
        'N': (-1, 0),
        'S': (1, 0)}
visited = [[0 for i in range(c)] for i in range(r)]
steps = 0
x, y = 0, 0
while True:
    if M[x][y] == 'T':
        print(steps)
        exit()
    if visited[x][y] == 1:
        print("Lost")
        exit()
    visited[x][y] = 1
    dx, dy = dir[M[x][y]]
    x += dx
    y += dy
    if (not (0 <= x < r)) or (not (0 <= y < c)):
        print("Out")
        exit()
    steps += 1
    