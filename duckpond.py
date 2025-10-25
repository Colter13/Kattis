n, m = map(int, input().split())
l = list(range(1, n+1))
out = [-1 for i in range(n)]
start = -1
for i in range(1, n+1):
    start = (start + m) % len(l)
    out[l.pop(start)-1] = i
    start -= 1 # accounts for removing item
print(*out)