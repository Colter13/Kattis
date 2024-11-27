names, rows, columns = map(int, input().split())
m = [list(input().split()) for i in range(rows)]
n = [input() for i in range(names)]
for i in range(rows):
    if m[i][0] == n[i*columns]:
        print("left")
    else:
        print("right")