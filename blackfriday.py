n = int(input())

nums = list(map(int, input().split()))
snums = sorted(nums, reverse=True)


seen = True
curr = -1
for i in range(n):
    if seen:
        if snums[i] == curr:
            continue
        else:
            curr = snums[i]
            seen = False
    else:
        if snums[i] == curr:
            seen = True
        else:
            print(nums.index(curr) + 1)
            exit()
if seen == False:
    print(nums.index(curr) + 1)
else:
    print("none")