
while True:
    x = list(input().split())
    if x == ['-1']:
        break
    print(x)
    time, letter, result = int(x[0]), x[1], x[2] == "right"
    print(time, letter, result)