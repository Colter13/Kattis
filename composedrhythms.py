n = int(input())
d = n // 2
t = n % 2
l = [2 for i in range(d)]
l[-1] = l[-1] + t
print(d)
print(*l)