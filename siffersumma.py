n = int(input())
digit_sum = sum([int(ch) for ch in str(n)])

while True:
    n += 1
    if sum([int(ch) for ch in str(n)]) == digit_sum:
        print(n)
        exit()