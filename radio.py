n, cost = map(int, input().split())
listeners = list(map(int, input().split()))

best = 0
curr = 0

for size in listeners:
    profit = size - cost
    curr += profit

    best = max(best, curr)
    curr = max(0, curr)

print(best)