from math import pi

total = 0
sectors = int(input())
for i in range(sectors):
    d, i, o = map(int, input().split())
    O = pi * (o)**2 *(d/360)
    I = pi * (i)**2 *(d/360)
    total += O-I
    print(O, I)
print(total)