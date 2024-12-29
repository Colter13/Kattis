interval = []
n = int(input())
for i in range(n):
    start, end = map(int, input().split())
    interval.append((start, end))
interval = sorted(interval, key=lambda x: x[1])

cnt = 0
curr = 0
for start, end in interval:
    if start >= curr:
        cnt += 1
        curr = end

print(cnt)