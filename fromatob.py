a, b = map(int, input().split())
steps = 0
if a <= b:
    print(b-a)
else:
    while a > b:
        if a % 2 == 1:
            a += 1
        else:
            a //= 2
        steps += 1
    print(steps + b-a)