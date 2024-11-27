total = 0

n = int(input())
if n % 2 != 0:
    print("still running")
else:
    for i in range(0, n, 2):
        total += - int(input()) + int(input())
    print(total)
