partition = []
x = list(map(int, input().split()))
values = x[0]
max_left = [0] * (values + 1)
min_right = [0] * (values + 2)
max_left[0] = 0
for i in range(2, values + 2):
    max_left[i] = max(max_left[i - 1], x[i])
min_right[values + 1] = 1000001
for i in range(2, values + 2):
    min_right[i] = min(min_right[i + 1], x[i])
print(max_left)
print(min_right)

#Sample Input:      [3, 1, 5, 4]
#Sample Output:     [1, 1]
#Sample max_right:  [0, 1, 5, 5]
#Sample min_left:   [1, 1, 4, 4, 1000001]
