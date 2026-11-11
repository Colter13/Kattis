def permutation(l):
    diff = l[1]-l[0]
    for i in range(1, n-1):
        if l[i]+diff != l[i+1]:
            return False
    return True

for i in range(int(input())):
    n, *x = map(int, input().split())
    if permutation(x):
        print("arithmetic")
    elif permutation(sorted(x)):
        print("permuted arithmetic")
    else:
        print("non-arithmetic")