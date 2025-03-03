import sys
import re

for line in sys.stdin:
    x = line.split()
    total = 0
    num = 0
    name = []
    numbers = "1234567890."
    for elem in x:
        if any([elem[i] not in numbers for i in range(len(elem))]):
            name.append(elem)
        else:
            total += float(elem)
            num += 1
    print(total/num, *name)