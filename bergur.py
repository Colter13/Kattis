n = int(input())
l = list(map(int, input().split()))
newl = [0 for i in range(n)]
newl[-1] = l[-1]
for i in range(n-2, -1, -1):
    newl[i] = min(newl[i+1], l[i])
print(sum(newl))
