from collections import Counter

n, t = map(int, input().split())
A = list(map(int, input().split()))
if t == 1:
    complements = set()
    for i in range(n):
        if A[i] in complements:
            print("Yes")
            exit()
        else:
            complements.add(7777 - A[i])
    print("no")
elif t == 2:
    if len(set(A)) == len(A):
        print("Unique")
    else:
        print("Contains duplicate")
elif t == 3:
    c = Counter(A)
    if c.most_common(1)[0][1] > (n/2):
        print(c.most_common(1)[0][0])
    else:
        print(-1)
elif t == 4:
    A.sort()
    if n % 2 == 1:
        print(A[n//2])
    else:
        print(A[n//2] - 1, A[n//2])
else:
    A.sort()
    print(*[num for num in A if 100 <= num <= 999])
    