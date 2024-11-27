
from collections import Counter

combos = []
total = 0

# Input
for i in range(int(input())):
    combos.append(tuple(set(input().split())))  # Use a tuple so that the Counter has a hashable object

# Create counter object and find the largest element
count = Counter(combos)
largest = max(count.values())

# Find how many combinations are the most popular combination
for combo in combos:
    if tuple(combo) in [combo for combo, i in count.items() if i == largest]:
        total += 1
