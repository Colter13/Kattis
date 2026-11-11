l1, l2 = map(int, input().split())
first = input()
second = input()[::-1]
t = int(input())
if t > l1 + l2 - 1:
    print(second[::-1] + first[::-1])
elif t == 0:
    print(first[::-1] + second[::-1])
else:
    out = ""
    for i in range(l1 - t):
        out += first.pop()
    
