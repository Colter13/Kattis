n = int(input())
directions = list(input())
directions.append("R")
locations = []

l = 0
end = -1
for i in range(len(directions)):
    if directions[i] == 'R':
        locations.extend(range(i+1, end+1, -1))
        end = i
        l = end +1
    else:
        l += 1

print(*locations, sep='\n')