while True:
    n = int(input())
    if n == 0:
        exit()
        
    b = []
    for i in range(n):
        x1, y1, x2, y2, size = input().split()
        b.append([float(x1), float(y1), float(x2), float(y2,), size])
    
    for i in range(int(input())):
        printed = False
        x, y, size = input().split()
        x, y = float(x), float(y)
        for box in b:
            if box[0] <= x <= box[2] and box[1] <= y <= box[3]:
                if size == box[4]:
                    print(size, "correct")
                else:
                    print(size, box[4])
                printed = True
        if printed == False:
            print(size,  "floor")
    print()