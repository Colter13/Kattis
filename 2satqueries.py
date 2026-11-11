from random import shuffle

for i in range(int(input())):
    n = int(input())
    arr = [None] * n

    # determine the values of 1 and 2
    queries = [
        (False, False),
        (True, False),
        (False, True),
        (True, True)
    ]
    shuffle(queries)

    print(f"{'-'*(not queries[0][0])}1 {'-'*(not queries[0][1])}2")
    res = input()
    if res == 'F':
        arr[0] = not queries[0][0]
        arr[1] = not queries[0][1]
    else:
        print(f"{'-'*(not queries[1][0])}1 {'-'*(not queries[1][1])}2")
        res = input()
        if res == 'F':
            arr[0] = not queries[1][0]
            arr[1] = not queries[1][1]
        else:
            print(f"{'-'*(not queries[2][0])}1 {'-'*(not queries[2][1])}2")
            res = input()
            if res == 'F':
                arr[0] = not queries[2][0]
                arr[1] = not queries[2][1]
            else:
                arr[0] = not queries[3][0]
                arr[1] = not queries[3][1]
    
    gimme = -1 if arr[0] else 1
    for i in range(2, n):
        print(gimme, i+1)
        arr[i] = input()  == 'T'
    out = ''
    for ch in arr:
        if ch:
            out += 'T'
        else:
            out += 'F'
    print(out)