ranges = []

# Input
for i in range(int(input())):
    high, low = map(int, input().split())
    ranges.append((high, low))

# Logic
rooms = 0
rmv_indices = []
while ranges:
    rooms += 1
    level = min(high for low, high in ranges)
    for i in range(len(ranges)):
        if ranges[i][0] <= level <= ranges[i][1]:
            rmv_indices.append(i)
    for i in rmv_indices[::-1]:
        ranges.pop(i)
    
    rmv_indices.clear()
    
print(rooms)
