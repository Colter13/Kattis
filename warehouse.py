for i in range(int(input())):
    d = {}
    for j in range(int(input())):
        toy, num = input().split()
        num = int(num)
        if toy in d:
            d[toy] += num
        else:
            d[toy] = num
    print(len(d))
    for k,v in sorted(d.items(), reverse=True):
        print(k, v)