n, current, previous = map(int, input().split())
total = 0
for i in range(n):
    num = int(input())
    if num > (current + previous):
        previous, current = current, num
        total += 1
print(total)
