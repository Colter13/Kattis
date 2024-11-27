for i in range(int(input())):
    n1 = int(input().replace(" ", ""))
    n2 = int(input().replace(" ", ""))
    n3 = list(str(n1 + n2))
    print(*n3)