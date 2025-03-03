pizza = []
cost = 0
for i in range(int(input())):
    name, price = input().split()
    pizza.append(int(price))
pizza = sorted(pizza)[::-1]
for i in range(0, len(pizza), 2):
    cost += pizza[i]
print(cost)