n, p = map(int, input().split())
piles = [list(map(int, input().split()))[1:] for i in range(p)]

for i in range(int(input())):
    s, d, num = map(int, input().split())
    s, d = s-1, d-1
    piles[d] += piles[s][-num:]
    piles[s] = piles[s][:-num]
    
for i in range(p):
    print(*piles[i])