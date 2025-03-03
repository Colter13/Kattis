p = {}
total = 0
solved = 0
while True:
    x = list(input().split())
    print(x)
    if '-1' in x:
        break
    time, letter, result = int(x[0]), x[1], x[2] == "right"
    if result == 1:
        solved += 1
        if letter in p:
            total += time + p[letter] * 20
        else:
            total += time
    else:
        if letter in p:
            p[letter] += 1
        else:
            p[letter] = 1
print(solved, total)