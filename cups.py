data = {}
for _ in range(int(input())):
    a, b = input().split()
    if b.isdigit():
        data[int(b)] = a
    else:
        data[int(int(a) // 2)] = b
for radius in sorted(data.keys()):
    print(data[radius])
