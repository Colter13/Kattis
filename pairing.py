a, b, c, d = map(int, input().split())
a = a % 2
c = c % 2
e = min(b,d)
b = b - e
d = d - e
if a and d:
    d -= 1
if c and b:
    b -= 1

total = b + d
    
if not b:
    total += a
if not d:
    total += c
print(total)