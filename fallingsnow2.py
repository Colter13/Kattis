rows, columns = map(int, input().split())

M = [list(input()) for i in range(rows)]
M = [sorted([row[i] for row in M]) for i in range(len(M[0]))]
M = [[row[i] for row in M] for i in range(len(M[0]))]

for row in M:
    print(''.join(row))