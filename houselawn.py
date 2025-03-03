l, m = map(int, input().split())
mowers = []
for i in range(m):
    n, *x = input().split(',')
    p, c, t, r = map(int, x)
    mowers.append((n, p, c, t, r))

capable = []
price = float('inf')

for mower in mowers:
    n, p, c, t, r = mower
    cycles = 10080/(t+r)
    grass = cycles * c * t
    if grass >= l:
        if p < price:
            price = p
            capable = [n]
        elif p == price:
            capable.append(n)

if not capable:
    print("no such mower")
else:
    print(*capable, sep='\n')