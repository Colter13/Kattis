total, k = map(int, input().split())
numbers = list(map(int, input().split()))
for i in range(k - 1, total, k):
    print(numbers[i], end=" ")
