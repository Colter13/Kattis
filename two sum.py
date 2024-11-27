nums = [2,7,11,15]
target = 9


length = len(nums)
for i in range(length):
    for j in range(length):
        if j != i and nums[j] + nums[i] == target:
            print([i, j])
