n = int(input())
a_count = 0
b_count = 1
for i in range(n):
    temp = a_count
    a_count += b_count - temp
    b_count += temp
    print(a_count, b_count)