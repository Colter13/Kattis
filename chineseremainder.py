for i in range(int(input())):
    a, n, b, m = map(int, input().split())
    x = max(n, m)
    while True:
        if x % n == a and x % m == b:
            break
        x += a
    print(x, n * m)