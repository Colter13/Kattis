n, k = map(int, input().split())
times = [0 for i in range(604800000)]
ranges = []
for i in range(n):
    a, b = map(int, input().split())
    ranges.append((a,b))
for i in range(len(ranges)):
    for j in range(ranges[i][0], ranges[i][1]+1):
        times[j] += 1
m = 0
for i in range(0, 604800000-k-1):
    m = max(sum(times[i:i+k+1]), m)
print(m)