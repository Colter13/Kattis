rows, columns = map(int, input().split())
P = [list(map(int, input().split())) for i in range(rows)]

is_low_pressure = False
for i in range(1, rows - 1):
    if is_low_pressure:
        break
    for j in range(1, columns - 1):
        if P[i-1][j] > P[i][j] and P[i+1][j] > P[i][j] and P[i][j-1] > P[i][j] and P[i][j+1] > P[i][j]:
            is_low_pressure = True
            break
        
print("Jebb" if is_low_pressure else "Neibb")
