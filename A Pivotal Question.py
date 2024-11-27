partition = []
x = list(map(int, input().split()))
num = x[0]
for i in range(1, num + 1):
    value = True
    for j in range(1, i):
        if x[j] > x[i]:
            value = False
    for k in range(i, num + 1):
        if x[k] < x[i]:
            value = False
    if value == True:
        partition.append(x[i])
str1 = str(len(partition)) + ' '
for i in range(len(partition)):
    if i < 100:
        str1 += str(partition[i]) + ' '
print(str1)
