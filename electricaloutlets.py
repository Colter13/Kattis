for i in range(int(input())):
    strips, *outlets = map(int, input().split())
    print(sum(outlets) - len(outlets) + 1)
