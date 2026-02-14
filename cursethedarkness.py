for i in range(int(input())):
    xb, yb = map(float, input().split())
    solution = False
    for _ in range(int(input())):
        xc, yc = map(float, input().split())
        if ((abs(xb-xc))**2 + (abs(yb-yc))**2)**0.5 <= 8.0:
            solution = True
    if solution:
        print("light a candle")
    else:
        print("curse the darkness")
