for i in range(int(input())):
    n = int(input())
    values = [i**2 - 1 for i in range(3, int(n**0.5)+2, 2)] 
    i = 0
    for j, v in enumerate(values):
        if v > n:
            break
        i = j+1
    print(i)