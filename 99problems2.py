import bisect

n, q = map(int, input().split())
diffs = list(map(int, input().split()))

for i in range(q):
    t, d = map(int, input().split())
    if t == 1:
        i = bisect.bisect_right(diffs, d)
        if i == len(diffs):
            print(-1)
        else:
            print(diffs[i])
            diffs.pop(i)
    else:
        i = bisect.bisect_left(diffs, d+1)
        if i == 0:
            print(-1)
        else:
            print(diffs[i-1])
            diffs.pop(i-1)