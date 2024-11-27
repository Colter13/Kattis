n = int(input())
times = sorted(list(map(int, input().split())), reverse=True)
for i in range(n):
    times[i] += 2 + i
print(max(times))