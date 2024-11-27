people = int(input())
spaces = list(map(int, input().split()))
order = [1]

for i in range(people - 1):
    order.append(spaces.index(i) + 2)
print(*order)
