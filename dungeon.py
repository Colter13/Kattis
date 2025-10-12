from collections import deque

while True:
    l, r, c = map(int, input().split())

    if l == 0:
        exit()

    # input grid
    g = [[] for i in range(l)]
    for d in range(l):
        for i in range(r):
            g[d].append(list(input()))
        input()

    # find S and E
    start = ()
    end = ()
    for d in range(l):
        for i in range(r):
            for j in range(c):
                if g[d][i][j] == 'S':
                    start = (d, i, j)
                if g[d][i][j] == 'E':
                    end = (d, i, j)

    # bfs
    q = deque([start])
    g[start[0]][start[1]][start[2]] = 0

    while q:
        a, b, d = q.pop()

        shifts = [(0, 0, 1), (0, 0, -1), 
                  (0, 1, 0), (0, -1, 0),
                  (1, 0, 0), (-1, 0, 0)]
        
        for shift in shifts:
            if a + shift[0] < l and a + shift[0] >= 0 and \
               b + shift[1] < r and b + shift[1] >= 0 and \
               d + shift[2] < c and d + shift[2] >= 0:
                if str(g[a + shift[0]][b + shift[1]][d + shift[2]]) in ".E":
                    q.appendleft((a + shift[0], b + shift[1], d + shift[2]))
                    g[a + shift[0]][b + shift[1]][d + shift[2]] = g[a][b][d] + 1

    if str(g[end[0]][end[1]][end[2]]) == "E":
        print("Trapped!")
    else:
        print(f"Escaped in {g[end[0]][end[1]][end[2]]} minute(s).")
