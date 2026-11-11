n = int(input())
weights = []

for i in range(n):
    weights.append(int(input()))

possible = {0}

for weight in weights:
    curr = set()
    for elem in possible:
        if weight + elem < 1334:
           curr.add(weight + elem)
    possible.update(curr)

p = list(possible)
p.sort(key=lambda x: (abs(1000-x), -x))

print(p[0])