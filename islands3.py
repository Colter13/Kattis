def clouds(M, i, j, islands, rows, cols):
    if i-1 >= 0 and M[i-1][j] in ['C', 'L']:
        M[i-1][j] = islands + 1
        clouds(M, i-1, j, islands)
    if i+1 < rows and M[i+1][j] in ['C', 'L']:
        M[i+1][j] = islands + 1
        clouds(M, i+1, j, islands)
    if j-1 >= 0 and M[i][j-1] in ['C', 'L']:
        M[i][j-1] = islands + 1
        clouds(M, i, j-1, islands)
    if j+1 < cols and M[i][j+1] in ['C', 'L']:
        M[i][j+1] = islands + 1
        clouds(M, i, j+1, islands)

rows, cols = map(int, input().split())

M = [list(input()) for i in range(rows)]

islands = 0
for i in range(rows):
    for j in range(cols):
        if M[i][j] == 'L':
            islands += 1
            M[i][j] = islands
            clouds(M, i, j, islands, rows, cols)
print(islands)
                