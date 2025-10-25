n, m, q = map(int, input().split())
ss = [input() for i in range(n)]

nope = set()

for _ in range(q):
    x = list(input().split())
    for i in range(n):
        if ss[i][int(x[0])-1] != x[1]:
            nope.add(i)

poss = set(range(n)).difference(nope)

if len(poss) == 1:
    print("unique")
    print(poss.pop()+1)
else:
    print("ambiguous")
    print(len(poss))