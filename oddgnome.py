for i in range(int(input())):
    x = list(map(int, input().split()))
    gnomes = x[1:]
    for i in range(1, x[0]-1):
        if gnomes[i] != gnomes[i-1] + 1:
            print(i+1)
            break
