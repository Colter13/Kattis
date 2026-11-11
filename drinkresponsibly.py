"""
10.00 9.0 2
fire 2 1/1 4.00
water 10 1/2 2.00
"""

money, units, drinks_number = map(float, input().split())

drinks = {}
for i in range(drinks_number):
    name, strength, size, cost = input().split()
    strength = int(strength)
    size = eval(size)
    cost = float(cost)
