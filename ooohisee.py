rows, cols = map(int, input().split())

# initialize matrix
M = [input() for i in range(rows)]

locations = 0
x = 9999
y = 9999
for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        if M[i][j] == '0':
            if M[i-1][j-1:j+2] == "OOO" and M[i][j-1] == 'O' and M[i][j+1] == 'O' and M[i+1][j-1:j+2] == "OOO":
                locations += 1
                x = i + 1
                y = j + 1

if locations == 1:
    print(x, y)
elif locations > 1:
    print("Oh no!", locations, "locations")
else:
    print("Oh no!")