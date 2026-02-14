from math import ceil

c = {
    'S': 0,
    'M': 0,
    'L': 0
}

for i in range(int(input())):
    size, slices = input().split()
    c[size] += int(slices)

print(ceil(c['S'] / 6) + ceil(c['M'] / 8) + ceil(c['L'] / 12))