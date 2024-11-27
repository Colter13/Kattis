n = input()
while len(n) > 1:
    product = 1
    for digit in n:
        if digit != '0':
            product *= int(digit)
    n = str(product)
print(n)
