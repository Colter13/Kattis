nums = [int(input()) for i in range(9)]
is_found = False
for i in range(9):
    if is_found == True:
            break
    for j in range(i + 1, 9):
        if is_found == True:
            break
        nums2 = nums.copy()
        nums2.remove(nums2[j])
        nums2.remove(nums2[i])
        if sum(nums2) == 100:
            for num in nums2:
                print(num)
            is_found = True