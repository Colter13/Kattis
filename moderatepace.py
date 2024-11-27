days = int(input())
plans = []
compromise = []
for i in range(3):
    plans.append(list(map(int, input().split())))
for i in range(days):
    options = sorted([plan[i] for plan in plans])
    compromise.append(options[1])

print(*compromise)
