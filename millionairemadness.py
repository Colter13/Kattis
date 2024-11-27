rows, cols = map(int, input().split())

M = [list(map(int, input().split())) for i in range(rows)]

C = [[-1 for i in range(cols)] for i in range(rows)]
