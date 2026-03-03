nums = [9, 99, 999, 9999, 99999]
for num in nums:
    start, stop = 0, num
    l = range(start, stop + 1)
    total = 0
    for i in range(len(l)):
        for ch in str(l[i]):
            total += int(ch)
    print(num, total)
