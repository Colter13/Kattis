N = int(input())
product = 0
i = 0
while product < N:
    product = i * (i + 1) * (i + 2)
    i += 1
print(i - 2)
