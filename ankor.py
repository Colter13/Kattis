from statistics import median

n = int(input())

m = 1e-6 # addresses colinearity

y_d = []
for i in range(2*n):
    x, y = map(int, input().split())
    y_d.append(y - m*x)

print(m, median(y_d))