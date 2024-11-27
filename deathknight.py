def tetrate(n):
    return n**n

n = float(input())
for i in range(10):
    n = tetrate(n)
print(n)
