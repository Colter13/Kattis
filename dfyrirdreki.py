a, b, c = int(input()), int(input()), int(input())
determinant = b**2 - 4 * a * c
if determinant > 0:
    print(2)
elif determinant == 0:
    print(1)
else:
    print(0)