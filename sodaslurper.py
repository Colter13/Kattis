# Input
e, f, c = map(int, input().split())

# Variables
bottles = e + f
new_bottles = 0
total = 0

# Bottle Cycle Logic
while bottles >= c:
    new_bottles = bottles // c
    total += new_bottles
    bottles = bottles % c + new_bottles

# Output
print(total)