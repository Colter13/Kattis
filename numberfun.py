for i in range(int(input())):
    x, y, z = map(int, input().split())
    able = False
    if x + y == z:
        able = True
    if abs(x - y) == z:
        able = True
    if x * y == z:
        able = True
    if x / y == z:
        able = True
    if y / x == z:
        able = True
    print("Possible" if able else "Impossible")