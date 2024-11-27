n = int(input())

nums = []
ans = []

for i in range(n):
    nums.append(int(input()))

for i in range(n//2, 0, -1):
    works = True
    if n % i == 0:
        currmax = 0
        for j in range(0, n//i):
            p = nums[i*j:i*j+i]
            if min(p) > currmax:
                currmax = max(p)
            else:
                works = False
                break
        if works:
            ans.append(n//i)

if nums == nums.sort():
    ans.append(n)

for i in ans:
    print(i)
if len(ans) == 0:
    print(-1)
