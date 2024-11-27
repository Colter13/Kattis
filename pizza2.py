from math import pi

R, r = map(float, input().split())

big = pi * R ** 2
small = pi * (R - r) ** 2

print((small * 100) / (big))