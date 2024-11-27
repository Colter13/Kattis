import math

while True:
    D, V = map(int, input().split())
    if D == 0 and V == 0:
        break
    print(pow((pow(D, 3) - (6 * V) / math.pi), 1/3))