from itertools import permutations

n = int(input())

digits = list(str(n))
perms = permutations(digits)
possible = sorted(list({int(''.join(perm)) for perm in perms}))

idx = possible.index(n)
if idx == len(possible)-1:
    print(0)
else:
    print(possible[idx+1])