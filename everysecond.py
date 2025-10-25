x = list(map(int, input().split(' : ')))
s = x[0]*3600 + x[1]* 60 + x[2]
x = list(map(int, input().split(' : ')))
s2 = x[0]*3600 + x[1]* 60 + x[2]
print((s2 - s) % (3600*24))