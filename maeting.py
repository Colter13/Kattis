names = {}
for i in range(int(input())):
    names[input()] = 0
for i in range(int(input())):
    _, *attenders = input().split()
    for name in attenders:
        names[name] += 1
names = dict(sorted(names.items(), key=lambda x: x[1])[::-1])
names = list((value, key) for key, value in names.items())
for i, name in names:
    print(i, name)
