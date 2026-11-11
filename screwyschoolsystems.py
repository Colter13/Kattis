for i in range(int(input())):
    names = list(input().split())
    n = int(len(names)**0.5)
    M = [["" for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            M[i][j] = names[j+i*n]

    shifts = {
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0)
    }
    found = False
    for i in range(n):
        if found:
            break
        for j in range(n):
            same = True
            l = len(M[i][j])
            for shift in shifts:
                if 0 <= i + shift[0] < n and 0 <= j + shift[1] < n and len(M[i+shift[0]][j+shift[1]]) != l:
                    same = False
                    break
            if same:
                found = True
                print(M[i][j])
                break
    if not found:
        print("Name Not Found")

                
                    

