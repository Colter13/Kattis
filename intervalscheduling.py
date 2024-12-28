interval = []
n = int(input())
for i in range(n):
    start, end = map(int, input().split())
    interval.append((start, end))
print(interval)

overlaps = {i: [] for i in range(n)}
for i in range(n-1):
    for j in range(i+1, n):
        if interval[i][1] > interval[j][0]:
            overlaps[i].append(j)
            overlaps[j].append(i)

for i, row in overlaps.items():
    print(f"{i}: {row}")