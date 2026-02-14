for i in range(int(input())):
    input()
    gn, mgn = map(int, input().split())
    gs = max(list(map(int, input().split())))
    mgs = max(list(map(int, input().split())))
    
    if mgs > gs:
        print("MechaGodzilla")
    else:
        print("Godzilla")