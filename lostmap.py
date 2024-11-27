from math import inf

rows = int(input())
columns = rows

M = [list(map(int, input().split())) for _ in range(columns)]
master_indices = []

for i in range(rows):
    minimum = inf
    indices = []
    for j in range(columns):
        item = M[i][j]
        if item < minimum and item != 0:
            minimum = item
            indices = [(i + 1, j + 1)]
        elif item == minimum:
            indices.append((i + 1, j + 1))
    master_indices += indices
#master_indices = [(min(i, j), max(i, j)) for i, j in master_indices]
for i, j in set(master_indices):
    print(i, j)

"""
This seems to be a cheese way of doing this problem and likely is a flawed approach.
Only passes the first four cases.
"""
