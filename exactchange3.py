a = input()
b = input()

needed = 0

if len(a) != len(b):
    needed = max(len(a), len(b))
else:
    leading_1s = 0
    remaining = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            remaining = len(a) - i
            break
        if a[i] == "1":
            leading_1s += 1
    needed = leading_1s + remaining
print(needed)
"""
Leading 1s that are shared + length of the discrepant portion of the string
"""