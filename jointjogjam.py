kx0, ky0, ox0, oy0, kx, ky, ox, oy = map(int, input().split())
distance = 0

calc1 = (abs(kx0-ox0)**2 + abs(ky0-oy0)**2)**0.5
calc2 = (abs(kx-ox)**2 + abs(ky-oy)**2)**0.5

print(max(calc1, calc2))