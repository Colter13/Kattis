base = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for _ in range(int(input())):
    s1 = input()
    s2 = input()
    s1IsGreater = True
    if len(s1) > len(s2):   # s1 is greater
        s1IsGreater = True
    elif len(s2) > len(s1):      # s2 is greater
        s1IsGreater = False
    else:   # length is equal
        for i in range(len(s1)):
            if base.index(s1[i]) > base.index(s2[i]):
                s1IsGreater = True
                break
            elif base.index(s2[i]) > base.index(s1[i]):
                s1IsGreater = False
                break
    if (s1IsGreater and (s1 > s2)) or (not s1IsGreater and (s2 > s1)):
        print("YES")
    else:
        print("NO")