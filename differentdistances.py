while True:
    x = input()
    if x == '0':
        break
    
    x1, y1, x2, y2, p = map(float, x.split())
    
    c1 = pow(abs(x1-x2), p)
    c2 = pow(abs(y1-y2), p)
    print(pow(c1 + c2, 1/p))
    